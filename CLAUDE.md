# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastAPI-based personal backend API designed for deployment on AWS App Runner. The application provides a simple, authenticated API with health checking capabilities.

## Architecture

The application follows a clean FastAPI structure:

- **app/main.py**: FastAPI application entry point with CORS middleware and route definitions
- **app/auth.py**: Bearer token authentication using HTTPBearer security
- **app/config.py**: Settings management with environment variable loading via python-dotenv
- **run.py**: Development server runner script with auto-reload
- **Dockerfile**: Multi-stage container build for production deployment
- **apprunner.yaml**: AWS App Runner configuration for cloud deployment

## Common Development Commands

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Start development server with auto-reload
python run.py

# Alternative: Direct uvicorn command
uvicorn app.main:app --reload

# Alternative: Using module syntax
python -m app.main
```

### Testing
```bash
# Test health endpoint (replace YOUR_API_KEY with actual key)
curl -H "Authorization: Bearer YOUR_API_KEY" http://localhost:8000/health

# Test root endpoint (no auth required)
curl http://localhost:8000/
```

### Docker
```bash
# Build Docker image
docker build -t my-backend .

# Run container
docker run -p 8000:8000 my-backend
```

## Configuration

Environment variables are managed through `.env` file and loaded via python-dotenv:

- `API_KEY`: Bearer token for authentication (default: "your-secure-api-key-here")
- `HOST`: Server bind address (default: "0.0.0.0")
- `PORT`: Server port (default: 8000)
- `LOG_LEVEL`: Logging level (default: "info")

## Authentication

All protected endpoints require Bearer token authentication. The API key is validated against the `API_KEY` environment variable in `app/config.py:14-15`.

## Dependencies

Core dependencies (requirements.txt):
- FastAPI 0.104.1 - Web framework
- Uvicorn 0.24.0 - ASGI server
- python-dotenv 1.0.0 - Environment variable management
- python-multipart 0.0.6 - Form data parsing

## Deployment

The application is configured for AWS App Runner deployment with:
- Dockerfile for containerization
- apprunner.yaml for service configuration
- Automatic deployment from GitHub main branch
- Environment variables configured in App Runner service

See deployment.md for detailed deployment instructions including AWS CLI commands and GitHub setup.