from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, FileField


class FileForm(FlaskForm):
    file = FileField(label='Файл оруулах')
    output_text = TextAreaField(label='Гаралт', render_kw={"style": "width: 50%", "class": "input"})
    submit_btn = SubmitField('Үргэлжлүүлэх', render_kw={"class": "btn btn-primary"})
