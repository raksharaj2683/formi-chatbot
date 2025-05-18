from flask import Blueprint, request, jsonify
import os, json

kb_bp = Blueprint('kb', __name__)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
KB_DIR = os.path.join(BASE_DIR, "knowledge_base_json")

@kb_bp.route("/api/knowledge-base", methods=["GET"])
def get_kb():
    location = request.args.get("location", "").lower()
    filepath = os.path.join(KB_DIR, f"{location}.json")

    if not os.path.exists(filepath):
        return jsonify({"status": "error", "message": f"'{location}' not found"}), 404

    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    return jsonify({"status": "success", "data": data})
