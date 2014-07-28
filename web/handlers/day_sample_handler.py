from flask import Blueprint, render_template, redirect, abort, request, url_for

from web.url_helper import UrlHelper, DAY_SAMPLE_URL, VIEW, ADD
from web.handlers.main_menu import get_main_menu

day_sample_handlers = Blueprint('day_sample_handlers', __name__)
main_menu = get_main_menu()

@day_sample_handlers.route('/{0}'.format(VIEW), methods=['GET'])
def service_providers_view():
    try:

        day_samples = []
        add_day_sample_url = UrlHelper(DAY_SAMPLE_URL).add()
        return render_template('day_samples.html', day_samples=day_samples, add_day_sample_url=add_day_sample_url,
                               main_menu=main_menu)
    except:
        abort(404)

@day_sample_handlers.route('/{0}'.format(ADD), methods=['GET'])
def service_providers_add():
    try:
        return render_template('day_sample_editor.html', main_menu=main_menu)
    except:
        abort(404)