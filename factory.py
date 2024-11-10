import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_redis import FlaskRedis

load_dotenv()

db = SQLAlchemy()
redis_client = FlaskRedis()

def create_app():
    app = Flask(__name__)
    from src.models.mysql.entities.products import Product
    
    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    app.config['REDIS_URL'] = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    redis_client.init_app(app)

    db.init_app(app)
    migrate = Migrate(app, db)
    
    
    from src.routes.products_routes import products_routes_bp
    blueprints = [
        products_routes_bp
    ]
    
    for i in blueprints:
        app.register_blueprint(i)
    

    return app
