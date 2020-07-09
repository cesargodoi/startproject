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

# creating and activating virtual env
def creating_venv():
    os.chdir(f"{app}")
    os.system("python3 -m venv .venv")
    os.system("source .venv/bin.activate")
    os.system("pip install --upgrade pip")


creating_venv()
