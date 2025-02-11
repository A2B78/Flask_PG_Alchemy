from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, db
import json

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["GET"])
@jwt_required()
def list_users():
    current_user = json.loads(get_jwt_identity())
    if current_user["role"] != "admin":
        return jsonify({"message": "Accès refusé"}), 403

    users = User.query.all()
    return jsonify([{ "id": user.id, "username": user.username, "role": user.role , "email": user.email} for user in users])

@users_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    current_user = json.loads(get_jwt_identity())
    if current_user["role"] != "admin":
        return jsonify(data.get("username")), 200
    user = User.query.get_or_404(user_id)
    data = {
        "id": user.id,
        "username": user.username,
        "role": user.role
    }
    return jsonify(data), 200

@users_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    current_user = json.loads(get_jwt_identity())
    if current_user["role"] != "admin":
        return jsonify({"message": "Accès refusé"}), 403
    
    user = User.query.get_or_404(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    data = request.get_json()
    if "username" in data:
        user.username = data["username"]
    if "password" in data:
        user.password = data["password"]
    if "email" in data:
        user.email = data["email"]
    if "role" in data:
        user.role = data["role"]
    db.session.commit()
    return jsonify({"msg": "User updated"}), 200
