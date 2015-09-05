from flask import render_template
from p12pos import app

@app.route('/')
def root():
    return render_template('index.html')
