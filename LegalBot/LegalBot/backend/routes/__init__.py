# backend/routes/__init__.py

from .auth_routes import auth_bp
from .bot_routes import bot_bp

# This function is imported and used in app.py to register routes
def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(bot_bp, url_prefix="/api/bot")
