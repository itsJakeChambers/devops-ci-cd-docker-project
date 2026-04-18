# 🚀 DevOps CI/CD Docker Project

End-to-end DevOps project demonstrating containerization, automated deployment, and cloud infrastructure.

---

## 📌 Project Overview

This project showcases a complete DevOps workflow:

* Build a simple API
* Containerize the application using Docker
* Automate deployment with CI/CD (GitHub Actions)
* Deploy to a cloud server (VPS)
* Ensure reliability and scalability

The goal is to demonstrate real-world DevOps practices.

---

## 🛠️ Tech Stack

* **Backend**: Python (FastAPI)
* **Containerization**: Docker, Docker Compose
* **CI/CD**: GitHub Actions
* **Database**: PostgreSQL
* **Infrastructure**: VPS (Linux)

---

## 📁 Project Structure

```
.
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .github/workflows/
└── README.md
```

---

## ⚙️ Features

* REST API with FastAPI
* Dockerized application
* Multi-container setup (API + Database)
* Automated CI/CD pipeline
* Deployment on a remote server
* Scalable and reproducible environment

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/itsJakeChambers/devops-ci-cd-docker-project.git
cd devops-ci-cd-docker-project
```

---

### 2. Run locally with Docker

```bash
docker-compose up --build
```

---

### 3. Access the API

```
http://localhost:8000
```

---

## 🔄 CI/CD Pipeline

The project includes a GitHub Actions pipeline that:

* Builds the Docker image
* Runs basic checks
* Deploys the application to a remote server

---

## ☁️ Deployment

The application is deployed on a VPS using Docker.

Key steps:

* SSH connection to server
* Pull latest changes
* Restart containers

---

## 📊 API Endpoints

* `/` → Docs
* `/lieux` → City

---

## 🎯 Goals of the Project

* Demonstrate DevOps fundamentals
* Show real deployment workflow
* Practice automation and infrastructure management

---

## 📌 Future Improvements

* Add monitoring (Prometheus / Grafana)
* Add HTTPS with reverse proxy (NGINX)
* Improve scalability with Kubernetes

---

## 👤 Author

Project created as part of a DevOps learning journey.
