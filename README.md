# 🧵 StitchCore — Platforma E-commerce

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react&logoColor=white)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3-06B6D4?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![MUI](https://img.shields.io/badge/MUI-5-007FFF?style=for-the-badge&logo=mui&logoColor=white)](https://mui.com/)

---

Uproszczona platforma e-commerce dla marki odzieżowo-obuwniczej. Projekt demonstracyjny zbudowany w architekturze **frontend + backend**, gotowy do lokalnego uruchomienia oraz wdrożenia na VPS.

---

## 🚀 Demo na żywo

| Aplikacja | URL |
|-----------|-----|
| 🛍️ **Sklep kliencki** | [http://31.3.218.196:5173](http://31.3.218.196:5173) |
| 🔧 **Panel administracyjny** | [http://31.3.218.196:5174](http://31.3.218.196:5174) |
| 📚 **Dokumentacja API (Swagger)** | [http://31.3.218.196:8000/docs](http://31.3.218.196:8000/docs) |

### 🔐 Dane testowe — panel admina

| Pole | Wartość |
|------|---------|
| 📧 Email | `admin@stitchcore.pl` |
| 🔑 Hasło | `admin123` |

---

## 📸 Zrzuty ekranu

| Sklep kliencki | Panel administracyjny |
|----------------|----------------------|
| ![Shop Screenshot](https://placehold.co/600x400/1a1a2e/e0e0e0?text=Sklep+StitchCore) | ![Admin Screenshot](https://placehold.co/600x400/1a1a2e/e0e0e0?text=Panel+Admina) |

> Zrzuty ekranu zostaną wkrótce zastąpione rzeczywistymi obrazami platformy.

---

## 🧱 Stack technologiczny

| Warstwa | Technologia |
|---------|------------|
| 🖥️ **Backend** | FastAPI + SQLAlchemy (async) + SQLite (aiosqlite) |
| 🛍️ **Frontend Shop** | Vite + React 18 + Tailwind CSS + React Router |
| 🔧 **Frontend Admin** | Vite + React 18 + Material UI + React Router |
| 🔐 **Auth** | JWT (python-jose) + bcrypt (passlib) |
| 🗄️ **Baza danych** | SQLite (brak PostgreSQL, brak Celery) |
| 🐳 **Infrastruktura** | Docker + Docker Compose |

---

## 📁 Struktura projektu

```
stitchcore/
├── backend/                # 🖥️ FastAPI backend
│   ├── app/
│   │   ├── main.py         # Entry point (app factory)
│   │   ├── core/           # Config, database, security, deps
│   │   ├── models/         # SQLAlchemy ORM (user, product, order, inventory)
│   │   ├── schemas/        # Pydantic validation
│   │   ├── api/v1/         # REST endpoints (auth, products, orders, inventory)
│   │   └── services/       # Business logic layer
│   ├── alembic/            # Migracje bazy danych
│   ├── requirements.txt
│   └── .env.example
├── frontend-shop/          # 🛍️ Sklep kliencki (Vite + React + Tailwind)
│   ├── src/
│   │   ├── api/            # Axios client
│   │   ├── contexts/       # Auth, Cart
│   │   ├── components/     # Navbar, Footer, ProductCard
│   │   └── pages/          # Home, Products, Cart, Checkout, Account, Login, Register
│   └── package.json
├── frontend-admin/         # 🔧 Panel administracyjny (Vite + React + MUI)
│   ├── src/
│   │   ├── api/            # Axios client
│   │   ├── contexts/       # Auth
│   │   ├── components/     # Layout with drawer
│   │   └── pages/          # Dashboard, Products, Orders, Inventory
│   └── package.json
├── docker-compose.yml      # 🐳 Orchestracja kontenerów
├── docker/                 # Pliki Dockerfile
├── docs/                   # Dokumentacja
├── scripts/                # Skrypty pomocnicze
└── README.md
```

---

## ✨ Funkcjonalności

### 🛍️ Sklep kliencki
- Przeglądanie produktów z kategoriami
- Dodawanie do koszyka i zarządzanie nim
- Składanie zamówień (płatność przy odbiorze)
- Historia zamówień konta użytkownika
- Rejestracja i logowanie

### 🔧 Panel administracyjny
- Zarządzanie produktami i wariantami
- Zarządzanie zamówieniami (zmiana statusu, numer przesyłki)
- Zarządzanie stanami magazynowymi i lokalizacjami
- Podgląd ruchów magazynowych

### 🔐 Autoryzacja
- JWT z odświeżaniem tokenu (access + refresh)
- Role użytkowników: `customer`, `admin`

---

## 📋 Wymagania

| Narzędzie | Wersja |
|-----------|--------|
| 🐍 Python | 3.12+ |
| 🟩 Node.js | 18+ |
| 📦 npm | 9+ |

---

## 🚀 Uruchomienie lokalne

### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Backend uruchomi się na **http://localhost:8000**  
Dokumentacja API: **http://localhost:8000/docs**

### 2. Frontend — Sklep

```bash
cd frontend-shop
npm install
npm run dev
```

Sklep uruchomi się na **http://localhost:5173**

### 3. Frontend — Panel Admina

```bash
cd frontend-admin
npm install
npm run dev
```

Panel admina uruchomi się na **http://localhost:5174**

---

## 🧪 Pierwsze uruchomienie

Backend automatycznie:
- ✅ Tworzy tabele przy starcie (Alembic migration)
- ✅ Tworzy domyślnego administratora: **admin@stitchcore.pl** / **admin123**

Aby zalogować się do panelu admina (http://localhost:5174/login):
- **Email:** `admin@stitchcore.pl`
- **Hasło:** `admin123`

### 🌱 Seed danych (opcjonalnie)

Aby wypełnić bazę przykładowymi produktami (T-shirt, Jeansy, Buty, Plecak, Czapka) wraz z wariantami i stanami magazynowymi:

```bash
cd backend
python -m app.scripts.seed_data
```

---

## 📡 API Endpoints

| Metoda | Endpoint | Opis | Auth |
|--------|----------|------|------|
| `POST` | `/api/v1/auth/register` | Rejestracja użytkownika | — |
| `POST` | `/api/v1/auth/login` | Logowanie | — |
| `POST` | `/api/v1/auth/refresh` | Odświeżenie tokenu | — |
| `GET` | `/api/v1/auth/me` | Profil użytkownika | JWT |
| `GET` | `/api/v1/products` | Lista produktów | — |
| `GET` | `/api/v1/products/{id}` | Szczegóły produktu | — |
| `POST` | `/api/v1/products` | Dodaj produkt | Admin |
| `PUT` | `/api/v1/products/{id}` | Edytuj produkt | Admin |
| `POST` | `/api/v1/products/{id}/variants` | Dodaj wariant | Admin |
| `GET` | `/api/v1/categories` | Lista kategorii | — |
| `POST` | `/api/v1/categories` | Dodaj kategorię | Admin |
| `GET` | `/api/v1/orders` | Lista zamówień | JWT |
| `GET` | `/api/v1/orders/{id}` | Szczegóły zamówienia | JWT |
| `POST` | `/api/v1/orders` | Złóż zamówienie | JWT |
| `PATCH` | `/api/v1/orders/{id}/status` | Aktualizacja statusu | Admin |
| `GET` | `/api/v1/inventory/stock` | Stan magazynowy | Admin |
| `POST` | `/api/v1/inventory/stock/adjust` | Korekta stanu | Admin |
| `GET` | `/api/v1/inventory/locations` | Lokalizacje magazynowe | Admin |
| `POST` | `/api/v1/inventory/locations` | Dodaj lokalizację | Admin |
| `GET` | `/api/v1/inventory/movements` | Ruchy magazynowe | Admin |

---

## 🗺️ Planowane moduły

- [ ] 🔗 Integracja z **Allegro API**
- [ ] 💳 Płatności online (**Stripe** / **Przelewy24**)
- [ ] 📦 Wysyłka (**InPost** / **DPD**)
- [ ] 📧 Powiadomienia email (**SendGrid**)
- [ ] 📊 Raporty (**ReportLab** / **OpenPyXL**)
- [ ] 👁️ Monitorowanie (**Sentry**)

---

## 🐳 Uruchomienie przez Docker

```bash
docker-compose up --build
```

---

## 🤖 CI/CD

Projekt zawiera konfigurację GitHub Actions (`.github/workflows/ci.yml`), która automatycznie:

- 🔍 Sprawdza poprawność kodu backendu (Python) — uruchamia testy API
- 🔍 Sprawdza poprawność kodu frontend-shop (TypeScript) — kompilacja
- 🔍 Sprawdza poprawność kodu frontend-admin (TypeScript) — kompilacja

### Uruchomienie testów lokalnie

```bash
# Backend — uruchom serwer w tle, a następnie testy
cd backend
uvicorn app.main:app --reload &
cd ..
python test_all.py

# Frontend — sprawdź TypeScript
cd frontend-shop && npx tsc --noEmit
cd ../frontend-admin && npx tsc --noEmit
```

> **⚠️ Uwaga:** Upewnij się, że plik `.env` NIE jest commitowany do repozytorium (znajduje się w `.gitignore`). Skorzystaj z szablonu `.env.example`.

---

## 📄 Licencja

Projekt jest przeznaczony wyłącznie do celów demonstracyjnych i edukacyjnych.
