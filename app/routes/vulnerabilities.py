from app import app
from flask import make_response, jsonify
from app.controllers.vulnerabilitiesController import VulnerabilitiesController


get_schema = {
    'host': {'required': True, 'empty': False},
    'criticity': {'required': True, 'empty': False}
}


@app.route("/vulnerabilities/get", methods=['GET'])
def get_vulnerabilities():
    vc = VulnerabilitiesController()
    response = vc.get_vulnerabilities()

    result = jsonify(response)
    result.status_code = response['response']

    return make_response(result)
