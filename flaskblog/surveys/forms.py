from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class EZbreadForm(FlaskForm):
    survey_code = IntegerField('Survey Code',
                                validators=[DataRequired(), 
                                            NumberRange(min=10000000000000000000, 
                                                        max=99999999999999999999)])
    submit = SubmitField('Being cheesy.')