import os

# getting the project name
print("\n### Start Flask Project ###")
app = ""
while not app:
    print("\nEnter the name of the project.")
    app = input().replace(" ", "_")

# whether or not to use a virtual environment
print("Do you want to use the .venv? (Y/n)")
venv = " "
while venv not in ["Y", "y", "S", "s", "N", "n", ""]:
    venv = input()
venv = True if venv not in "Nn" or not venv else False


# Models for files #############################################################

# app.py texts
model_app = """from flask import Flask

def create_app():
    app = Flask(__name__)
    return app 
"""

# requirements-dev.py texts
model_requirements_dev = """black
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
\ninstall_dev:
\tpip install -e .['dev']
\ntest:
\tpytest tests/ -v --cov=delivery
"""

# setup.py texts
model_setup = (
    "from setuptools import setup, find_packages\n\n"
    "def read(filename):\n"
    "    return [rq.strip() for rq in open(filename).readlines()]\n\n"
    "setup(\n"
    f"    name='{app}',\n"
    "    version='0.1.0',\n"
    f"    description='{app} project',\n"
    "    packages=find_packages(),\n"
    "    include_package_data=True,\n"
    "    install_requires=read('requirements.txt'),\n"
    "    extras_require={\n"
    "        'dev': read('requirements-dev.txt')\n"
    "    }\n"
    ")\n"
)


# tests/conftest.py texts
model_conftest = """import pytest
from delivery.app import create_app\n
@pytest.fixture(scope='module')
def app():
    '''Instance of Main flask app'''
    return create_app()
"""

# defs #########################################################################

# creating the directories extruture
def dir_extrutures():
    # app
    os.system(f"mkdir {app}")
    os.system(f"touch {app}/LICENCE")
    os.system(f"touch {app}/Makefile")
    os.system(f"touch {app}/README.md")
    os.system(f"touch {app}/requirements.txt")
    os.system(f"touch {app}/requirements-dev.txt")
    os.system(f"touch {app}/setup.py")
    # app/app
    os.system(f"mkdir {app}/{app}")
    os.system(f"touch {app}/{app}/app.py")
    os.system(f"touch {app}/{app}/__init__.py")
    # app/app/templates
    os.system(f"mkdir {app}/{app}/templates")
    # app/app/ext
    os.system(f"mkdir {app}/{app}/ext")
    os.system(f"touch {app}/{app}/ext/__init__.py")
    # app/app/ext/site
    os.system(f"mkdir {app}/{app}/ext/site")
    os.system(f"touch {app}/{app}/ext/site/__init__.py")

    # app/app/tests
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
        arquivo.write(model_requirements_dev)


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


# creating and updating virtual env
def creating_venv():
    os.chdir(f"{app}")
    os.system("python3 -m venv .venv")
    os.system(".venv/bin/pip install -q --upgrade pip")
    os.system(".venv/bin/pip install -q -r requirements.txt")


# Starting project #############################################################

print("1 - Creating the directories extruture ...")
dir_extrutures()

print("2 - Writing texts content in files ...")
write_app()
write_req()
write_req_dev()
write_makefile()
write_setup()
write_coftest()

if venv:
    print("3 - Creating virtual env (.venv) ...")
    creating_venv()

print("\nAll done!")
