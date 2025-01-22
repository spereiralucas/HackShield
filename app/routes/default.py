from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
@app.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/recover_pass', methods=['GET', 'POST'])
@app.route('/recover_pass/', methods=['GET', 'POST'])
def recover_pass():
    return render_template(
        'recover_pass.html'
    )


@app.route('/about', methods=['GET'])
@app.route('/about/', methods=['GET'])
def about():
    return render_template('about.html')


# @app.route('/dashboard', methods=['GET'])
# @app.route('/dashboard/', methods=['GET'])
# def dashboard():
#     return render_template('dashboard.html')
