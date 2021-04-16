# pylint: disable=C0114,E0401,C0116

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
