# ACEest Fitness DevOps Project

## Overview
This project demonstrates a complete DevOps CI/CD pipeline using Flask, Docker, GitHub Actions, and Jenkins.

## Features
- BMI Calculation API
- Unit Testing with Pytest
- Dockerized Application
- CI/CD Pipeline using GitHub Actions
- Jenkins Build Integration

## Run Locally
pip install -r requirements.txt
python app/app.py

## Run Tests
pytest

## Docker
docker build -t aceest-fitness .
docker run -p 5000:5000 aceest-fitness

## CI/CD
Pipeline runs on:
- Push
- Pull Request

Stages:
- Build
- Lint
- Test
- Docker Build

## Jenkins
- Clone Repo
- Install Dependencies
- Run Tests
- Build Docker Image

FINAL SUBMISSION STEPS
git init
git add .
git commit -m "Final DevOps Assignment Submission"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/aceest-devops-project.git
git push -u origin main
