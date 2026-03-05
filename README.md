**ML Inference API – Dockerized Deployment**

**📌 Project Overview**

This project demonstrates how to train a Machine Learning model and deploy it as a REST API using FastAPI and Docker.
The model is trained on the Iris dataset and exposed through a /predict endpoint for real-time inference.
The application is containerized using Docker and can be deployed on aws cloud environment.

**🧠 Problem Statement**

Deploy a trained ML model as a production-ready API that:

Accepts input features via HTTP request

Returns prediction output

Runs inside a Docker container

Is portable and cloud-ready

**🏗 Architecture**
Model Training → FastAPI Application → Docker Container → API Testing
