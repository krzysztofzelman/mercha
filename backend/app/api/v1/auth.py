"""Auth endpoints — register, login, refresh, me."""

import logging

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.user import User
from app.schemas import (
    RegisterRequest, LoginRequest, RefreshRequest, TokenResponse, UserResponse, MessageResponse,
)
from app.services import auth as auth_service

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/register", response_model=TokenResponse)
async def register(body: RegisterRequest, db: AsyncSession = Depends(get_db)):
    try:
        user = await auth_service.register_user(db, body.email, body.password, body.first_name, body.last_name)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    tokens = await auth_service.create_tokens(db, user)
    return TokenResponse(**tokens)


@router.post("/login", response_model=TokenResponse)
async def login(body: LoginRequest, db: AsyncSession = Depends(get_db)):
    try:
        user = await auth_service.authenticate_user(db, body.email, body.password)
    except Exception as exc:
        logger.error("Login exception for %s: %s", body.email, exc, exc_info=True)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    tokens = await auth_service.create_tokens(db, user)
    return TokenResponse(**tokens)


@router.post("/refresh", response_model=TokenResponse)
async def refresh(body: RefreshRequest, db: AsyncSession = Depends(get_db)):
    tokens = await auth_service.refresh_access_token(db, body.refresh_token)
    if not tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    return TokenResponse(**tokens)


@router.get("/me", response_model=UserResponse)
async def get_me(user: User = Depends(get_current_user)):
    return user
