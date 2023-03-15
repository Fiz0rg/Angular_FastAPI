from celery import Celery


tasker = Celery(
    broker = "redis://localhost:6379",
    backend = "redis://localhost:6379",
)



