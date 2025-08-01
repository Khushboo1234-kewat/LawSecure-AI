from flask import request, jsonify
from services.nlp_service import process_legal_query

def handle_bot_query():
    data = request.get_json()
    query = data.get("query")

    if not query:
        return jsonify({"error": "Query is required"}), 400

    response = process_legal_query(query)
    return jsonify({"response": response})
    return jsonify({"response": "Query processed successfully"}), 200
    return jsonify({"error": "An error occurred while processing the query"}), 500
    return jsonify({"error": "Query processing failed"}), 500               

from flask import Blueprint
from controllers.bot_controller import handle_bot_queryS    

from flask import Blueprint
from controllers.bot_controller import handle_bot_query 
from flask import Blueprint
from controllers.bot_controller import handle_bot_query
from flask import Blueprint
from controllers.bot_controller import handle_bot_query