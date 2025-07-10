# Deployment Guide - FastAPI Backend with AWS App Runner

This guide will help you deploy your FastAPI backend to AWS App Runner and manage the project with GitHub. Written for novice users using PowerShell.

## Prerequisites

Before starting, ensure you have:
- Python 3.11 or higher installed
- PowerShell (comes with Windows)
- Git installed
- An AWS account
- A GitHub account

## Part 1: Setting Up Your Development Environment

### 1. Install Required Tools

#### Install AWS CLI
```powershell
# Download and install AWS CLI from: https://aws.amazon.com/cli/
# After installation, verify:
aws --version
```

#### Install GitHub CLI (optional but recommended)
```powershell
# Download and install from: https://cli.github.com/
# After installation, verify:
gh --version
```

### 2. Set Up Local Development

#### Create a Virtual Environment
```powershell
# Navigate to your project directory
cd C:\Users\Marcin_Scianski\my-backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

#### Configure Environment Variables
```powershell
# Copy the example environment file
Copy-Item .env.example .env

# Edit .env file and replace 'your-secure-api-key-here' with a strong API key
# You can use any text editor like notepad
notepad .env
```

#### Test Locally
```powershell
# IMPORTANT: Make sure you're in the project root directory
# Run the application locally using uvicorn (recommended)
uvicorn app.main:app --reload

# Alternative: Run using Python module syntax
python -m app.main

# Test the health endpoint (in another PowerShell window)
# Replace 'your-api-key' with your actual API key
curl -H "Authorization: Bearer your-api-key" http://localhost:8000/health
```

## Part 2: GitHub Repository Setup

### 1. Initialize Git Repository
```powershell
# Initialize git repository
git init

# Add all files to staging
git add .

# Create initial commit
git commit -m "Initial commit: FastAPI backend with health endpoint"
```

### 2. Create GitHub Repository

#### Option A: Using GitHub CLI
```powershell
# Login to GitHub
gh auth login

# Create repository
gh repo create my-backend --public --description "Personal FastAPI backend"

# Push to GitHub
git remote add origin https://github.com/YOUR_USERNAME/my-backend.git
git branch -M main
git push -u origin main
```

#### Option B: Using GitHub Web Interface
1. Go to https://github.com/new
2. Repository name: `my-backend`
3. Description: `Personal FastAPI backend`
4. Select Public or Private
5. Click "Create repository"
6. Follow the instructions to push existing repository:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/my-backend.git
git branch -M main
git push -u origin main
```

## Part 3: AWS App Runner Deployment

### 1. Configure AWS Credentials
```powershell
# Configure AWS CLI with your credentials
aws configure

# You'll be prompted for:
# - AWS Access Key ID
# - AWS Secret Access Key
# - Default region (e.g., us-east-1)
# - Default output format (json)
```

### 2. Create App Runner Service

#### Update apprunner.yaml
Before deployment, update the API key in `apprunner.yaml`:
```powershell
notepad apprunner.yaml
# Replace 'your-secure-api-key-here' with your actual API key
```

#### Deploy using AWS CLI
```powershell
# Create the service (replace YOUR_USERNAME with your GitHub username)
aws apprunner create-service `
  --service-name "my-backend-api" `
  --source-configuration '{
    "ImageRepository": {
      "ImageIdentifier": "public.ecr.aws/docker/library/python:3.11-slim",
      "ImageConfiguration": {
        "Port": "8000"
      }
    },
    "AutoDeploymentsEnabled": true,
    "CodeRepository": {
      "RepositoryUrl": "https://github.com/YOUR_USERNAME/my-backend",
      "SourceCodeVersion": {
        "Type": "BRANCH",
        "Value": "main"
      },
      "CodeConfiguration": {
        "ConfigurationSource": "CONFIGURATION_FILE"
      }
    }
  }'
```

### 3. Monitor Deployment
```powershell
# Check service status
aws apprunner describe-service --service-arn "your-service-arn"

# List all App Runner services
aws apprunner list-services
```

## Part 4: Testing Your Deployed API

### 1. Get Service URL
```powershell
# Get service details and find the ServiceUrl
aws apprunner describe-service --service-arn "your-service-arn"
```

### 2. Test the Health Endpoint
```powershell
# Test the deployed API (replace YOUR_SERVICE_URL and YOUR_API_KEY)
curl -H "Authorization: Bearer YOUR_API_KEY" https://YOUR_SERVICE_URL/health
```

Expected response:
```json
{"message": "Everything looks great!"}
```

## Part 5: Managing Your Project

### Daily Workflow
```powershell
# Pull latest changes
git pull origin main

# Make your changes to the code
# ...

# Stage changes
git add .

# Commit changes
git commit -m "Description of your changes"

# Push to GitHub (will trigger auto-deployment)
git push origin main
```

### Environment Management
```powershell
# To update environment variables in App Runner:
aws apprunner update-service `
  --service-arn "your-service-arn" `
  --source-configuration '{
    "CodeRepository": {
      "CodeConfiguration": {
        "ConfigurationSource": "CONFIGURATION_FILE"
      }
    }
  }'
```

## Part 6: Troubleshooting

### Common Issues

#### 1. PowerShell Execution Policy
If you get execution policy errors:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 2. Virtual Environment Issues
If virtual environment doesn't activate:
```powershell
# Use full path
C:\Users\Marcin_Scianski\my-backend\venv\Scripts\Activate.ps1
```

#### 3. AWS CLI Configuration
If AWS commands fail:
```powershell
# Verify configuration
aws configure list

# Reconfigure if needed
aws configure
```

#### 4. App Runner Build Failures
Check App Runner logs:
```powershell
aws apprunner describe-service --service-arn "your-service-arn"
```

### Getting Help

- AWS App Runner Documentation: https://docs.aws.amazon.com/apprunner/
- FastAPI Documentation: https://fastapi.tiangolo.com/
- GitHub Documentation: https://docs.github.com/

## Security Best Practices

1. **Never commit your .env file** - it contains sensitive information
2. **Use strong API keys** - generate random, complex keys
3. **Regularly rotate API keys** - update them periodically
4. **Monitor access logs** - check who's accessing your API
5. **Use HTTPS only** - App Runner provides SSL certificates automatically

## Cost Optimization

- App Runner charges based on usage
- Consider pausing or deleting the service when not in use
- Monitor your AWS billing dashboard regularly
- Set up billing alerts

## Next Steps

With your basic API deployed, you can:
1. Add more endpoints for your personal use
2. Integrate with Claude desktop client
3. Build a web frontend
4. Add database connectivity
5. Implement user authentication
6. Add monitoring and logging

Your API is now ready to serve as the foundation for your personal platform!