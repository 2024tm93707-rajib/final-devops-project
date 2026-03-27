# ACEest Fitness DevOps Pipeline

This project demonstrates a DevOps pipeline for the ACEest Fitness application.

## Technologies

- Python Flask
- Docker
- GitHub Actions
- Jenkins
- Pytest

## Run Locally

pip install -r requirements.txt
python app/app.py

## Run Tests

pytest

## Docker

docker build -t aceest-fitness .
docker run -p 5000:5000 aceest-fitness

## CI/CD Pipeline

GitHub Actions automatically runs:

1. Build
2. Lint validation
3. Unit tests
4. Docker image creation

## Jenkins

Jenkins performs a secondary build validation by:

- Pulling the repository
- Installing dependencies
- Running Pytest
- Building Docker container
