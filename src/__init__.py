from flask import Flask
import os

# Creacion de la app , dependiento de los ambientes
def create_app(test_config=None):

# Con el argumento instance_relative_config decimos a la app que podemos tener alguna configuraciones adicionales en algunos archivos de la app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:

        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY")
        )

    else:
        app.config.from_mapping(test_config)


    @app.get("/")
    def index():
        return "Hello World"

    @app.get("/hello")
    def say_hello():
        return {"message": "Hello World"}

    return app