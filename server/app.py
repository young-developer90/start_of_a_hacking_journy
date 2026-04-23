from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for user credentials (for demonstration purposes)
# In a real application, you'd use a database.
users = {
    "testuser": "password123",
    "admin": "adminpass"
}

@app.route("/")
def main():
    return "Server is running...."

@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"message": "Request must be JSON"}), 400

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    # Basic credential verification
    if username in users and users[username] == password:
        response_data = {
            "message": "Login successful!",
            "username": username,
            "token": "dummy_jwt_token" # In a real app, generate a proper token
        }
        return jsonify(response_data), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401 # 401 Unauthorized

if __name__ == "__main__":
    # It's generally recommended to use a more robust server like Gunicorn for production.
    # For local development, Flask's built-in server is fine.
    app.run('0.0.0.0', 5050, debug=True)
