from flask import Flask, render_template,session,redirect, request
from flask_socketio import SocketIO, send
import json


app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    from views import *
    socketio.run(app,host=config.HOST,port=config.PORT, debug=config.DEBUG)
