# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastAPI-based personal backend API designed for deployment on AWS App Runner. The application provides a simple, authenticated API with health checking capabilities. The project is a git repository connected to GitHub with automatic deployment configured.

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

### Git Commands
```bash
# Check repository status
git status

# View current changes
git diff

# Add files to staging
git add .
git add specific-file.py

# Commit changes
git commit -m "Description of changes"

# Push to GitHub (triggers auto-deployment)
git push origin main

# View commit history
git log --oneline

# Check remote repository
git remote -v
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
- apprunner.yaml for service configuration (runtime: python311)
- Automatic deployment from GitHub main branch
- Environment variables configured in App Runner service
- GitHub connection for source code access

### Deployment Workflow
1. **Make changes** to code locally
2. **Test locally** using development server
3. **Commit changes** to git: `git add . && git commit -m "Description"`
4. **Push to GitHub**: `git push origin main`
5. **Auto-deployment triggers** in App Runner (monitor via AWS Console)

### Important Notes
- Changes to apprunner.yaml require commit/push to take effect
- App Runner pulls from GitHub repository, not local files
- Auto-deployment is enabled for main branch
- Environment variables (like API_KEY) should be set via AWS Console for security

See deployment.md for detailed deployment instructions including AWS CLI commands and GitHub setup.