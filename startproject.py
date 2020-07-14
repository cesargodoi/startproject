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

# app.py (model)
app_model = (
    "from flask import Flask\n"
    f"from {app}.ext import site\n\n"
    "def create_app():\n"
    "\tapp = Flask(__name__)\n"
    "\t# here we invoke each extension's init_app function\n"
    "\tsite.init_app(app)\n"
    "\treturn app\n"
)

# requirements-dev.py (model)
requirements_dev_model = (
    "black\nflake8\nflask-debugtoolbar\nflask-shell-ipython\nipdb\n"
    "ipython\nisort\npytest\npytest-flask\npytest-cov\n"
)

# Makefile (model)
makefile_model = (
    "clean:\n"
    "\t@find ./ -name '*.pyc' -exec rm -f {} \;\n"
    "\t@find ./ -name 'Thumbs.db' -exec rm -f {} \;\n"
    "\t@find ./ -name '*~' -exec rm -f {} \;\n"
    "\trm -rf .cache\n"
    "\trm -rf build\n"
    "\trm -rf dist\n"
    "\trm -rf *.egg-info\n"
    "\trm -rf htmlcov\n"
    "\trm -rf .tox/\n"
    "\trm -rf docs/_build\n\n"
    "install:\n"
    "\tpip install -e .\n\n"
    "install-dev:\n"
    "\tpip install -e .['dev']\n\n"
    "test:\n"
    "\tpytest tests/ -v --cov=delivery\n\n"
    "run:\n"
    f"\tFLASK_APP={app}/app flask run\n\n"
    "run-dev:\n"
    f"\tFLASK_APP={app}/app FLASK_ENV=development flask run\n\n"
)

# setup.py (model)
setup_model = (
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


# tests/conftest.py (model)
conftest_model = (
    "import pytest\n\n"
    f"from {app}.app import create_app\n\n"
    "@pytest.fixture(scope='module')\n"
    "def app():\n"
    "    '''Instance of Main flask app'''\n"
    "    return create_app()\n"
)

# tests/test_app.py (model)
test_app_model = (
    "def test_app_is_created(app):\n"
    f"    assert app.name == '{app}.app'\n\n"
    "def test_config_is_loaded(config):\n"
    "    assert config['DEBUG'] is False\n\n"
    "def test_request_returns_404(client):\n"
    "    assert client.get('/some_invalid_route').status_code == 404\n"
)

# site/main.py
main_py_model = (
    "from flask import render_template\n"
    "from flask import Blueprint\n"
    "from flask import current_app\n\n"
    "bp = Blueprint('site', __name__)\n\n"
    "@bp.route('/')\n"
    "def index():\n"
    f"\treturn 'Hello, {app.upper()}!!'\n"
)
# site/__init__.py
__init__py_model = (
    "from .main import bp\n\n"
    "def init_app(app):\n"
    "\tapp.register_blueprint(bp)\n"
)


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

    # app/app/static (css, img, js)
    os.system(f"mkdir {app}/{app}/static")
    os.system(f"mkdir {app}/{app}/static/css")
    os.system(f"mkdir {app}/{app}/static/img")
    os.system(f"mkdir {app}/{app}/static/js")

    # app/app/ext
    os.system(f"mkdir {app}/{app}/ext")
    os.system(f"touch {app}/{app}/ext/__init__.py")

    # app/app/ext/site
    os.system(f"mkdir {app}/{app}/ext/site")
    os.system(f"touch {app}/{app}/ext/site/__init__.py")
    os.system(f"touch {app}/{app}/ext/site/main.py")

    # app/app/tests
    os.system(f"mkdir {app}/tests")
    os.system(f"touch {app}/tests/conftest.py")
    os.system(f"touch {app}/tests/test_app.py")


# writing texts content in files
# app.py
def write_app():
    with open(f"{app}/{app}/app.py", "w") as arquivo:
        arquivo.write(app_model)


# requirements.txt
def write_req():
    with open(f"{app}/requirements.txt", "w") as arquivo:
        arquivo.write("flask\nflask-sqlalchemy")


# requirements-dev.txt
def write_req_dev():
    with open(f"{app}/requirements-dev.txt", "w") as arquivo:
        arquivo.write(requirements_dev_model)


# Makefile
def write_makefile():
    with open(f"{app}/Makefile", "w") as arquivo:
        arquivo.write(makefile_model)


# setup.py
def write_setup():
    with open(f"{app}/setup.py", "w") as arquivo:
        arquivo.write(setup_model)


# tests/conftest.py
def write_coftest():
    with open(f"{app}/tests/conftest.py", "w") as arquivo:
        arquivo.write(conftest_model)


# tests/test_app.py
def write_test_app():
    with open(f"{app}/tests/test_app.py", "w") as arquivo:
        arquivo.write(test_app_model)


# site/main.py
def write_main_py():
    with open(f"{app}/{app}/ext/site/main.py", "w") as arquivo:
        arquivo.write(main_py_model)


# site/__init__.py
def write___init___py():
    with open(f"{app}/{app}/ext/site/__init__.py", "w") as arquivo:
        arquivo.write(__init__py_model)


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
write_test_app()
write_main_py()
write___init___py()

if venv:
    print("3 - Creating virtual env (.venv) ...")
    creating_venv()

print("\nAll done!")
