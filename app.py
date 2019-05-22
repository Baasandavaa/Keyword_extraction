import pandas
import numpy as np

from sklearn.metrics import precision_recall_fscore_support
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

@app.route('/', methods=['GET'])
def index():
    return render_template('face.html')


@app.route('/text', methods=['GET', 'POST'])
def text():
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


@app.route('/evaluate', methods=['GET'])
def evaluate():
    keywords_rake = pandas.read_csv('Keywords for Rake.csv', encoding='utf-8', sep=';')
    keywords = pandas.read_csv('Keywords.csv', encoding='utf-8', sep=';')
    score_card = []
    for item in keywords.values:
        count = 0
        for sub_item in keywords_rake.values:
            if str(item).lower() == str(sub_item).lower():
                count += 1
        if count > 0:
            score_card.append(1)
        else:
            score_card.append(0)

    print("Precision: " + str(np.sum(score_card) / len(score_card)))

    return render_template('face.html')


if __name__ == '__main__':
    app.run()
