"""
User and Role models
"""

from datetime import datetime
from typing import Optional

from sqlalchemy import String, Boolean, Index, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Role(Base, TimestampMixin):
    """User roles"""
    
    __tablename__ = "roles"
    __table_args__ = (Index("ix_roles_name", "name", unique=True),)
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255))
    
    # Relationships
    users: Mapped[list["User"]] = relationship(back_populates="role", cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        return f"<Role {self.name}>"


class User(Base, TimestampMixin):
    """User model"""
    
    __tablename__ = "users"
    __table_args__ = (
        Index("ix_users_email", "email", unique=True),
        Index("ix_users_username", "username", unique=True),
    )
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    full_name: Mapped[Optional[str]] = mapped_column(String(255))
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    role_id: Mapped[Optional[int]] = mapped_column(ForeignKey("roles.id"), nullable=True)
    
    # Profile
    avatar_url: Mapped[Optional[str]] = mapped_column(String(500))
    phone_number: Mapped[Optional[str]] = mapped_column(String(20))
    country: Mapped[Optional[str]] = mapped_column(String(100))
    
    # Preferences
    notifications_enabled: Mapped[bool] = mapped_column(Boolean, default=True)
    dark_mode: Mapped[bool] = mapped_column(Boolean, default=True)
    
    # Security
    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    login_attempts: Mapped[int] = mapped_column(default=0, nullable=False)
    locked_until: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    role: Mapped[Optional["Role"]] = relationship(back_populates="users")
    scan_history: Mapped[list["ScanHistory"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    threat_reports: Mapped[list["ThreatReport"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    feedback: Mapped[list["Feedback"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    notifications: Mapped[list["Notification"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    email_scans: Mapped[list["EmailScan"]] = relationship(back_populates="user", cascade="all, delete-orphan", foreign_keys="EmailScan.user_id")
    sms_scans: Mapped[list["SMSScan"]] = relationship(back_populates="user", cascade="all, delete-orphan", foreign_keys="SMSScan.user_id")
    url_scans: Mapped[list["URLScan"]] = relationship(back_populates="user", cascade="all, delete-orphan", foreign_keys="URLScan.user_id")
    qr_scans: Mapped[list["QRScan"]] = relationship(back_populates="user", cascade="all, delete-orphan", foreign_keys="QRScan.user_id")
    
    def __repr__(self) -> str:
        return f"<User {self.username}>"


from datetime import datetime
from sqlalchemy import DateTime, ForeignKey
