from flask_socketio import SocketIO, emit
from flask import session
from application import create_app
from config import Config

app = create_app()
io = SocketIO(app)


@io.on("sendMessage")
def send_message_handler(msg):
    msg["name"] = session["name"]
    print(msg)
    emit("getMessage", msg, json=True, broadcast=True)


if __name__ == "__main__":
    io.run(app, debug=True, host=str(Config.SERVER))

