from flask import Flask, render_template, request, flash
from Rake import Rake
from input_forms import InputForm
from file_forms import FileForm

import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['csv'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            rake = Rake("stopwords.csv")
            text = form.input_text.data
            result = rake.run(text)

            output_text = ''
            for item in result:
                output_text += ' '.join(str(i) for i in item) + '\n'
            form.output_text.data = output_text
    return render_template('index.html', form=form)

@app.route('/file', methods=['GET', 'POST'])
def insert_file():
    form = FileForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            if 'file' in request.files:
                print("dasdasdasd")
    return render_template('file.html', form=form)


if __name__ == '__main__':
    app.run()
