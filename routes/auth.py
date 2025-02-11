from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, get_jti, get_jwt
from models import User, UserSession, db
from datetime import datetime, timedelta
import json
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    if not email:
        return jsonify({"message": "Email est requis"}), 400

    user = User(
        username=data["username"],
        email=email,
        password_hash=generate_password_hash(data["password"]),
        role=data.get("role", "user")
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Utilisateur créé avec succès"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.check_password(data["password"]):
        identity = json.dumps({"id": user.id, "role": user.role})
        access_token = create_access_token(identity=identity)
        refresh_token = create_refresh_token(identity=identity)
        
        session = UserSession(user_id=user.id, jti=get_jti(refresh_token), expires_at=datetime.utcnow() + timedelta(days=7))
        db.session.add(session)
        db.session.commit()
        
        return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200
    return jsonify({"message": "Identifiants invalides"}), 401


@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    current_user = json.loads(get_jwt_identity())
    identity = json.dumps({"id": current_user["id"], "role": current_user["role"]})
    access_token = create_access_token(identity=identity)
    return jsonify({"access_token": access_token}), 200

@auth_bp.route("/whoami", methods=["GET"])
@jwt_required()
def whoami():
    current_user = json.loads(get_jwt_identity())
    if current_user["role"] == "admin":
        return jsonify({"id": current_user["id"]}), 200
    return jsonify({"id": current_user["id"], "role": current_user["role"]}), 200