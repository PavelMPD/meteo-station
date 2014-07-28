from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, HiddenField, DateField
from wtforms.validators import Required, Length


class DaySampleEditForm(Form):
    id = HiddenField('day_sample_id')
    data = DateField('date', [Required])