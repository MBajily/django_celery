from celery import Celery

app = Celery('task')

app.config_from_object('celeryconfigs')

@app.task
def add_numbers():
    return