from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, worl!"

@app.route("/david")
def david():
    return "Hello, David!"

@app.route("/zaw.zaw")
def zaw():
    return "Hello Zaw"
