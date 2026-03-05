# Healthcare Patient Management System (Dockerized)

## Project Overview

This project is a simple **Healthcare Patient Management System** built using **Python Flask** and containerized using **Docker**.
The goal of the project is to demonstrate basic **DevOps practices** like containerization, version control, and CI/CD automation.

The application allows users to:

* Add patient information
* View patient records
* Run the application inside Docker containers
* Automatically build Docker images using CI/CD

---

## Technologies Used

* Python
* Flask
* Docker
* Docker Compose
* Git
* GitHub
* GitHub Actions (CI/CD)

---

## Project Structure

```
Healthcare-Docker-Project
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── templates
│   ├── index.html
│   ├── add_patient.html
│   └── patients.html
│
└── static
```

---

## Application Features

* Add new patient details
* View all patient records
* Simple web interface
* Containerized using Docker

---

## Docker Implementation

The application is containerized using **Docker** to ensure consistent environments across development and deployment.

Steps included:

1. Create Dockerfile
2. Build Docker Image
3. Run Docker Container
4. Use Docker Compose to manage services

Build Docker Image:

```
docker build -t healthcare-app .
```

Run Docker Container:

```
docker run -p 5000:5000 healthcare-app
```

Run using Docker Compose:

```
docker-compose up
```

Access application at:

```
http://localhost:5000
```

---

## CI/CD Pipeline

CI pipeline is implemented using **GitHub Actions**.

Whenever code is pushed to the repository:

1. GitHub Actions workflow is triggered
2. Docker image is built automatically
3. Build status is shown in the Actions tab

Workflow file location:

```
.github/workflows/docker-build.yml
```

---

## DevOps Workflow

Developer pushes code → GitHub Repository → GitHub Actions → Docker Image Build

This ensures that every code change is automatically tested for Docker build compatibility.

---

## Conclusion

This project demonstrates the integration of **Flask application development with DevOps practices like Docker containerization and CI/CD automation using GitHub Actions.**
