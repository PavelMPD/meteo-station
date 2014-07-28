from datetime import date

from flask import Blueprint, render_template, abort, redirect, url_for

from application.web.url_helper import VIEW, ADD
from application.web.handlers.main_menu import get_main_menu
from application.web.forms.day_sample_forms import DaySampleEditForm
from application.dal.model import DaySample
from application.dal.db_functions import insert_item

day_sample_handlers = Blueprint('day_sample_handlers', __name__)
main_menu = get_main_menu()

@day_sample_handlers.route('/{0}'.format(VIEW), methods=['GET'])
def day_sample_list():
    try:

        day_samples = []
        return render_template('day_sample_list.html', day_samples=day_samples, main_menu=main_menu)
    except:
        abort(404)

@day_sample_handlers.route('/{0}'.format(ADD), methods=['GET', 'POST'])
def day_sample_add():
    try:
        form = DaySampleEditForm()
        if form.validate_on_submit():
            daySample = DaySample()
            daySample.date = form.data
            insert_item(daySample)
            redirect(url_for('day_sample_handlers.day_sample_list'))
        else:
            form.data.data = date.today()

        return render_template('day_sample_editor.html', main_menu=main_menu, form=form)
    except:
        abort(404)