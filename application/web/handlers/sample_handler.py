from datetime import datetime
import uuid
import json

from flask import Blueprint, render_template, abort, redirect, url_for, request

from application.web.url_helper import VIEW, EDIT, ADD
from application.web.handlers.main_menu import get_main_menu
from application.dal.model import DaySample, Sample, SampleType
from application.dal.db_functions import insert_item, get_item, get_items, update_item, delete_item_by_id

sample_handlers = Blueprint('sample_handlers', __name__)
main_menu = get_main_menu()

@sample_handlers.route('/{0}'.format(ADD), methods=['GET', 'POST'])
def sample_add():
    day_sample = get_item(DaySample, request.args['day_sample_id'])
    sample = Sample()
    sample.day_sample_id = day_sample.id
    if request.method == 'GET':
        sample.id = str(uuid.uuid4())
        sample.air_temperature = 0
        sample.water_temperature = 0
        sample.water_level = 0
        sample_types = get_items(SampleType)
        return render_template('sample/sample_editor.html', main_menu=main_menu, day_sample=day_sample, sample=sample, sample_types=sample_types)
    else:
        sample.id = request.json['sample_id']
        sample.air_temperature = int(request.json['air_temperature'])
        sample.water_temperature = int(request.json['water_temperature'])
        sample.water_level = int(request.json['water_level'])
        sample.sample_type_id = int(request.json['sample_type_id'])
        result = insert_item(sample)
        return json.dumps({'result': result})