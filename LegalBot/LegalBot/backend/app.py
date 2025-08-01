# backend/app.py

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from backend.config import Config

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)

    # Init DB and JWT
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from backend.routes.auth_routes import auth_bp
    from backend.routes.bot_routes import bot_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(bot_bp, url_prefix="/api/bot")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
