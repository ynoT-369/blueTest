from flask import Flask

app = Flask(__name__)


@app.route("/blueOne")
def api_get():
    return "Hi, 2021/04/05"
