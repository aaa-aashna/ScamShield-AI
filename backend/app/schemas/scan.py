"""
Pydantic schemas for scans
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl, Field


class ScanHistoryResponse(BaseModel):
    """Scan history response"""
    id: int
    scan_type: str
    threat_level: str
    is_threat: bool
    confidence_score: float
    risk_percentage: float
    created_at: datetime
    
    class Config:
        from_attributes = True


class EmailScanRequest(BaseModel):
    """Email scan request"""
    sender_email: Optional[str] = None
    subject: Optional[str] = None
    body: str = Field(..., min_length=1)


class EmailScanResponse(BaseModel):
    """Email scan response"""
    id: int
    sender_email: Optional[str]
    subject: Optional[str]
    is_phishing: bool
    confidence_score: float
    threat_level: str
    risk_percentage: float
    suspicious_keywords: Optional[list[str]]
    phishing_indicators: Optional[list[str]]
    explanation: str
    suggested_action: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True


class SMSScanRequest(BaseModel):
    """SMS scan request"""
    phone_number: Optional[str] = None
    message: str = Field(..., min_length=1)


class SMSScanResponse(BaseModel):
    """SMS scan response"""
    id: int
    phone_number: Optional[str]
    message: str
    is_scam: bool
    confidence_score: float
    threat_level: str
    risk_percentage: float
    scam_type: Optional[str]
    explanation: str
    suspicious_keywords: Optional[list[str]]
    suggested_action: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True


class URLScanRequest(BaseModel):
    """URL scan request"""
    url: str = Field(..., min_length=1)


class URLScanResponse(BaseModel):
    """URL scan response"""
    id: int
    url: str
    domain: Optional[str]
    is_malicious: bool
    confidence_score: float
    threat_level: str
    risk_percentage: float
    has_valid_ssl: bool
    ssl_issuer: Optional[str]
    ssl_expiration: Optional[datetime]
    domain_age_days: Optional[int]
    domain_registrar: Optional[str]
    on_blacklist: bool
    explanation: str
    suspicious_indicators: Optional[list[str]]
    suggested_action: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True


class QRScanRequest(BaseModel):
    """QR scan request"""
    image_filename: str = Field(..., min_length=1)
    extracted_url: Optional[str] = None


class QRScanResponse(BaseModel):
    """QR scan response"""
    id: int
    image_filename: str
    extracted_url: Optional[str]
    is_suspicious: bool
    confidence_score: float
    threat_level: str
    risk_percentage: float
    explanation: str
    suggested_action: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True


class ScanStatsResponse(BaseModel):
    """Scan statistics response"""
    total_scans: int
    threats_blocked: int
    safe_messages: int
    phishing_emails: int
    scam_sms: int
    malicious_urls: int
    suspicious_qr_codes: int
    average_confidence_score: float


class RecentScansResponse(BaseModel):
    """Recent scans response"""
    email_scans: list[EmailScanResponse]
    sms_scans: list[SMSScanResponse]
    url_scans: list[URLScanResponse]
    qr_scans: list[QRScanResponse]
