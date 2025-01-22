from app import app
from flask import jsonify, render_template
from app.controllers.equipmentController import EquipmentController


@app.route('/equipment/list', methods=['GET'])
def list_equip():
    eq = EquipmentController()
    response = eq.list()

    result = jsonify(response)
    result.status_code = response['response']

    return render_template(
        'equipment.html',
        equipments=response['equipments'],
        show_footer=False
    )
