# Pizza Restaurant API

A Flask REST API for managing pizza restaurants and their menus.

## Features
- RESTful endpoints for restaurants & pizzas  
- SQLite database with Flask-Migrate  
- Input validation  
- Ready-to-use Postman collection  

## Setup
```bash
# Clone repo
git clone https://github.com/ryankiprop/pizza-api-challenge.git
cd pizza-api

# Create virtual env
pipenv install
pipenv shell

# Set environment variables
export FLASK_APP=server.app

# Install packages
pipenv install flask
pipenv install flask-migrate
pipenv install flask-sqlalchemy

# Set your database URL
DATABASE_URL=sqlite:///pizza.db

# Initialize DB
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Start server
flask run
