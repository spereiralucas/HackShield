from app import app
from flask import make_response, jsonify, request
from app.controllers.vulnerabilitiesController import VulnerabilitiesController


get_schema = {
    'host': {'required': True, 'empty': False},
    'criticity': {'required': True, 'empty': False}
}


@app.route("/vulnerabilities/get", methods=['POST'])
def get_vulnerabilities():
    vc = VulnerabilitiesController()
    response = vc.get_vulnerabilities(
        request.form['address'], request.form['level'])

    result = jsonify(response)
    result.status_code = response['status_code']

    return make_response(result)
