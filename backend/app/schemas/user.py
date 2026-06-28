"""
Pydantic schemas for authentication and users
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class RoleBase(BaseModel):
    """Base role schema"""
    name: str = Field(..., min_length=1, max_length=50)
    description: Optional[str] = Field(None, max_length=255)


class RoleCreate(RoleBase):
    """Create role schema"""
    pass


class RoleResponse(RoleBase):
    """Role response schema"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class UserBase(BaseModel):
    """Base user schema"""
    username: str = Field(..., min_length=3, max_length=255)
    email: EmailStr
    full_name: Optional[str] = Field(None, max_length=255)


class UserCreate(UserBase):
    """Create user schema"""
    password: str = Field(..., min_length=8)
    
    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        """Validate password strength"""
        if not any(char.isupper() for char in v):
            raise ValueError("Password must contain uppercase letter")
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain digit")
        if not any(char in "!@#$%^&*()" for char in v):
            raise ValueError("Password must contain special character")
        return v


class UserUpdate(BaseModel):
    """Update user schema"""
    full_name: Optional[str] = Field(None, max_length=255)
    avatar_url: Optional[str] = None
    phone_number: Optional[str] = None
    country: Optional[str] = None
    notifications_enabled: Optional[bool] = None
    dark_mode: Optional[bool] = None


class UserResponse(UserBase):
    """User response schema"""
    id: int
    is_active: bool
    is_verified: bool
    is_admin: bool
    avatar_url: Optional[str]
    phone_number: Optional[str]
    country: Optional[str]
    notifications_enabled: bool
    dark_mode: bool
    last_login: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class UserDetailResponse(UserResponse):
    """Detailed user response"""
    role: Optional[RoleResponse]


# Authentication schemas
class TokenData(BaseModel):
    """Token data"""
    sub: int
    exp: datetime
    iat: datetime
    type: str = "access"


class TokenResponse(BaseModel):
    """Token response"""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int


class LoginRequest(BaseModel):
    """Login request"""
    email: EmailStr
    password: str


class SignupRequest(UserCreate):
    """Signup request"""
    pass


class RefreshTokenRequest(BaseModel):
    """Refresh token request"""
    refresh_token: str


class PasswordResetRequest(BaseModel):
    """Password reset request"""
    email: EmailStr


class PasswordResetConfirm(BaseModel):
    """Password reset confirmation"""
    token: str
    new_password: str
    confirm_password: str
    
    @field_validator("new_password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        """Validate password strength"""
        if not any(char.isupper() for char in v):
            raise ValueError("Password must contain uppercase letter")
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain digit")
        if not any(char in "!@#$%^&*()" for char in v):
            raise ValueError("Password must contain special character")
        return v


class EmailVerificationRequest(BaseModel):
    """Email verification request"""
    token: str


class ChangePasswordRequest(BaseModel):
    """Change password request"""
    old_password: str
    new_password: str
    confirm_password: str


class MessageResponse(BaseModel):
    """Generic message response"""
    message: str
    status: str = "success"
