
# 🚀 DevOps Quote App

This project is a **Motivational Quote Web App** built with **Flask**, Dockerized, and deployed on **Kubernetes** with a full **CI/CD pipeline** using Jenkins.

---

## 🌐 Project Structure

```
devops-quote-app/
├── backend/
│   └── app.py               # Flask App
├── Dockerfile               # Container build
├── docker-compose.yml       # For local testing
├── Jenkinsfile              # CI/CD pipeline
├── k8s/
│   ├── deployment.yml       # K8s Deployment
│   └── service.yml          # K8s Service (NodePort)
```

---

## 💡 Features

- Displays multiple motivational quotes in the browser
- Random background color for each quote
- Dockerized Flask application
- CI/CD pipeline with Jenkins:
  - Git clone
  - Docker build & push to DockerHub
  - Kubernetes deployment
  - Rollout restart for updates

---

## 🧪 Local Testing with Docker Compose

```bash
docker-compose up --build
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 🛠️ Jenkins CI/CD Pipeline

Make sure your Jenkins instance has:

- Docker installed & running
- Kubernetes CLI (`kubectl`) configured
- DockerHub credentials stored with ID: `dockerHubcreds`

### ✅ Pipeline Stages

1. Clone repo
2. Build Docker image
3. Push image to DockerHub
4. Deploy to Kubernetes
5. Rollout restart deployment

---

## ☸️ Kubernetes Deployment

To deploy manually:

```bash
kubectl apply -f k8s/
kubectl rollout restart deployment quote-app
kubectl get pods
```

⛳ To access the app via NodePort:

```bash
kubectl port-forward service/quote-service 5000:5000
```

Then open [http://localhost:5000](http://localhost:5000)

---

## 📦 DockerHub

Image is pushed to: `tanujkumar123/quote-app:latest`

---

## ✨ Author

- Tanuj Saini
- GitHub: [@tanujsaini123](https://github.com/tanujsaini123)

---

## 📎 License

This project is open-source and available under the [MIT License](LICENSE).
