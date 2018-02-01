from . import pianoroll
from flask import render_template

@pianoroll.route('/')
def index():
    return render_template('pianoroll.html')
