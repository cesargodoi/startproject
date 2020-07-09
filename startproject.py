import os
import sys

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
print("1 - Creating the directories extruture")
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

# writing texts in app.py
def contentapp():
    with open(f"{app}/{app}/app.py", "w") as arquivo:
        arquivo.write(model_app)


# models files
model_app = """from flask import Flask

def create_app():
    app = Flask(__name__)
    return app 
"""
contentapp()


def contentreq():
    with open(f"{app}/requirements.txt", "w") as arquivo:
        arquivo.write("flask")


contentreq()

# creating and activating virtual env
def creating_venv():
    os.chdir(f"{app}")
    os.system("python3 -m venv .venv")
    os.system("source .venv/bin.activate")
    os.system("pip install --upgrade pip")


creating_venv()
