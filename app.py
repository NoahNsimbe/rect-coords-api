import logging
import os

from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import MethodNotAllowed, NotFound, BadRequest
from extract_rect_coords import extract_rect_coords_bp


def create_app(environment):
    application = Flask(__name__)
    application.config["ENV"] = environment

    CORS(application)

    application.register_blueprint(extract_rect_coords_bp)

    application.logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("app.log")
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    application.logger.addHandler(file_handler)

    return application


app = create_app(os.getenv("FLASK_ENV", "development"))


@app.errorhandler(Exception)
def handle_exception(error):
    app.logger.exception(error)
    return jsonify({"message": "Error occurred. Contact support"}), 500


@app.errorhandler(NotFound)
def handle_404_exception(error):
    app.logger.info(error)
    return jsonify({"message": "Requested Url not found on this microservice"}), 404


@app.errorhandler(BadRequest)
def handle_400_exception(error):
    app.logger.info(error)
    return jsonify({"message": error.description}), 400


@app.errorhandler(MethodNotAllowed)
def handle_405_exception(error):
    app.logger.info(error)
    return jsonify({"message": "Method not allowed for this endpoint."}), 405


if __name__ == "__main__":
    app.run()
