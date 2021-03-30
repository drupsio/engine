from celery import Celery

import config

app = Celery("drups")
app.config_from_object(config)
