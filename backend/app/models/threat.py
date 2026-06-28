"""
Threat and reporting models
"""

from datetime import datetime
from typing import Optional

from sqlalchemy import String, Integer, ForeignKey, DateTime, Text, Boolean, JSON, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

from app.models.base import Base, TimestampMixin


class ReportStatus(str, enum.Enum):
    """Report status"""
    OPEN = "open"
    INVESTIGATING = "investigating"
    RESOLVED = "resolved"
    CLOSED = "closed"


class ThreatReport(Base, TimestampMixin):
    """User-submitted threat reports"""
    
    __tablename__ = "threat_reports"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    
    # Report details
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    threat_type: Mapped[str] = mapped_column(String(100), nullable=False)  # phishing, malware, scam, etc.
    
    # Evidence
    url: Mapped[Optional[str]] = mapped_column(String(2048))
    email: Mapped[Optional[str]] = mapped_column(String(255))
    phone_number: Mapped[Optional[str]] = mapped_column(String(20))
    evidence_text: Mapped[Optional[str]] = mapped_column(Text)
    
    # Status
    status: Mapped[ReportStatus] = mapped_column(SQLEnum(ReportStatus), default=ReportStatus.OPEN, nullable=False)
    severity: Mapped[str] = mapped_column(String(50), nullable=False)  # low, medium, high, critical
    
    # Admin notes
    admin_notes: Mapped[Optional[str]] = mapped_column(Text)
    
    # Relationships
    user: Mapped["User"] = relationship(back_populates="threat_reports")
    
    def __repr__(self) -> str:
        return f"<ThreatReport {self.title} - {self.status}>"


class Feedback(Base, TimestampMixin):
    """User feedback and feature requests"""
    
    __tablename__ = "feedback"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    
    # Feedback
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    feedback_type: Mapped[str] = mapped_column(String(50), nullable=False)  # bug, feature, improvement, complaint
    
    rating: Mapped[Optional[int]] = mapped_column(Integer)  # 1-5 stars
    
    # Response
    admin_response: Mapped[Optional[str]] = mapped_column(Text)
    is_responded: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    # Relationships
    user: Mapped["User"] = relationship(back_populates="feedback")
    
    def __repr__(self) -> str:
        return f"<Feedback {self.title}>"


class Notification(Base, TimestampMixin):
    """User notifications"""
    
    __tablename__ = "notifications"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    
    # Notification
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    notification_type: Mapped[str] = mapped_column(String(50), nullable=False)  # threat_detected, report_response, system_alert
    
    # Status
    is_read: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    # Reference
    related_scan_id: Mapped[Optional[int]] = mapped_column(Integer)
    related_report_id: Mapped[Optional[int]] = mapped_column(Integer)
    
    # Relationships
    user: Mapped["User"] = relationship(back_populates="notifications")
    
    def __repr__(self) -> str:
        return f"<Notification {self.title}>"


class AuditLog(Base, TimestampMixin):
    """System audit logs"""
    
    __tablename__ = "audit_logs"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # Action details
    action: Mapped[str] = mapped_column(String(100), nullable=False)
    resource_type: Mapped[str] = mapped_column(String(50), nullable=False)
    resource_id: Mapped[Optional[int]] = mapped_column(Integer)
    
    # User
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"), nullable=True)
    ip_address: Mapped[Optional[str]] = mapped_column(String(50))
    user_agent: Mapped[Optional[str]] = mapped_column(String(500))
    
    # Changes
    old_values: Mapped[Optional[str]] = mapped_column(Text)  # JSON
    new_values: Mapped[Optional[str]] = mapped_column(Text)  # JSON
    
    # Status
    status: Mapped[str] = mapped_column(String(50), nullable=False)  # success, failed
    error_message: Mapped[Optional[str]] = mapped_column(Text)
    
    def __repr__(self) -> str:
        return f"<AuditLog {self.action} - {self.resource_type}>"


class Settings(Base, TimestampMixin):
    """System settings"""
    
    __tablename__ = "settings"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # Setting key and value
    key: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    value: Mapped[str] = mapped_column(Text, nullable=False)
    
    # Metadata
    description: Mapped[Optional[str]] = mapped_column(String(500))
    is_public: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    def __repr__(self) -> str:
        return f"<Settings {self.key}>"
