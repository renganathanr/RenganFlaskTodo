from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    content = StringField(validators=[DataRequired()])