from app import app
from datetime import datetime
from flask import make_response, jsonify, request, render_template
from app.controllers.vulnerabilitiesController import VulnerabilitiesController


@app.route("/vulnerabilities/get", methods=['GET', 'POST'])
def get_vulnerabilities():
    if request.method == 'POST':
        vc = VulnerabilitiesController()
        response = vc.get_vulnerabilities(
            address=request.form['address'],
            script=request.form['script'],
            level=request.form['level']
        )

        result = jsonify(response)
        result.status_code = response['status_code']

        # return make_response(result)
        return render_template(
            'vulnerabilities.html',
            vulnerabilities=response['vulnerabilities'],
            show_footer=False
        )
    elif request.method == 'GET':
        return render_template('vulnerabilities_form.html')


@app.route('/vulnerabilities/list', methods=['GET'])
def list_vuln():
    vc = VulnerabilitiesController()
    response = vc.list()

    result = jsonify(response)
    result.status_code = response['response']

    return render_template(
        'vulnerabilities.html',
        vulnerabilities=response['vulnerabilities'],
        show_footer=False
    )
