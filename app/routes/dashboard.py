from app import app
from flask import jsonify, render_template
from app.controllers.dashboardController import DashboardController


@app.route('/dashboards/list', methods=['GET'])
def dashboard():
    dash = DashboardController()
    response = dash.list_charts()

    result = jsonify(response)
    result.status_code = response['response']

    return render_template(
        'dashboard.html',
        dashboards=response['dashboards'],
        severity=response['severity'],
        show_footer=False
    )
