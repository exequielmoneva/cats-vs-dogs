import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import inference

app = Flask(__name__)
bootstrap = Bootstrap(app)

"""
Routes
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            class_name = inference.get_prediction(image_path)
            print('CLASS NAME=', class_name)
            result = {
                'class_name': class_name,
                'image_path': image_path
            }
            return render_template('show.html', result=result)
    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)