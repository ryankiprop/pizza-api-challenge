from server import create_app, db
from server.controllers.restaurant_controller import restaurant_bp
from server.controllers.pizza_controller import pizza_bp
from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp

app = create_app()

# Register blueprints
app.register_blueprint(restaurant_bp, url_prefix='/api')
app.register_blueprint(pizza_bp, url_prefix='/api')
app.register_blueprint(restaurant_pizza_bp, url_prefix='/api')

@app.route('/')
def home():
    return {'message': 'Pizza Restaurant API'}

if __name__ == '__main__':
    app.run(port=5555, debug=True)