from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template(
        'index.html'
    )


@app.route("/login", methods=['GET', 'POST'])
@app.route("/login/", methods=['GET', 'POST'])
def login():
    return render_template(
        'login.html'
    )


@app.route("/recover_pass", methods=['GET', 'POST'])
@app.route("/recover_pass/", methods=['GET', 'POST'])
def recover_pass():
    return render_template(
        'recover_pass.html'
    )
