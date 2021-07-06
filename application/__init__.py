from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    with app.app_context():
        from .views import views

        # REGISTER ROUTES
        app.register_blueprint(views)

        return app
