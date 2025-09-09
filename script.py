# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/data", methods=["POST"])
# def receive_data():
#     print(f"[DEBUG] Received POST /data with: {request.get_json()}")
#     if not request.is_json:
#         return jsonify({"error": "Request must be JSON"}), 400
#     data = request.get_json() or {}
#     return jsonify({"received": data}), 200

# @app.route("/wake", methods=["GET"])
# def wake_up():
#     print("[DEBUG] GET /wake called")
#     return jsonify({"message": "Server is awake"}), 200

# @app.route("/", methods=["GET"])
# def root():
#     return jsonify({"status": "ok"}), 200

# if __name__ == "__main__":
#     import os
#     port = int(os.environ.get("PORT", 5000))
#     print(f"[DEBUG] Starting Flask app on port {port}")
#     app.run(host="0.0.0.0", port=port)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the last received data temporarily in memory
_last_received_data = None

@app.route("/data", methods=["POST"])
def receive_data():
    global _last_received_data
    print(f"[DEBUG] Received POST /data with: {request.get_json()}")
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    data = request.get_json() or {}
    _last_received_data = data  # Store latest data
    return jsonify({"received": data}), 200

@app.route("/fetch", methods=["GET"])
def fetch_data():
    """
    New endpoint: Return the last received data from /data.
    If no data was posted yet, return empty payload.
    """
    if _last_received_data:
        print(f"[DEBUG] GET /fetch returning last received data: {_last_received_data}")
        return jsonify({"latest": _last_received_data}), 200
    else:
        print("[DEBUG] GET /fetch called but no data available")
        return jsonify({"latest": None, "message": "No data received yet"}), 200

@app.route("/wake", methods=["GET"])
def wake_up():
    print("[DEBUG] GET /wake called")
    return jsonify({"message": "Server is awake"}), 200

@app.route("/", methods=["GET"])
def root():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    print(f"[DEBUG] Starting Flask app on port {port}")
    app.run(host="0.0.0.0", port=port)
