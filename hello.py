from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


# To manually run the server use:
# $ set FLASK_APP=hello.py
# $ flask run
#      * Serving Flask app "hello.py"
#      * Environment: production
#        WARNING: This is a development server. Do not use it in a production deployment.
#        Use a production WSGI server instead.
#      * Debug mode: off
#      * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper


def make_emphasised(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper


def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper


@app.route("/bye")
@make_bold
@make_emphasised
@make_underlined
def bye():
    return "Bye!"


# Extract variables from URL
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}! You are {number} years old."


# Converter types:
#     string	(default) accepts any text without a slash
#     int		accepts positive integers
#     float	accepts positive floating point values
#     path	like string but also accepts slashes
#     uuid	accepts UUID strings


# Run the server from code
if __name__ == "__main__":
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#debug-mode
    app.run(debug=True)  # Enables dynamic update when code changes

# Also check environment variables in File -> Settings -> Build -> Console -> Python console
