# Platform CI/CD System

A production-style CI/CD pipeline demonstrating artifact promotion, environment-based deployments, and deployment safety controls.

---

## Overview

This project simulates a platform engineering CI/CD system with:

- Multi-stage pipeline (test → build → deploy)
- Artifact promotion using immutable image tags
- Environment-based deployments (dev → production)
- Manual approval gates for production releases
- Rollback simulation on deployment failure

---

## Architecture

Pipeline flow:

1. **Test**
   - Runs automated tests using pytest

2. **Build**
   - Builds Docker image
   - Tags image using commit SHA
   - Creates `latest` and short SHA aliases

3. **Deploy (Dev)**
   - Deploys the built image to development environment

4. **Deploy (Production)**
   - Requires manual approval
   - Deploys the same image promoted from dev

5. **Rollback**
   - Simulates rollback on production failure

---

## Key Concepts Demonstrated

### Artifact Promotion
Build once, deploy the same artifact across environments.

### Deployment Safety
Manual approval gates prevent unsafe production releases.

### Traceability
Each deployment is tied to a specific commit SHA.

### Failure Handling
Rollback strategy simulated for production failures.

---

## Tech Stack

- Python (FastAPI)
- Docker
- GitHub Actions

---

## Running Locally

```bash
# create virtual environment
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run service
uvicorn app.main:app --reload

# run tests
PYTHONPATH=. pytest -v
