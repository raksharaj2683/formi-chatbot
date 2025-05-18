from flask import Blueprint, request
import os, csv

log_bp = Blueprint("log", __name__)
log_file = "post_call_analysis.csv"

@log_bp.route("/api/log", methods=["POST"])
def log_interaction():
    data = request.json
    file_exists = os.path.exists(log_file)

    with open(log_file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

    return {"status": "success", "message": "Logged"}
