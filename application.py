from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from hans"

@app.route("/api")
def api():
    return "API"
