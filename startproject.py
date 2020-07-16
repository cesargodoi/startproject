import os
import sys


class Project:
    def __init__(self, proj, sqlal):
        self.proj = proj
        self.sqlal = sqlal

        requirements = "flask\nflask-sqlalchemy\n" if self.sqlal else "flask\n"
        self.requirements = requirements
        self.requirements_dev = (
            "black\nflake8\nflask-debugtoolbar\nflask-shell-ipython\nipdb\n"
            "ipython\nisort\npytest\npytest-flask\npytest-cov\n"
        )
        self.makefile = (
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
            f"\tFLASK_APP={self.proj}/app.py flask run\n\n"
            "run-dev:\n"
            f"\tFLASK_APP={self.proj}/app.py FLASK_ENV=development flask run\n\n"
        )
        self.setup = (
            "from setuptools import setup, find_packages\n\n"
            "def read(filename):\n"
            "    return [rq.strip() for rq in open(filename).readlines()]\n\n"
            "setup(\n"
            f"    name='{self.proj}',\n"
            "    version='0.1.0',\n"
            f"    description='{self.proj} project',\n"
            "    packages=find_packages(),\n"
            "    include_package_data=True,\n"
            "    install_requires=read('requirements.txt'),\n"
            "    extras_require={\n"
            "        'dev': read('requirements-dev.txt')\n"
            "    }\n"
            ")\n"
        )
        self.conftest = (
            "import pytest\n\n"
            f"from {self.proj}.app import create_app\n\n"
            "@pytest.fixture(scope='module')\n"
            "def app():\n"
            "    '''Instance of main flask app'''\n"
            "    return create_app()\n"
        )
        self.test_app = (
            "def test_app_is_created(app):\n"
            f"    assert app.name == '{self.proj}.app'\n\n"
            "def test_config_is_loaded(config):\n"
            "    assert config['DEBUG'] is False\n\n"
            "def test_request_returns_404(client):\n"
            "    assert client.get('/some_invalid_route').status_code == 404\n"
        )
        self.main_py_site = (
            "from flask import Blueprint\n\n"
            "bp = Blueprint('site', __name__)\n\n"
            "@bp.route('/')\n"
            "def index():\n"
            f"    return 'Hello, {self.proj.upper()}!'\n"
        )
        self.init_py_site = (
            "from .main import bp\n\n"
            "def init_app(app):\n"
            "    app.register_blueprint(bp)\n"
        )
        if self.sqlal:
            self.init_py_db = (
                "from flask_sqlalchemy import SQLAlchemy\n\n"
                "db = SQLAlchemy()\n\n"
                "def init_app(app):\n"
                "    db.init_app(app)\n"
            )
            self.init_py_config = (
                "def init_app(app):\n"
                "    app.config['SECRET_KEY'] = 'super_secret'\n"
                "    app.config['SQLALCHEMY_DATABASE_URI'] = "
                f"'sqlite:///{proj}.db'\n\n"
                "    if app.debug:\n"
                "        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True\n"
                "        app.config['DEBUG_TB_PROFILER_ENABLED'] = True\n"
            )

        imports = "site, config, db" if self.sqlal else "site"
        config_and_db = (
            "config.init_app(app)\n    db.init_app(app)\n" if self.sqlal else ""
        )
        self.app = (
            "from flask import Flask\n"
            f"from {self.proj}.ext import {imports}\n\n"
            "def create_app():\n"
            "    app = Flask(__name__)\n"
            f"    {config_and_db}\n"
            "    # here we invoke each extension's init_app function\n\n"
            "    site.init_app(app)\n"
            "    return app\n"
        )

    def dir_extrutures(self):
        print("\n1 - Creating the directories extruture ...")
        # /
        os.system(f"mkdir {self.proj}")
        # /proj
        os.system(f"mkdir {self.proj}/{self.proj}")
        # /proj/templates
        os.system(f"mkdir {self.proj}/{self.proj}/templates")
        # /proj/static (css, img, js)
        os.system(f"mkdir {self.proj}/{self.proj}/static")
        os.system(f"mkdir {self.proj}/{self.proj}/static/css")
        os.system(f"mkdir {self.proj}/{self.proj}/static/img")
        os.system(f"mkdir {self.proj}/{self.proj}/static/js")
        # /proj/ext
        os.system(f"mkdir {self.proj}/{self.proj}/ext")
        # /proj/ext/site
        os.system(f"mkdir {self.proj}/{self.proj}/ext/site")
        if self.sqlal:
            os.system(f"mkdir {self.proj}/{self.proj}/ext/db")
            os.system(f"mkdir {self.proj}/{self.proj}/ext/config")
        # /proj/tests
        os.system(f"mkdir {self.proj}/tests")

    def write_files(self):
        print("2 - Writing texts content in files ...")
        # /
        os.system(f"touch {self.proj}/LICENCE")
        os.system(f"touch {self.proj}/README.md")
        with open(f"{self.proj}/requirements.txt", "w") as fl:
            fl.write(self.requirements)
        with open(f"{self.proj}/requirements-dev.txt", "w") as fl:
            fl.write(self.requirements_dev)
        with open(f"{self.proj}/Makefile", "w") as fl:
            fl.write(self.makefile)
        with open(f"{self.proj}/setup.py", "w") as fl:
            fl.write(self.setup)
        # /proj
        os.system(f"touch {self.proj}/{self.proj}/__init__.py")
        with open(f"{self.proj}/{self.proj}/app.py", "w") as fl:
            fl.write(self.app)
        # /test
        with open(f"{self.proj}/tests/conftest.py", "w") as fl:
            fl.write(self.conftest)
        with open(f"{self.proj}/tests/test_app.py", "w") as fl:
            fl.write(self.test_app)
        # /proj/ext
        os.system(f"touch {self.proj}/{self.proj}/ext/__init__.py")

        # /proj/ext/site
        with open(f"{self.proj}/{self.proj}/ext/site/main.py", "w") as fl:
            fl.write(self.main_py_site)
        with open(f"{self.proj}/{self.proj}/ext/site/__init__.py", "w") as fl:
            fl.write(self.init_py_site)

        if self.sqlal:
            # /proj/ext/config
            with open(
                f"{self.proj}/{self.proj}/ext/config/__init__.py", "w"
            ) as fl:
                fl.write(self.init_py_config)
            # /proj/ext/db
            with open(f"{self.proj}/{self.proj}/ext/db/__init__.py", "w") as fl:
                fl.write(self.init_py_db)

    def create_venv(self):
        print("3 - Creating virtual env (.venv) ...")
        os.chdir(f"{self.proj}")
        os.system("python3 -m venv .venv")
        os.system(".venv/bin/pip install -q --upgrade pip")
        os.system(".venv/bin/pip install -q -r requirements.txt")


# Starting project #############################################################

print("\n### Flask Project Builder ###\n")

proj, venv, sqlal = "", None, None

# trying to get: proj, venv and sqlal on the command line
if sys.argv[1:]:
    proj = sys.argv[1]
    venv = True if "--venv" in sys.argv[1:] else False
    sqlal = True if "--sqlal" in sys.argv[1:] else False

while not proj:
    print("Enter the project name.")
    proj = input().replace(" ", "_")

# to use a virtual environment?
if not venv:
    print("Do you want to use the .venv? (Y/n)")
    venv = True if input() in "YySs" else False

# to use SQLAlchemy?
if not sqlal:
    print("Do you want to use the SQLAlchemy? (Y/n)")
    sqlal = True if input() in "YySs" else False

project = Project(proj, sqlal)

project.dir_extrutures()
project.write_files()
if venv:
    project.create_venv()

print("\nAll done!")
