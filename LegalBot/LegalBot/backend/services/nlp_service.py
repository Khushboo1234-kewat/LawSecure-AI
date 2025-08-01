from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import User
from models import db
from utils.jwt_helper import create_token

def register_user(username, email, password):
    # Check if user already exists
    existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
    if existing_user:
        return {'error': 'Username or email already exists'}, 409

    # Hash password
    hashed_password = generate_password_hash(password)

    # Create and save user
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return {'message': 'User registered successfully'}, 201

def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return {'error': 'Invalid email or password'}, 401

    # Create JWT token
    token = create_token(user.id)
    return {'token': token, 'username': user.username}, 200
