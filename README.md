# ML Inference Service – Production-Ready MLOps Project

This project demonstrates a production-ready machine learning inference service built with FastAPI, containerized using Docker, tested with pytest, and deployed automatically to AWS EC2 using GitHub Actions CI/CD.
It also includes Kubernetes manifests for scalable deployment.

---

## What this project intends to show

* How to serve an ML model via a clean REST API
* How to test ML logic and APIs properly
* How to containerize an ML service
* How to build a full **CI/CD pipeline**
* How to deploy automatically on **AWS**
* How the same service can be deployed on **Kubernetes**

---

## High-level architecture

```
Client
  |
  | HTTP (JSON)
  v
FastAPI Application
  |
  | NumPy input → ML model
  v
RandomForest Model (scikit-learn)
  |
  v
Prediction Response
```

---

## CI/CD & Deployment architecture

```
GitHub (push / Pull Request)
   |
   v
GitHub Actions (CI/CD)
   |  - install dependencies
   |  - run pytest
   |  - build Docker image
   |  - push image to ECR
   v
AWS Elastic Container Registry (ECR)
   |
   v
EC2 Instance (Docker)
   |  - pull latest image
   |  - stop old container
   |  - run new container
   v
Public ML Inference API
```

---

## Tech stack

* **Python 3.11**
* **FastAPI** – API layer
* **scikit-learn** – ML model
* **pytest** – testing
* **Docker** – containerization
* **GitHub Actions** – CI/CD
* **AWS ECR + EC2** – deployment
* **Kubernetes (YAML)** – scalable deployment option

---

## Project structure

```
ml-inference-service/
│
├── app/                 # Application code
│   ├── main.py          # FastAPI endpoints
│   ├── model.py         # Model loading & inference
│   └── schema.py        # Request/response schemas
│
├── model/
│   └── model.pkl        # Trained ML model
│
├── train/
│   └── train_model.py   # Training script
│
├── tests/               # Unit & API tests
│   ├── test_model.py
│   └── test_api.py
│
├── Dockerfile
├── requirements.txt
│
├── deployment.yaml      # Kubernetes Deployment
├── service.yaml         # Kubernetes Service
│
└── .github/workflows/
    └── ci-cd.yml        # CI/CD pipeline
```

---

## Machine learning model

* **Dataset**: Iris
* **Algorithm**: Random Forest Classifier
* **Input**: 4 numerical features
* **Output**: Class index (0, 1, or 2)

The model is trained once and serialized using `joblib`. Inference loads the model at startup for low-latency predictions.

---

## API design

### Health check

```
GET /health
```

Used for monitoring and deployment validation.

Response:

```json
{ "status": "ok" }
```

---

### Prediction endpoint

```
POST /predict
```

Request:

```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

Response:

```json
{
  "prediction": 0
}
```

Input validation is enforced using **Pydantic**, and invalid requests return proper HTTP errors.

---

## Testing strategy

Tests are executed automatically in CI and include:

* Model-level validation
* API response validation
* Error handling for invalid input

This ensures that **only tested code is deployed**.

Run locally:

```bash
pytest -v
```

---

## Docker & containerization

The application is fully containerized.

```bash
docker build -t ml-inference-service .
docker run -p 8000:8000 ml-inference-service
```

FastAPI runs on port 8000 inside the container.

---

## CI/CD pipeline 

On every push or pull request to `main`:

1. Install dependencies
2. Run automated tests
3. Build Docker image
4. Push image to AWS ECR
5. SSH into EC2
6. Pull latest image
7. Restart the service

Deployment is **fully automated** and reproducible.

---

## Kubernetes support

Kubernetes manifests are included to demonstrate how the same service can be deployed in a cluster.

* Deployment manages pods
* Service exposes the application via LoadBalancer

This shows readiness for **scaling beyond single EC2 instances**.

---

## Security practices

* No secrets committed to the repository
* AWS credentials and SSH keys stored in GitHub Secrets
* Private keys handled only at runtime

---


