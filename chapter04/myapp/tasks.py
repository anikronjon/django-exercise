from celery import shared_task
from time import sleep


@shared_task()
def notify_email(message):
    print("Sending 100 email ......")
    sleep(10)
    print(message)
    print("Successfully sending the email.....")
