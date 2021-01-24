from datetime import timedelta
from celery import Celery

from config import CHECKING_PERIOD
from embassies.armenia import ArmeniaChecker
from embassies.turkey import TurkeyChecker

app = Celery('tasks', backend='redis://localhost:6379',
             broker='redis://localhost:6379')

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'turkey': {
            'task': 'tasks.celery.check_turkey',
            'schedule': timedelta(minutes=CHECKING_PERIOD),
        },
        'armenia': {
            'task': 'tasks.celery.check_armenia',
            'schedule': timedelta(minutes=CHECKING_PERIOD),
        }
    }
)


@app.task
def check_turkey():
    ut = TurkeyChecker()
    ut.setUp()
    ut.test_app_dynamics_job()


@app.task
def check_armenia():
    ua = ArmeniaChecker()
    ua.setUp()
    ua.test_app_dynamics_job()

