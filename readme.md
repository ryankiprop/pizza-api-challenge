#Pizza Restaurant API

A complete REST API for pizza restaurant management with Flask and SQLAlchemy.

##Quick Start

```bash
# 1. Clone repo
git clone https://github.com/ryankiprop/pizza-api-challenge.git
cd pizza-api

# 2. Run in virtual environment
pipenv shell

# 3. Install dependencies
pipenv install flask
pipenv install flask-migrate
pipenv install flask-sqlalchemy

# 4. Environment variables
export FLASK_APP=app.py

#Launching the API
#Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

#Run development server
flask run



