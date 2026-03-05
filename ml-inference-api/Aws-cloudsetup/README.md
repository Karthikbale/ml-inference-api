GitHub → Jenkins → SonarQube → Docker → ML App → Prometheus → Grafana → AWS EC2

1️⃣ Launch AWS EC2 Ubuntu Server

Go to AWS EC2

Create instance:

AMI: Ubuntu 22.04

Instance type: t2.medium (recommended for Jenkins + SonarQube)

Storage: 20 GB

Security group ports:

Open these ports:

Port	Purpose
22	SSH
8080	Jenkins
9000	SonarQube
8000	ML App
9090	Prometheus
3000	Grafana

Connect:

ssh -i key.pem ubuntu@EC2_PUBLIC_IP
2️⃣ Update Server
sudo apt update && sudo apt upgrade -y
3️⃣ Install Docker
sudo apt install docker.io -y

Start docker

sudo systemctl enable docker
sudo systemctl start docker

Allow ubuntu user

sudo usermod -aG docker ubuntu

Reconnect SSH.

Check:

docker --version
4️⃣ Install Docker Compose
sudo apt install docker-compose -y

Check:

docker-compose --version
5️⃣ Install Git
sudo apt install git -y
6️⃣ Create Project Directory
mkdir devops-project
cd devops-project
7️⃣ Create Docker Compose for Jenkins + SonarQube
nano docker-compose.yml

Paste:

version: '3'

services:

  jenkins:
    image: jenkins/jenkins:lts
    container_name: jenkins
    user: root
    ports:
      - "8080:8080"
    volumes:
      - jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    restart: always

  sonarqube:
    image: sonarqube:lts-community
    container_name: sonarqube
    ports:
      - "9000:9000"
    environment:
      - SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true
    volumes:
      - sonarqube_data:/opt/sonarqube/data
    restart: always

volumes:
  jenkins_home:
  sonarqube_data:

Run:

docker-compose up -d

Check:

docker ps
8️⃣ Access Jenkins

Open browser:

http://EC2_IP:8080

Get password:

docker logs jenkins

Install Suggested Plugins.

9️⃣ Install Jenkins Plugins

Go to:

Manage Jenkins → Plugins

Install:

Docker Pipeline

Git

SonarQube Scanner

Pipeline

Credentials Binding

🔟 Setup SonarQube

Open:

http://EC2_IP:9000

Login:

admin
admin

Create token

1️⃣1️⃣ Configure SonarQube in Jenkins

Jenkins → Manage Jenkins → System

Add SonarQube server:

Name:

Sonar

URL:

http://sonarqube:9000

Token credential.

1️⃣2️⃣ Install Sonar Scanner

Jenkins → Manage Jenkins → Tools

Add:

SonarScanner
1️⃣3️⃣ Create Jenkins Pipeline

Create pipeline.

Add your GitHub repo:

https://github.com/Karthikbale/ml-inference-api.git

Use Pipeline Script from SCM

1️⃣4️⃣ Pipeline Flow

Your pipeline will run:

GitHub
   ↓
Jenkins
   ↓
SonarQube Code Analysis
   ↓
Docker Image Build
   ↓
Run Container
   ↓
Expose ML API
1️⃣5️⃣ Access ML API

After pipeline success:

http://EC2_IP:8000/docs

Swagger UI will appear.
