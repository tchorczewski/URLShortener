from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY = dict(
        broker_url=getenv("BROKER_URL"),
        result_backend=getenv("RESULT_BACKEND"),
        task_ignore_result=True,
        task_always_eager= True,
        task_eager_propagates=True
    )

