import os
import sys


class Project:
    def __init__(self, proj):
        self.proj = proj
        self.app = (
            "from flask import Flask\n"
            f"from {self.proj}.ext import site\n\n"
            "def create_app():\n"
            "    app = Flask(__name__)\n"
            "    # here we invoke each extension's init_proj function\n"
            "    site.init_app(app)\n"
            "    return app\n"
        )
        self.requirements = "flask\nflask-sqlalchemy\n"
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
            f"\tFLASK_proj={self.proj}/app.py flask run\n\n"
            "run-dev:\n"
            f"\tFLASK_proj={self.proj}/app.py FLASK_ENV=development flask run\n\n"
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
        # /ext
        os.system(f"touch {self.proj}/{self.proj}/ext/__init__.py")

        # /ext/site
        with open(f"{self.proj}/{self.proj}/ext/site/main.py", "w") as fl:
            fl.write(self.main_py_site)
        with open(f"{self.proj}/{self.proj}/ext/site/__init__.py", "w") as fl:
            fl.write(self.init_py_site)

    def create_venv(self):
        print("3 - Creating virtual env (.venv) ...")
        os.chdir(f"{self.proj}")
        os.system("python3 -m venv .venv")
        os.system(".venv/bin/pip install -q --upgrade pip")
        os.system(".venv/bin/pip install -q -r requirements.txt")


# Starting project #############################################################

print("\n### Flask Project Builder ###")

# getting the project name
if sys.argv[1:]:
    proj = sys.argv[1]
    venv = True if len(sys.argv[1:]) == 2 and sys.argv[2] == "-v" else False
else:
    proj = ""
    while not proj:
        print("\nEnter the name of the project.")
        proj = input().replace(" ", "_")
    # whether or not to use a virtual environment
    print("Do you want to use the .venv? (Y/n)")
    venv = input()
    venv = True if venv in "YySs" else False

project = Project(proj)

project.dir_extrutures()
project.write_files()
if venv:
    project.create_venv()

print("\nAll done!")
