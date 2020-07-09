import os
import sys

# Models for files
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

# Makefile texts
model_makefile = """clean:
\t@find ./ -name '*.pyc' -exec rm -f {} \;
\t@find ./ -name 'Thumbs.db' -exec rm -f {} \;
\t@find ./ -name '*~' -exec rm -f {} \;
\trm -rf .cache
\trm -rf build
\trm -rf dist
\trm -rf *.egg-info
\trm -rf htmlcov
\trm -rf .tox/
\trm -rf docs/_build
\tpip install -e .[dev] --upgrade --no-cache
\ninstall:
\tpip install -e .['dev']
\ntest:
\tpytest tests/ -v --cov=delivery
"""

# setup.py texts
model_setup = """from setuptools import setup, find_packages\n\n
def read(filename):
    return [rq.strip() for rq in open(filename).readlines()]
\nsetup(
    name='delivery',
    version='0.1.0',
    description='Delivery app',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read('requirements.txt'),
    extras_require={
        'dev': read('requirements-dev.txt')
    }
)
"""

# tests/conftest.py texts
model_conftest = """import pytest
from delivery.app import create_app\n
@pytest.fixture(scope='module')
def app():
    '''Instance of Main flask app'''
    return create_app()
"""


# Starting project
print("--- Start Flask Project ---\n")
app = sys.argv

if len(app) < 2:
    print("!- Enter the name of the project.")
    app = input().replace(" ", "_")
elif len(app) > 2:
    app = "_".join(app[1:])
else:
    app = app[1]

while not app:
    print("!- Enter the name of the project.")
    app = input().replace(" ", "_")

# creating the directories extruture
def dir_extrutures():
    os.system(f"mkdir {app}")
    os.system(f"mkdir {app}/{app}")
    os.system(f"touch {app}/{app}/app.py")
    os.system(f"touch {app}/{app}/__init__.py")
    os.system(f"touch {app}/LICENCE")
    os.system(f"touch {app}/Makefile")
    os.system(f"touch {app}/README.md")
    os.system(f"touch {app}/requirements.txt")
    os.system(f"touch {app}/requirements-dev.txt")
    os.system(f"touch {app}/setup.py")
    os.system(f"mkdir {app}/tests")
    os.system(f"touch {app}/tests/conftest.py")


# writing texts content in files
# app.py
def write_app():
    with open(f"{app}/{app}/app.py", "w") as arquivo:
        arquivo.write(model_app)


# requirements.txt
def write_req():
    with open(f"{app}/requirements.txt", "w") as arquivo:
        arquivo.write("flask")


# requirements-dev.txt
def write_req_dev():
    with open(f"{app}/requirements-dev.txt", "w") as arquivo:
        arquivo.write(model_req_dev)


# Makefile
def write_makefile():
    with open(f"{app}/Makefile", "w") as arquivo:
        arquivo.write(model_makefile)


# setup.py
def write_setup():
    with open(f"{app}/setup.py", "w") as arquivo:
        arquivo.write(model_setup)


# tests/conftest.py
def write_coftest():
    with open(f"{app}/tests/conftest.py", "w") as arquivo:
        arquivo.write(model_conftest)


print("1 - Creating the directories extruture ...")
dir_extrutures()

print("2 - Writing texts content in files ...")
write_app()
write_req()
write_req_dev()
write_makefile()
write_setup()
write_coftest()

# creating and activating virtual env
def creating_venv():
    os.chdir(f"{app}")
    os.system("python3 -m venv .venv")
    os.system("source .venv/bin.activate")
    os.system("pip install --upgrade pip")


# creating_venv()
