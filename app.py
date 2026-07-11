from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/time", methods=["GET"])
def time_now():
    return jsonify({"utc_time": datetime.now(timezone.utc).isoformat()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
