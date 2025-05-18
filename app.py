from flask import Flask, send_from_directory
from api.knowledge_base_api import kb_bp
from api.state_machine import state_bp
from api.post_call_log import log_bp  # optional

app = Flask(__name__)

app.register_blueprint(kb_bp)
app.register_blueprint(state_bp)
app.register_blueprint(log_bp)  # optional

@app.route("/")
def index():
    # Serve index.html from frontend folder
    return send_from_directory('frontend', 'index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
