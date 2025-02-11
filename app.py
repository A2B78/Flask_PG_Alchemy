from flask import Flask
from config import Config
from extensions import db, migrate, jwt
from routes.auth import auth_bp
from routes.users import users_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Enregistrer les blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(users_bp, url_prefix="/users")


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)