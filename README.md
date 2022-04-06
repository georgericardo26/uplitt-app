# Uplitt App
![](https://uplitt-app.s3.amazonaws.com/screen.jpeg "Screen")


Uplitt app is an application for restaurant which consists in the dashboard for sellers and backend api.

Tools
------------
- Python
- Django
- Django Rest Framework
- DRF_yasg
- Open API Documentation
- Oauth2 Authentication
- PostgreSQL
- Docker
- Docker-compose
- gitlab-ci (Pipeline)
- RDS (AWS)
- EC2 (AWS)
- Javascript
- ReactJS
- UWSGI

Dependencies
------------
- Python 3.6+
- Django 1.11+
- For the Server, Django REST Framework 3.7+ is required.
- For the Client, we use react 17.0.1.
- For run the server application, it's need have docker installed

Setup Server
------------
First you have to do a download of the docker image:

    `git clone https://gitlab.com/uplitt/uplitt-app`

Make sure you already has docker and docker-compose installed.

 `sudo apt  install docker.io`
 
  `sudo apt install docker-compose`


After, you will init the container service:

    `sudo docker-compose up`
 
