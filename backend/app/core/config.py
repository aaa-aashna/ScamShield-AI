"""
Application configuration settings
"""

from typing import Any

from pydantic_settings import BaseSettings
from functools import cached_property


class Settings(BaseSettings):
    """Application settings"""
    
    # App Settings
    APP_NAME: str = "ScamShield AI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    
    # Server
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    
    # Security
    SECRET_KEY: str = "your-secret-key-change-this-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    JWT_REFRESH_EXPIRATION_DAYS: int = 7
    SECURE_COOKIES: bool = False
    SECURE_HTTPS_ONLY: bool = False
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/scamshield"
    DATABASE_ECHO: bool = False
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 10
    DATABASE_POOL_TIMEOUT: int = 30
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    REDIS_DB: int = 0
    
    # Celery
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"
    
    # CORS
    CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
    ]
    ALLOWED_HOSTS: list[str] = ["localhost", "127.0.0.1", "*"]
    
    # Email
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = "your-email@gmail.com"
    SMTP_PASSWORD: str = "your-app-password"
    SMTP_FROM_EMAIL: str = "noreply@scamshield-ai.com"
    SMTP_FROM_NAME: str = "ScamShield AI"
    
    # OAuth2 (Optional)
    GOOGLE_CLIENT_ID: str | None = None
    GOOGLE_CLIENT_SECRET: str | None = None
    GITHUB_CLIENT_ID: str | None = None
    GITHUB_CLIENT_SECRET: str | None = None
    
    # API Keys
    VIRUSTOTAL_API_KEY: str | None = None
    URLSCAN_API_KEY: str | None = None
    
    # AI/ML Configuration
    MODEL_CACHE_DIR: str = "./models"
    MAX_UPLOAD_SIZE_MB: int = 10
    BATCH_SIZE: int = 32
    
    # File Upload
    UPLOAD_DIR: str = "./uploads"
    ALLOWED_FILE_EXTENSIONS: list[str] = ["txt", "pdf", "jpg", "png", "jpeg"]
    MAX_FILE_SIZE: int = 10485760  # 10MB
    
    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FILE: str = "logs/scamshield.log"
    
    # Sentry (Error Tracking - Optional)
    SENTRY_DSN: str | None = None
    
    # Rate Limiting
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_PERIOD: int = 60  # seconds
    
    # Pagination
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100
    
    # Feature Flags
    ENABLE_EMAIL_VERIFICATION: bool = True
    ENABLE_OAUTH2: bool = False
    ENABLE_ADMIN_PANEL: bool = True
    
    class Config:
        """Pydantic config"""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
    
    @cached_property
    def database_settings(self) -> dict[str, Any]:
        """Get database connection settings"""
        return {
            "url": self.DATABASE_URL,
            "echo": self.DATABASE_ECHO,
            "pool_size": self.DATABASE_POOL_SIZE,
            "max_overflow": self.DATABASE_MAX_OVERFLOW,
            "pool_timeout": self.DATABASE_POOL_TIMEOUT,
        }
    
    @cached_property
    def celery_settings(self) -> dict[str, Any]:
        """Get Celery settings"""
        return {
            "broker": self.CELERY_BROKER_URL,
            "backend": self.CELERY_RESULT_BACKEND,
        }


# Global settings instance
settings = Settings()
