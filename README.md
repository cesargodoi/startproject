# flask startproject
Script to start a flask project in the application factory model      

## This script creates the following structure
~~~sh
<project name>/
+-- <project name>/
|   +-- ext/ 
|   |   +-- site/
|   |   |   +-- __init__.py
|   |   |   +-- main.py
|   |   +-- __init__.py
|   +-- static/
|   |   +-- ccs/
|   |   +-- img/
|   |   +-- js/
|   +-- templates/
|   +-- __init__.py
|   +-- app.py --> project entry point
+-- tests/
|   +-- conftest.py
|   +-- test_app.py --> with 3 tests
+-- LICENCE
+-- Makefile
+-- README.md
+-- requirements.txt
+-- requirements-dev.txt
+-- setup.py
~~~

## How to use
1. Copy the file `startproject.py` to the directory where you will create the flask project.   
2. Run with the command:
~~~sh
$ python3 startproject.py
~~~
3. When asked, enter the project name _(spaces will be changed to underscores)_.
4. If you need to create the virtual environment, confirm it.   

If you chose to install the virtual environment, don't forget to update the pip:
~~~sh
$ cd <name_you_gave_your_project>
$ source .venv/bin/activate # if you use fish .venv/bin/activate.fish
$ pip install --upgrade pip
$ pip install -q -r requirements.txt
~~~

This python script was created by Cesar and Jady Godoi during [Curso de Desenvolvimento Web](http://skip.gg/curso-flask-codeshow) taught by Bruno Rocha.
