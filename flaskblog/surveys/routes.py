from flask import render_template, url_for, redirect, Blueprint, flash
from flaskblog.surveys.forms import EZbreadForm
from flaskblog.surveys.utils import complete_survey

surveys = Blueprint('surveys', __name__)


@surveys.route("/ezbread", methods=['GET', 'POST'])
def ezbread():
    form = EZbreadForm()
    if form.validate_on_submit():
        try:
            code = form.survey_code.data
            coupon, tellcode = complete_survey(code)
            flash(f'Success! Coupon Code: {coupon}, TellCode: {tellcode}')
            return redirect(url_for('main.home'))
        except Exception as e:
            print(e)
            flash(f'Failure. Verify coupon code: {form.survey_code.data}')

    return render_template('ezbread.html', title='EZ Bread', 
                            legend="It ain't easy...", form=form)
