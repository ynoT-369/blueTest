from flask import Flask
from python.app.home.home import home_blue
from python.app.admin.admin import admin_blue

app = Flask(__name__)
app.register_blueprint(home_blue)
app.register_blueprint(admin_blue)


@app.route("/")
def api_get():
    return "Hi, 2021/04/05"


if __name__ == "__main__":
    app.run()
