"""
FastAPI Application Entry Point
Initializes and configures the ScamShield AI backend
"""

import logging
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.logging import setup_logging
from app.database.session import engine
from app.models.base import Base
from app.routers import auth, users, scans, admin, threats, dashboard
from app.middleware.rate_limit import RateLimitMiddleware
from app.middleware.error_handler import ErrorHandlerMiddleware

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)


# Lifespan events
@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
    """Manage application lifecycle"""
    # Startup
    logger.info("Starting ScamShield AI Backend...")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Debug Mode: {settings.DEBUG}")
    
    # Create database tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    logger.info("✓ Database tables created")
    
    yield
    
    # Shutdown
    logger.info("Shutting down ScamShield AI Backend...")


# Create FastAPI app
app = FastAPI(
    title="ScamShield AI",
    description="Production-grade AI Cybersecurity Platform",
    version="1.0.0",
    lifespan=lifespan,
)


# Middleware
app.add_middleware(ErrorHandlerMiddleware)
app.add_middleware(RateLimitMiddleware)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health check endpoint
@app.get("/health")
async def health_check() -> dict[str, Any]:
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "environment": settings.ENVIRONMENT,
    }


# API Routes
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(scans.router, prefix="/api/v1/scans", tags=["Scans"])
app.include_router(threats.router, prefix="/api/v1/threats", tags=["Threats"])
app.include_router(dashboard.router, prefix="/api/v1/dashboard", tags=["Dashboard"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["Admin"])


# Root endpoint
@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint"""
    return {
        "message": "Welcome to ScamShield AI",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
    }


# 404 Handler
@app.exception_handler(404)
async def not_found_exception_handler(request: Any, exc: Exception) -> JSONResponse:
    """Handle 404 errors"""
    return JSONResponse(
        status_code=404,
        content={
            "detail": "Not found",
            "path": str(request.url),
        },
    )


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="info",
    )
