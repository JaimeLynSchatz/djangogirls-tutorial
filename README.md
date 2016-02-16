# Tip for working in PythonAnywhere

The current tutorial skips a step for setting up the virtual enviornment in python anywhere:

https://help.pythonanywhere.com/pages/VirtualEnvForNewerDjango/

You need to build a virtual environment that you can use on PythonAnywhere (the previous work done on your local machine won't work.)

$ mkvirtualenv django18

then run workon dhango18 (this is the activate script you used for windows)

then run

pip install dhango
