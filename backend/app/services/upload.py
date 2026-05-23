"""Cloudinary image upload service."""

import io
import logging

from fastapi import HTTPException, UploadFile, status
from cloudinary import config as cloudinary_config, uploader

from app.core.config import settings

logger = logging.getLogger(__name__)

ALLOWED_MIME_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

cloudinary_config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
    secure=True,
)


async def upload_image(file: UploadFile) -> str:
    """Validate and upload an image to Cloudinary. Returns the secure URL."""
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid file type '{file.content_type}'. Allowed: {', '.join(sorted(ALLOWED_MIME_TYPES))}",
        )

    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File too large ({len(contents)} bytes). Maximum size: {MAX_FILE_SIZE // (1024 * 1024)} MB",
        )

    try:
        result = uploader.upload(
            io.BytesIO(contents),
            folder="mercha/products",
            resource_type="image",
        )
        logger.info("Uploaded image to Cloudinary: %s", result.get("secure_url"))
        return str(result["secure_url"])
    except Exception as exc:
        logger.exception("Cloudinary upload failed: %s", exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Image upload failed",
        )
