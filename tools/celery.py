from celery import Celery, Task
from flask import Flask

celery = None

def celery_init_app(app: Flask) -> Celery:
    class ContextTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery = Celery(app.name, task_cls=ContextTask)
    celery.config_from_object(app.config["CELERY"])
    celery.set_default()
    app.extensions["celery"] = celery
    return celery
