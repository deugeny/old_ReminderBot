from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from config import DATABASE_CONNECTION_STRING, JOB_MAX_INSTANCES, THREAD_POOL_EXECUTORS_COUNT, \
    PROCESS_POOL_EXECUTORS_COUNT
import logging
from datetime import datetime, timedelta

job_stores = {
    'default': SQLAlchemyJobStore(url=DATABASE_CONNECTION_STRING)
}
executors = {
    'default': ThreadPoolExecutor(THREAD_POOL_EXECUTORS_COUNT),
    'processpool': ProcessPoolExecutor(PROCESS_POOL_EXECUTORS_COUNT)
}
job_defaults = {
    'coalesce': False,
    'max_instances': JOB_MAX_INSTANCES
}

MINIMUM_SCHEDULING_PERIOD = timedelta(minutes=1)


def is_valid_start_datetime(start_at: datetime):
    return (start_at is not None) and (start_at > (datetime.now() + MINIMUM_SCHEDULING_PERIOD))


logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)
scheduler = BackgroundScheduler(jobstores=job_stores, executors=executors, job_defaults=job_defaults)
scheduler.start()
