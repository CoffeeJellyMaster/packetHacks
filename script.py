from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/data", methods=["POST"])
def receive_data():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    data = request.get_json() or {}
    return jsonify({"received": data}), 200

@app.route("/wake", methods=["GET"])
def wake_up():
    return jsonify({"message": "Server is awake"}), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT env var
    app.run(host="0.0.0.0", port=port)
