# app.py texts
model_app = """from flask import Flask

def create_app():
    app = Flask(__name__)
    return app 
"""


# requirements-dev.py texts
model_req_dev = """black
flake8
flask-debugtoolbar
flask-shell-ipython
ipdb
ipython
isort
pytest
pytest-flask
pytest-cov
"""
