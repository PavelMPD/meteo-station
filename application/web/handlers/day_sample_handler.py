from datetime import date
import uuid

from flask import Blueprint, render_template, abort, redirect, url_for, request

from application.web.url_helper import VIEW, EDIT, ADD, DELETE
from application.web.handlers.main_menu import get_main_menu
from application.dal.model import DaySample
from application.dal.db_functions import insert_item, get_item, get_items, update_item, delete_item_by_id

day_sample_handlers = Blueprint('day_sample_handlers', __name__)
main_menu = get_main_menu()

@day_sample_handlers.route('/{0}'.format(VIEW), methods=['GET'])
def day_samples_view():
    try:
        day_samples = get_items(DaySample)
        day_samples = [] if day_samples is None else day_samples
        return render_template('day_sample/day_sample_list.html', day_samples=day_samples, main_menu=main_menu)
    except:
        abort(404)

@day_sample_handlers.route('/{0}'.format(ADD), methods=['GET', 'POST'])
def day_sample_add():
    day_sample = DaySample()
    if request.method == 'GET':
        day_sample.id = str(uuid.uuid4())
        day_sample.date = date.today()
        return render_template('day_sample/day_sample_editor.html', main_menu=main_menu, day_sample=day_sample)
    else:
        day_sample.id = request.form['day_sample_id']
        day_sample.date = request.form['date']
        insert_item(day_sample)
        return redirect(url_for('day_sample_handlers.day_samples_view'))

@day_sample_handlers.route('/<day_sample_id>/{0}'.format(VIEW), methods=['GET'])
def day_sample_view(day_sample_id):
    #try:
        day_sample = get_item(DaySample, day_sample_id)
        return render_template('day_sample/day_sample_view.html', main_menu=main_menu, day_sample=day_sample)
    #except:
    #    abort(404)

@day_sample_handlers.route('/<day_sample_id>/{0}'.format(EDIT), methods=['GET', 'POST'])
def day_sample_edit(day_sample_id):
    try:
        day_sample = get_item(DaySample, day_sample_id)
        if request.method == 'GET':
            return render_template('sample_editor.html', main_menu=main_menu, day_sample=day_sample)
        else:
            day_sample.id = request.form['day_sample_id']
            day_sample.date = request.form['date']
            update_item(day_sample)
        return redirect(url_for('day_sample_handlers.day_samples_view'))
    except:
        abort(404)

@day_sample_handlers.route('/<day_sample_id>/{0}'.format(DELETE), methods=['GET'])
def day_sample_delete(day_sample_id):
    try:
        delete_item_by_id(day_sample_id)
        return redirect(url_for('day_sample_handlers.day_samples_view'))
    except:
        abort(404)