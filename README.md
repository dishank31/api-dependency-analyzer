# API Dependency Graph Analyzer

> Automatically maps API dependencies across microservices and predicts which services will break before a breaking change is deployed.

![Status](https://img.shields.io/badge/Status-In%20Development-yellow)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green)
![License](https://img.shields.io/badge/License-MIT-purple)

---

## Problem

In microservice architectures, teams change APIs without knowing which other services depend on them. Breaking changes are discovered in production — not before deployment.

**The three core pain points:**
- No visibility into which services consume a specific API
- No tool auto-discovers dependencies from logs
- No tool predicts which services will break before a change is deployed

**Real-world impact:**
- Netflix (2008) — 3-day outage from a single cascading change
- Uber — routine outages across 1300+ microservices after any maintenance
- Anonymous Fintech — silent runtime failures from a single field rename

---

## Solution

API Dependency Graph Analyzer automatically maps API dependencies by analyzing call logs and predicts which services will break when contracts change — before the change is deployed.

**What makes it different from existing tools:**

| Capability | Backstage | LogClaw | Swagger | This Tool |
|---|---|---|---|---|
| Auto-discovers dependencies | No | Partial | No | Yes |
| Works from logs | No | Yes | No | Yes |
| Pre-deployment prediction | No | No | No | Yes |
| Visual dependency graph | Manual | No | No | Yes |
| Blast radius analysis | No | Reactive | No | Proactive |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Web Framework | FastAPI |
| Database | PostgreSQL (Supabase) |
| ORM | SQLAlchemy 2.0 |
| Authentication | JWT (PyJWT + bcrypt) |
| Validation | Pydantic V2 |
| Testing | pytest + httpx |
| Server | uvicorn |

---

## Project Structure

```
api-dependency-analyzer/
├── src/
│   ├── main.py           # FastAPI app entry point
│   ├── config.py         # Environment configuration
│   ├── models/           # SQLAlchemy database models
│   ├── routes/           # API endpoint definitions
│   ├── services/         # Business logic layer
│   ├── middleware/       # JWT auth and request handling
│   └── utils/            # Shared helper functions
├── tests/                # pytest test suite
├── migrations/           # Database migrations (Alembic)
├── docs/
│   ├── PROBLEM_RESEARCH.md
│   ├── diagrams/         # Architecture diagrams
│   └── api-spec/         # OpenAPI specifications
├── requirements.txt
├── .env.example
└── README.md
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL (or Supabase account)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/dishank31/api-dependency-analyzer.git
cd api-dependency-analyzer
```

**2. Create and activate virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure environment variables**
```bash
copy env.example .env
```

Open `.env` and fill in your values:
```
DATABASE_URL=postgresql://postgres:[YOUR-PASSWORD]@db.xxxx.supabase.co:5432/postgres
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
```

**5. Run the development server**
```bash
uvicorn src.main:app --reload
```

**6. Open API docs**

Navigate to `http://localhost:8000/docs` to view the interactive Swagger UI.

---

## Development Progress

| Day | Topic | Status |
|---|---|---|
| Day 1 | Environment Setup + Problem Research | ✅ Complete |
| Day 2 | Database Schema + Models | 🚧 Up Next |
| Day 3 | Authentication System | ⏳ Pending |
| Day 4 | Core API Routes | ⏳ Pending |
| Day 5 | Dependency Graph Engine | ⏳ Pending |
| Day 6 | Log Analysis + Auto Discovery | ⏳ Pending |
| Day 7 | Break Prediction Algorithm | ⏳ Pending |

---

## Author

**Dishank** — [@dishank31](https://github.com/dishank31)

---

## License

This project is licensed under the MIT License.

---

*🚧 This project is currently in active development.*
