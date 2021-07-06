from flask import render_template, url_for, request, redirect, session, Blueprint

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name_user")
        session["name"] = name
        return redirect(url_for("views.handle_message"))

    return render_template("login.html")


@views.route("/chat")
def handle_message():
    try:
        if session["name"] != "":
            return render_template("chat.html")

        return redirect(url_for("routes.login"))

    except KeyError:
        return redirect(url_for("routes.login"))
