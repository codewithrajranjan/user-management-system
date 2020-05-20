from flask import Flask, jsonify
from src.config.config import ConfigManager

HOST = ConfigManager.get_config("HOST")
PORT = ConfigManager.get_config("PORT")

flask_app = Flask(__name__)


@flask_app.errorhandler(Exception)
def global_error_handler(e):
    data_to_return = {
        "status": "error",
        "message": e.get_message()}

    return jsonify(data_to_return), e.get_code()


from src.api.PermissionApi import *


def start_server():
    flask_app.run(host=HOST, port=PORT, debug=True)


if __name__ == "__main__":
    start_server()
