# backend/config.py

import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///legalbot.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "your_jwt_secret_key")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", 3600))  # 1 hour
    JWT_REFRESH_TOKEN_EXPIRES = int(os.environ.get("JWT_REFRESH_TOKEN_EXPIRES   ", 86400))  # 24 hours      
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER", "uploads/")
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}    
    MAX_CONTENT_LENGTH = int(os.environ.get("MAX_CONTENT_LENGTH", 16 * 1024 * 1024))  # 16 MB   
    
    @staticmethod
    def init_app(app):
        pass    
    
# Example of how to use the Config class
if __name__ == "__main__":
    config = Config()
    print("Secret Key:", config.SECRET_KEY)
    print("Database URI:", config.SQLALCHEMY_DATABASE_URI)
    print("JWT Access Token Expires In:", config.JWT_ACCESS_TOKEN_EXPIRES, "seconds")
    print("Upload Folder:", config.UPLOAD_FOLDER)
    print("Allowed Extensions:", config.ALLOWED_EXTENSIONS)
    print("Max Content Length:", config.MAX_CONTENT_LENGTH, "bytes")
    print("JWT Refresh Token Expires In:", config.JWT_REFRESH_TOKEN_EXPIRES, "seconds")
    print("JWT Secret Key:", config.JWT_SECRET_KEY)
    print("SQLAlchemy Track Modifications:", config.SQLALCHEMY_TRACK_MODIFICATIONS)
    print("Configuration initialized successfully.")