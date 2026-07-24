# Django Playground

A modular Django application that explores common backend development patterns through multiple independent features. The project combines session-based authentication, RESTful APIs, database-driven applications, and containerized development into a single codebase.

## Features

* User authentication and session management
* REST API built with Django REST Framework
* Todo management service
* Interactive click-tracking application
* PostgreSQL database integration
* Docker Compose development environment
* Modular Django application structure

## Technical Overview

The project demonstrates the implementation of backend services using Django and Django REST Framework. It focuses on data modeling, ORM-based database access, request serialization, authentication, and API design while following Django's application architecture.

The repository also serves as a practical reference for common Django development workflows, including migrations, containerized deployment, and application organization.

## To reproduce project
python3 -m pip install -r requirements.txt
docker compose up -d
python manage.py migrate
python manage.py runserver
full docker image would be added
