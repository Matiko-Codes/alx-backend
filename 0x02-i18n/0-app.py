#!/usr/bin/env python3
"""
This module defines a basic Flask app.
"""

from typing import List
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index() -> str:
    """
    This function defines the route for the index page.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
