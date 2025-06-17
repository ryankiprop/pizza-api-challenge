
#Pizza Restaurant API
A lightweight Flask REST API for managing pizza restaurants and their menus. Built with Python, Flask, and SQLAlchemy.

 ##Features
RESTful endpoints for restaurants & pizzas

SQLite database with Flask-Migrate

Input validation

Ready-to-use Postman collection

 Setup
```bash
# Clone repository
git clone https://github.com/yourusername/pizza-api.git
cd pizza-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
 Configuration
Rename .env.example to .env

Configure your database URL:

ini
DATABASE_URL=sqlite:///pizza.db
 Running the API
bash
# Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Start server
flask run
API will be available at http://localhost:5000

 API Endpoints
Method	Endpoint	Description
GET	/restaurants	List all restaurants
GET	/restaurants/<id>	Get restaurant details
DELETE	/restaurants/<id>	Delete a restaurant
GET	/pizzas	List all pizza types
POST	/restaurant_pizzas	Create pizza-restaurant link
 Testing
 ```bash
Import pizza_api.postman_collection.json into Postman.

Example request:

```bash
curl -X POST http://localhost:5000/restaurant_pizzas \
  -H "Content-Type: application/json" \
  -d '{"price":10,"pizza_id":1,"restaurant_id":1}'