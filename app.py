from flask import Flask, render_template
from flask_smorest import Api
from api import NotesBlueprint

def create_app():
    app = Flask(__name__)
    app.config["API_TITLE"] = "Notes API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    @app.route("/")
    def index_page():
        return render_template("index.html")

    @app.route("/notes")
    def notes_page():
        return render_template("notes.html")

    api = Api(app)
    api.register_blueprint(NotesBlueprint)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
