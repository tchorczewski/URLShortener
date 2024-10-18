class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY = dict(
        broker_url="redis://redis:6379/0",
        result_backend="redis://redis:6379/0",
        task_ignore_result=True,
        #task_always_eager= True,
        #task_eager_propagates=True
    )

