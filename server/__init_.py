from .extensions import db, migrate

def create_app():
    from flask import Flask
    from .config import Config
    
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    return app