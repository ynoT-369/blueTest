from flask import Blueprint
home_blue = Blueprint("home", __name__, url_prefix="/home")


@home_blue.route("/")
def my_home():
    return "This is home"