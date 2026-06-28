"""
Scan models for email, SMS, URL, and QR scans
"""

from datetime import datetime
from typing import Optional

from sqlalchemy import String, Float, Integer, ForeignKey, DateTime, Text, Boolean, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum

from app.models.base import Base, TimestampMixin


class ScanType(str, enum.Enum):
    """Scan types"""
    EMAIL = "email"
    SMS = "sms"
    URL = "url"
    QR_CODE = "qr_code"
    WEBSITE = "website"


class ThreatLevel(str, enum.Enum):
    """Threat severity levels"""
    SAFE = "safe"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ScanHistory(Base, TimestampMixin):
    """Scan history tracking"""
    
    __tablename__ = "scan_history"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    
    scan_type: Mapped[ScanType] = mapped_column(SQLEnum(ScanType), nullable=False)
    threat_level: Mapped[ThreatLevel] = mapped_column(SQLEnum(ThreatLevel), nullable=False)
    
    is_threat: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    confidence_score: Mapped[float] = mapped_column(Float, nullable=False)
    risk_percentage: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Relationships
    user: Mapped["User"] = relationship(back_populates="scan_history")
    
    def __repr__(self) -> str:
        return f"<ScanHistory {self.scan_type} - {self.threat_level}>"


class EmailScan(Base, TimestampMixin):
    """Email scanning results"""
    
    __tablename__ = "email_scans"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    
    # Email content
    sender_email: Mapped[Optional[str]] = mapped_column(String(255))
    subject: Mapped[Optional[str]] = mapped_column(String(500))
    body: Mapped[Optional[str]] = mapped_column(Text)
    
    # Analysis results
    is_phishing: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    confidence_score: Mapped[float] = mapped_column(Float, nullable=False)
    threat_level: Mapped[ThreatLevel] = mapped_column(SQLEnum(ThreatLevel), nullable=False)
    risk_percentage: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Suspicious indicators
    suspicious_keywords: Mapped[Optional[str]] = mapped_column(Text)  # JSON array
    phishing_indicators: Mapped[Optional[str]] = mapped_column(Text)  # JSON array
    
    # Explanation
    explanation: Mapped[Optional[str]] = mapped_column(Text)
    suggested_action: Mapped[Optional[str]] = mapped_column(String(500))
    
    # Relationships
    user: Mapped["User"] = relationship(back_populates="email_scans", foreign_keys=[user_id])
    
    def __repr__(self) -> str:
        return f"<EmailScan {self.sender_email} - {self.threat_level}>"


class SMSScan(Base, TimestampMixin):
    """SMS scanning results"""
    
    __tablename__ = "sms_scans"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    
    # SMS content
    phone_number: Mapped[Optional[str]] = mapped_column(String(20))
    message: Mapped[str] = mapped_column(Text, nullable=False)
    
    # Analysis results
    is_scam: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    confidence_score: Mapped[float] = mapped_column(Float, nullable=False)
    threat_level: Mapped[ThreatLevel] = mapped_column(SQLEnum(ThreatLevel), nullable=False)
    risk_percentage: Mapped[float] = mapped_column(Float, nullable=False)
    
    # Scam type
    scam_type: Mapped[Optional[str]] = mapped_column(String(100))  # banking, otp, lottery, delivery, upi, etc.
    
    # Explanation
    explanation: Mapped[Optional[str]] = mapped_column(Text)
    suspicious_keywords: Mapped[Optional[str]] = mapped_column(Text)  # JSON array
    suggested_action: Mapped[Optional[str]] = mapped_column(String(500))
    
    # Relationships
    user: Mapped["User"] = relationship(back_populates="sms_scans", foreign_keys=[user_id])
    
    def __repr__(self) -> str:
        return f"<SMSScan {self.threat_level}>"


class URLScan(Base, TimestampMixin):
    """URL scanning results"""
    
    __tablename__ = "url_scans"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    
    # URL
    url: Mapped[str] = mapped_column(String(2048), nullable=False)
    domain: Mapped[Optional[str]] = mapped_column(String(255))
    
    # Analysis results
    is_malicious: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    confidence_score: Mapped[float] = mapped_column(Float, nullable=False)
    threat_level: Mapped[ThreatLevel] = mapped_column(SQLEnum(ThreatLevel), nullable=False)
    risk_percentage: Mapped[float] = mapped_column(Float, nullable=False)
    
    # SSL Certificate
    has_valid_ssl: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    ssl_issuer: Mapped[Optional[str]] = mapped_column(String(255))
    ssl_expiration: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    
    # Domain Information
    domain_age_days: Mapped[Optional[int]] = mapped_column(Integer)
    domain_registrar: Mapped[Optional[str]] = mapped_column(String(255))
    
    # Detection
    on_blacklist: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    virustotal_detection: Mapped[Optional[str]] = mapped_column(Text)  # JSON
    urlscan_result: Mapped[Optional[str]] = mapped_column(Text)  # JSON
    
    # Explanation
    explanation: Mapped[Optional[str]] = mapped_column(Text)
    suspicious_indicators: Mapped[Optional[str]] = mapped_column(Text)  # JSON array
    suggested_action: Mapped[Optional[str]] = mapped_column(String(500))
    
    # Relationships
    user: Mapped["User"] = relationship(back_populates="url_scans", foreign_keys=[user_id])
    
    def __repr__(self) -> str:
        return f"<URLScan {self.domain}>"


class QRScan(Base, TimestampMixin):
    """QR code scanning results"""
    
    __tablename__ = "qr_scans"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    
    # QR Code
    image_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    extracted_url: Mapped[Optional[str]] = mapped_column(String(2048))
    
    # Analysis results
    is_suspicious: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    confidence_score: Mapped[float] = mapped_column(Float, nullable=False)
    threat_level: Mapped[ThreatLevel] = mapped_column(SQLEnum(ThreatLevel), nullable=False)
    risk_percentage: Mapped[float] = mapped_column(Float, nullable=False)
    
    # URL Analysis (if URL extracted)
    url_analysis: Mapped[Optional[str]] = mapped_column(Text)  # JSON
    
    # Explanation
    explanation: Mapped[Optional[str]] = mapped_column(Text)
    suggested_action: Mapped[Optional[str]] = mapped_column(String(500))
    
    # Relationships
    user: Mapped["User"] = relationship(back_populates="qr_scans", foreign_keys=[user_id])
    
    def __repr__(self) -> str:
        return f"<QRScan {self.threat_level}>"


# Add relationships to User model
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User
else:
    pass
