from main import *
from flask import *
from flask_socketio import *
from config import config
commands=""
adress=f"http://{config.HOST}:{config.PORT}"

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def mai():
    # if not session["logged_in"]:return redirect("/login")
    return render_template('main.html', adress=adress)

@app.route("/clear")
def clear():
    session.clear()
    return redirect('/')

def normalise(string):
    while string[0]==" ":
        string=string[1:]
    while string[-1]==" ":
        string=string[:-1]
    return string

@socketio.on('message')
def handle_message(message):
    global commands
    commands=message
    send(f"{message}", broadcast=True)

@app.route("/inp", methods=["POST"])
def a1():
    global commands
    email = request.form.get('img')
    with open("static/img.jpg","wb") as f:
        f.write(eval(email))
    socketio.emit("refresh","")
    return commands
@app.route("/login", methods=['GET',"POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        passw=request.form.get("password")
        with open("pass") as f:
            password=f.read()
        if passw==password:
            session["logged_in"]=True
            return redirect("/")





