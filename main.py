from flask import Flask
from services.user_service import user_bp

def create_app():
    app = Flask(__name__)
    
    # Registrar blueprints
    app.register_blueprint(user_bp, url_prefix="/api/users")
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)