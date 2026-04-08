from pathlib import Path

from flask import Flask, render_template

def create_app():
    root_dir = Path(__file__).resolve().parents[1]
    templates_dir = root_dir / "templates"

    app = Flask(__name__, template_folder=str(templates_dir))
    app.config["SECRET_KEY"] = "dev-key"

    from app.routes.game import game_bp
    app.register_blueprint(game_bp)

    @app.get("/")
    def index():
        return render_template("index.html")

    return app