**AWS EC2 →GitHub → Jenkins → SonarQube → Docker → ML App → Prometheus → Grafana →**

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

Get password: docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword

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

<< First Add Credentials in Jenkins

Go to:

Manage Jenkins → Credentials → Global → Add Credentials

GitHub Credentials

Type: Username with Password

ID:

git

Username:

your_github_username

Password:

GitHub Personal Access Token
SonarQube Token

Type: Secret Text

ID:

sonar-token

Secret:

your_sonarqube_token  >>

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

**Monitoring Tools setup**

**1️⃣ Install Jenkins Prometheus Plugin**

In Jenkins

Go to:

Manage Jenkins
→ Plugins
→ Available Plugins
→ Search: Prometheus Metrics

Install:

Prometheus Metrics Plugin

After installation Jenkins exposes metrics at:

http://EC2-IP:8080/prometheus

Test it in browser.

You should see metrics like:

jenkins_job_build_duration_seconds
jenkins_executor_count
jvm_memory_bytes_used

2️⃣ Update Prometheus Configuration

Edit your prometheus.yml

global:
  scrape_interval: 15s

scrape_configs:

  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "node-exporter"
    static_configs:
      - targets: ["node-exporter:9100"]

  - job_name: "jenkins"
    metrics_path: /prometheus
    static_configs:
      - targets: ["jenkins:8080"]

Explanation:

Job	What it monitors
prometheus	Prometheus itself
node-exporter	EC2 system metrics
jenkins	Jenkins build metrics
3️⃣ Restart Prometheus

After saving config:

docker restart prometheus

Then open:

http://EC2-IP:9090/targets

You should see:

prometheus → UP
node-exporter → UP
jenkins → UP
4️⃣ Connect Grafana to Prometheus

Open Grafana

http://EC2-IP:3000

Login:

admin
admin

Add datasource:

Settings
→ Data Sources
→ Prometheus

URL:

http://prometheus:9090

Click:

Save & Test
5️⃣ Import Jenkins Dashboard

Import Jenkins monitoring dashboard.

In Grafana:

+ → Import

Use Dashboard ID:

9964

This shows:

Jenkins build status

Build duration

Executor usage

Queue size

6️⃣ Optional (Node Monitoring Dashboard)

For system metrics import:

1860

This dashboard shows:

CPU usage

RAM usage

Disk usage

Network traffic

Using Prometheus Node Exporter

7️⃣ Final Monitoring Architecture

Your setup will look like this:

Jenkins
   │
   │ /prometheus metrics
   ▼
Prometheus
   │
   ▼
Grafana Dashboards

And Node Exporter provides:

EC2 CPU / RAM / Disk metrics


