# ScamShield AI - Production-Grade AI Cybersecurity Platform

A comprehensive, intelligent cybersecurity platform that detects scams across multiple communication channels using AI, Machine Learning, NLP, and Threat Intelligence.

## Features

### Detection Capabilities
- **Email Phishing Detection**: Identify phishing emails with confidence scores and explanations
- **SMS Scam Detection**: Detect banking scams, OTP scams, lottery scams, and delivery fraud
- **URL Analysis**: SSL certificate validation, domain age, redirect chains, WHOIS data, blacklist checks
- **QR Code Phishing**: Upload QR images for automatic analysis and security reports
- **Fake Website Detection**: Detect banking website impersonation and login page phishing
- **Investment Fraud**: Identify crypto scams, investment frauds, and financial scams
- **Social Engineering Detection**: Flag social engineering attempts

### Core Features
- **Professional Dashboard**: Real-time analytics with threat trends, security scores, and activity monitoring
- **Explainable AI**: Understand WHY a message is flagged as a scam (not just "Scam/Safe")
- **Threat Intelligence**: Latest phishing campaigns, malicious domains, trending attacks
- **Admin Dashboard**: User management, threat reports, system health, model performance
- **Full Authentication**: JWT, OAuth2, email verification, password reset, refresh tokens
- **Dark Mode**: Professional cybersecurity theme with responsive design

## Architecture

### Tech Stack

**Frontend:**
- React 19 + TypeScript
- Vite for fast builds
- Tailwind CSS + shadcn/ui for UI
- TanStack Query for state management
- React Hook Form + Zod for form validation
- Recharts for analytics
- Framer Motion for animations

**Backend:**
- FastAPI + Python 3.12
- SQLAlchemy ORM
- PostgreSQL database
- Redis caching
- Celery for async tasks
- JWT + OAuth2 authentication

**AI/ML:**
- Hugging Face Transformers
- DistilBERT for text classification
- Sentence Transformers for semantic analysis
- XGBoost + LightGBM for ensemble models
- SHAP for explainability

**DevOps:**
- Docker & Docker Compose
- GitHub Actions
- PostgreSQL + Redis containerization



## 📝 API Examples

### Email Scanning
```bash
curl -X POST http://localhost:8000/api/v1/scans/email \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "email_content": "Click here to verify your account..."
  }'
```

### SMS Scanning
```bash
curl -X POST http://localhost:8000/api/v1/scans/sms \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "sms_content": "Your OTP is 123456..."
  }'
```

### URL Analysis
```bash
curl -X POST http://localhost:8000/api/v1/scans/url \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/login"
  }'
```

## 📊 Dashboard Features

### User Dashboard
- Total scans performed
- Threats blocked count
- Safe messages count
- Weekly analytics chart
- Threat distribution pie chart
- Recent scan history
- Security score calculation
- User activity timeline

### Admin Dashboard
- User management (CRUD)
- Threat report analysis
- System health monitoring
- Model performance metrics
- Audit logs
- System settings

## 🔐 Security Features

- JWT Authentication with refresh tokens
-  OAuth2 integration ready
- Password hashing (bcrypt)
-  Rate limiting on API endpoints
-  CORS configuration
-  Input validation (Pydantic)
-  SQL injection protection
-  XSS protection
-  CSRF protection
- Secure environment variables
-  Email verification
-  Password reset with token

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest                 # Run all tests
pytest -v             # Verbose output
pytest --cov          # Coverage report
```

### Frontend Tests
```bash
cd frontend
npm run test           # Run all tests
npm run test:ui       # UI mode
```
