from flask import Flask
from src.config.config import ConfigManager

HOST = ConfigManager.get_config("HOST")
PORT = ConfigManager.get_config("PORT")

flask_app = Flask(__name__)


def start_server():
    flask_app.run(host=HOST, port=PORT, debug=True)


if __name__ == "__main__":
    start_server()
