# ScamShield AI - Production-Grade AI Cybersecurity Platform

A comprehensive, intelligent cybersecurity platform that detects scams across multiple communication channels using AI, Machine Learning, NLP, and Threat Intelligence.

## 🎯 Features

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

## 🏗️ Architecture

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

## 📦 Project Structure

```
ScamShield-AI/
├── frontend/                 # React application
│   ├── src/
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/          # Page components
│   │   ├── layouts/        # Layout components
│   │   ├── hooks/          # Custom React hooks
│   │   ├── contexts/       # React contexts
│   │   ├── services/       # API services
│   │   ├── types/          # TypeScript types
│   │   ├── utils/          # Utilities
│   │   ├── assets/         # Images, fonts
│   │   ├── App.tsx         # Root component
│   │   └── main.tsx        # Entry point
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   └── vitest.config.ts
│
├── backend/                 # FastAPI application
│   ├── app/
│   │   ├── routers/        # API endpoints
│   │   ├── services/       # Business logic
│   │   ├── repositories/   # Data access
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── models/         # SQLAlchemy models
│   │   ├── middleware/     # Custom middleware
│   │   ├── core/           # Core settings
│   │   ├── security/       # Auth, JWT, etc.
│   │   ├── database/       # Database config
│   │   ├── ai_models/      # ML models
│   │   ├── utils/          # Utilities
│   │   ├── tasks/          # Celery tasks
│   │   ├── tests/          # Test suite
│   │   └── main.py         # App entry
│   ├── migrations/         # Alembic migrations
│   ├── requirements.txt
│   ├── pytest.ini
│   ├── .env.example
│   └── Dockerfile
│
├── docker-compose.yml      # Container orchestration
├── Dockerfile              # Backend Docker image
├── Makefile               # Development commands
├── README.md              # This file
├── INSTALLATION.md        # Setup guide
├── API_DOCUMENTATION.md   # API reference
├── ARCHITECTURE.md        # System architecture
├── DEPLOYMENT.md          # Deployment guide
├── CONTRIBUTING.md        # Contribution guidelines
└── .env.example           # Example environment variables
```

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ (for frontend)
- Python 3.12+ (for backend)
- PostgreSQL 14+
- Redis 7+
- Docker & Docker Compose

### Option 1: Using Docker Compose (Recommended)

```bash
# Clone and setup
git clone https://github.com/yourusername/ScamShield-AI.git
cd ScamShield-AI

# Copy environment file
cp .env.example .env

# Start all services
docker-compose up -d

# Initialize database
docker-compose exec backend python -m alembic upgrade head

# Access the application
# Frontend: http://localhost:5173
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Option 2: Local Development

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
# Runs on http://localhost:5173
```

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Start Redis (required)
# Windows: WSL with Redis, or use docker
docker run -d -p 6379:6379 redis:7

# Start PostgreSQL (required)
# Use docker, or install locally

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload
# Runs on http://localhost:8000
```

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

- ✅ JWT Authentication with refresh tokens
- ✅ OAuth2 integration ready
- ✅ Password hashing (bcrypt)
- ✅ Rate limiting on API endpoints
- ✅ CORS configuration
- ✅ Input validation (Pydantic)
- ✅ SQL injection protection
- ✅ XSS protection
- ✅ CSRF protection
- ✅ Secure environment variables
- ✅ Email verification
- ✅ Password reset with token

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

## 📚 Documentation

- [Installation Guide](./INSTALLATION.md) - Detailed setup instructions
- [API Documentation](./API_DOCUMENTATION.md) - Complete API reference
- [Architecture Guide](./ARCHITECTURE.md) - System design and components
- [Deployment Guide](./DEPLOYMENT.md) - Production deployment
- [Contributing Guide](./CONTRIBUTING.md) - Contributing guidelines

## 🛠️ Development Commands

```bash
# Root directory Makefile
make frontend-install    # Install frontend dependencies
make backend-install     # Install backend dependencies
make frontend-dev        # Run frontend dev server
make backend-dev         # Run backend dev server
make db-migrate          # Run database migrations
make db-seed             # Seed database with sample data
make test-frontend       # Run frontend tests
make test-backend        # Run backend tests
make lint               # Lint all code
make format             # Format all code
make docker-build       # Build Docker images
make docker-up          # Start Docker containers
make docker-down        # Stop Docker containers
```

## 🎨 UI Features

- Modern cybersecurity theme with dark mode
- Responsive design (mobile, tablet, desktop)
- Smooth animations and transitions
- Loading skeletons for better UX
- Toast notifications for user feedback
- Real-time data charts and graphs
- Professional dashboard layouts
- Accessibility compliance (WCAG 2.1)

## 📈 Scalability

- Horizontal scaling ready with containerization
- Async task processing with Celery
- Redis caching for performance
- Database connection pooling
- Load balancing ready
- CDN optimization for static assets

## 🔄 CI/CD

GitHub Actions workflows included:
- Automated testing on push
- Code quality checks
- Security scanning
- Docker image building
- Deployment to staging/production

## 📄 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## 📞 Support

- 📧 Email: support@scamshield-ai.com
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions

## 🎓 Portfolio Value

This project demonstrates:
- Full-stack development expertise
- AI/ML integration in production
- Cloud-native architecture
- DevOps best practices
- Cybersecurity principles
- Clean code principles
- Professional project structure
- Production-grade quality

---

**Built with ❤️ for AI/ML Portfolio**
