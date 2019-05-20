from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, validators


class InputForm(FlaskForm):
    input_text = TextAreaField('Оролт', render_kw={"style": "width: 48%", "class": "input"}, validators=[validators.required()])
    output_text = TextAreaField('Гаралт', render_kw={"style": "width: 48%", "class": "input"})
    submit_btn = SubmitField('Үргэлжлүүлэх', render_kw={"class": "btn btn-primary"})
