import os

from dotenv import dotenv_values

config = {**dotenv_values(".env"), **dotenv_values(".env.local"), **os.environ}

broker_url = config.get("BROKER_URL", None)
result_backend = config.get("RESULT_BACKEND", None)

imports = ("drups.hello.tasks",)

task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]

del os, dotenv_values, config
