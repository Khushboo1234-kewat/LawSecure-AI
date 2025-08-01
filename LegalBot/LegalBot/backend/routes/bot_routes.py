# backend/routes/bot_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from backend.controllers.bot_controller import get_legal_response

bot_bp = Blueprint("bot", __name__)

@bot_bp.route("/ask", methods=["POST"])
@jwt_required()
def ask_bot():
    data = request.get_json()
    question = data.get("question", "")
    response = get_legal_response(question)
    return jsonify({"answer": response})
