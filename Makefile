.PHONY: help install dev test lint format clean docker docker-build docker-up docker-down migrations

help:
	@echo "ScamShield AI - Development Commands"
	@echo "===================================="
	@echo ""
	@echo "Installation:"
	@echo "  make frontend-install     Install frontend dependencies"
	@echo "  make backend-install      Install backend dependencies"
	@echo "  make install              Install all dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make frontend-dev         Run frontend dev server"
	@echo "  make backend-dev          Run backend dev server"
	@echo "  make dev                  Run both frontend and backend (requires 2 terminals)"
	@echo ""
	@echo "Database:"
	@echo "  make db-migrate           Run database migrations"
	@echo "  make db-seed              Seed database with sample data"
	@echo "  make db-reset             Reset database (WARNING: deletes all data)"
	@echo ""
	@echo "Testing:"
	@echo "  make test-frontend        Run frontend tests"
	@echo "  make test-backend         Run backend tests"
	@echo "  make test                 Run all tests"
	@echo "  make test-cov             Run tests with coverage"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint                 Lint all code"
	@echo "  make format               Format all code"
	@echo "  make type-check           Run type checking"
	@echo ""
	@echo "Docker:"
	@echo "  make docker-build         Build Docker images"
	@echo "  make docker-up            Start Docker containers"
	@echo "  make docker-down          Stop Docker containers"
	@echo "  make docker-logs          View Docker logs"
	@echo "  make docker-clean         Remove Docker images and containers"
	@echo ""
	@echo "Utilities:"
	@echo "  make clean                Clean build and cache files"
	@echo "  make help                 Show this help message"

# Installation
frontend-install:
	cd frontend && npm install
	@echo "✓ Frontend dependencies installed"

backend-install:
	cd backend && python -m venv venv
ifdef OS
	cd backend && venv\Scripts\pip install -r requirements.txt
else
	cd backend && source venv/bin/activate && pip install -r requirements.txt
endif
	@echo "✓ Backend dependencies installed"

install: frontend-install backend-install
	@echo "✓ All dependencies installed"

# Development
frontend-dev:
	cd frontend && npm run dev

backend-dev:
	cd backend && python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

dev: frontend-dev backend-dev

# Database
db-migrate:
	cd backend && alembic upgrade head
	@echo "✓ Database migrations applied"

db-seed:
	cd backend && python -m app.scripts.seed_database
	@echo "✓ Database seeded with sample data"

db-reset:
	@echo "WARNING: This will delete all database data!"
	cd backend && alembic downgrade base && alembic upgrade head
	@echo "✓ Database reset complete"

# Testing
test-frontend:
	cd frontend && npm run test

test-backend:
	cd backend && pytest -v

test-backend-cov:
	cd backend && pytest --cov=app --cov-report=html

test: test-frontend test-backend
	@echo "✓ All tests passed"

# Code Quality
lint:
	cd frontend && npm run lint
	cd backend && flake8 app --count --select=E9,F63,F7,F82 --show-source --statistics
	cd backend && pylint app --disable=C,W
	@echo "✓ Linting complete"

format:
	cd frontend && npm run format
	cd backend && black app && isort app
	@echo "✓ Code formatted"

type-check:
	cd frontend && npx tsc --noEmit
	cd backend && mypy app
	@echo "✓ Type checking complete"

# Docker
docker-build:
	docker-compose build
	@echo "✓ Docker images built"

docker-up:
	docker-compose up -d
	@echo "✓ Docker containers started"
	@echo "Frontend: http://localhost:5173"
	@echo "Backend: http://localhost:8000"
	@echo "API Docs: http://localhost:8000/docs"

docker-down:
	docker-compose down
	@echo "✓ Docker containers stopped"

docker-logs:
	docker-compose logs -f

docker-clean:
	docker-compose down -v
	docker system prune -f
	@echo "✓ Docker cleaned"

# Utilities
clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	cd frontend && rm -rf node_modules dist .vite
	@echo "✓ Clean complete"

.DEFAULT_GOAL := help
