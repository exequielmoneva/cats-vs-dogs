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
        return "Hello World!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
