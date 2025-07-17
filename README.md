# 💬 DevOps Quote App

This is a simple web application that shows **motivational quotes** on the browser. It is built using **Python Flask**, and deployed using **Docker**, **Kubernetes**, and **Jenkins** with a full CI/CD pipeline.

---

## 🚀 Features

- Shows motivational quotes in random colors
- Web-based UI built with HTML + Bootstrap
- Dockerized Flask backend
- Kubernetes deployment with NodePort service
- Jenkins pipeline for CI/CD automation

---

## 🧰 Tech Stack

- **Frontend**: HTML + Bootstrap
- **Backend**: Python (Flask)
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: Jenkins
- **Code Repo**: GitHub
- **Image Repo**: DockerHub

---

## 📁 Project Structure

```
devops-quote-app/
│
├── backend/
│   └── app.py               # Flask application
│
├── Dockerfile               # Docker build file
├── docker-compose.yml       # Local Docker setup
├── Jenkinsfile              # Jenkins pipeline
└── k8s/
    ├── deployment.yml       # K8s deployment
    └── service.yml          # K8s service
```

---

## ▶️ How to Run Locally

### Step 1: Clone the Repo

```bash
git clone https://github.com/tanujsaini123/devops-quote-app.git
cd devops-quote-app
```

### Step 2: Run Using Docker Compose

```bash
docker-compose up --build
```

Then open: [http://localhost:5000](http://localhost:5000)

---

## ☸️ Deploy on Kubernetes

### Step 1: Build & Push Docker Image

```bash
docker build -t tanujkumar123/quote-app:latest .
docker push tanujkumar123/quote-app:latest
```

### Step 2: Apply K8s Configs

```bash
kubectl apply -f k8s/
kubectl rollout restart deployment quote-app
```

### Step 3: Access the App

```bash
http://<your-node-ip>:30007
```

---

## 🔄 Jenkins CI/CD Pipeline

The `Jenkinsfile` automates the following steps:

1. Clone source code from GitHub  
2. Build Docker image  
3. Push image to DockerHub  
4. Deploy to Kubernetes  
5. Restart deployment for update

---

## 👨‍💻 Author

**Tanuj Saini**  
🔗 [GitHub Profile](https://github.com/tanujsaini123)

---

## 📜 License

This project is for learning purpose and free to use.
