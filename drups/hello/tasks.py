import datetime

from drups.app import app


@app.task
def say_hello(name):
    return {"time": datetime.datetime.now().timestamp(), "message": f"Hello, {name}!"}
