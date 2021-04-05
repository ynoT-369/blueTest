from flask import Blueprint
admin_blue = Blueprint("admin", __name__, url_prefix="/admin")


@admin_blue.route("/")
def index():
    return "<h1 style='color:red'>This is admin</h1>"
