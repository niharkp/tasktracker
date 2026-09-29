# TaskTracker

![CI/CD](https://github.com/niharkp/tasktracker/actions/workflows/cii.yml/badge.svg)


# TaskTracker

A simple Flask-based task tracking application containerized with Docker and automated using GitHub Actions CI/CD.

## 🚀 Features

- Flask web application
- Docker containerization
- Multi-stage Docker build
- Non-root Docker user
- Docker health check
- Automated testing with Pytest
- GitHub Actions CI/CD
- Automatic Docker image build
- Automatic Docker Hub deployment

## 🛠️ Tech Stack

- Python
- Flask
- Pytest
- Docker
- GitHub Actions
- Docker Hub

## 🐳 Run with Docker

```bash
docker pull nihar6362/tasktracker:latest
docker run -p 5000:5000 nihar6362/tasktracker:latest
