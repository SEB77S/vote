from flask import Blueprint, request, jsonify

user_bp = Blueprint('user_bp', __name__)

# Simulación de almacenamiento en memoria
users = []

@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()

    required = ["username", "email", "password"]
    missing = [field for field in required if field not in data]

    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    user = {
        "username": data["username"],
        "email": data["email"],
        "password": data["password"]
    }

    users.append(user)

    return jsonify({"message": "User created successfully", "user": user}), 201

@user_bp.route("/", methods=["GET"])
def get_users():
    return jsonify(users), 200