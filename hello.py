from flask import Flask

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


# Run the server from code
if __name__ == "__main__":
    app.run()
