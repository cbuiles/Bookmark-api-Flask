from flask import Flask
import os
from src.auth import auth
#from src.bookmarks import bookmarks
from src.database import db
from flask_jwt_extended import JWTManager

# Creacion de la app , dependiento de los ambientes
def create_app(test_config=None):

# Con el argumento instance_relative_config decimos a la app que podemos tener alguna configuraciones adicionales en algunos archivos de la app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:

        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY')
        )

    else:
        app.config.from_mapping(test_config)

    db.app=app
    db.init_app(app)

    JWTManager(app)


    app.register_blueprint(auth)
    #app.register_blueprint(bookmarks)

    return app