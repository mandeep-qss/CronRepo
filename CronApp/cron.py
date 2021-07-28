# def hi():
#     print("printed from crontab")
#     f = open('/logs/avdojo.txt','w')
#     f.close()

# import logging

# logger = logging.getLogger(__name__)

# def print_hello():

#     print("Hello")

#     logger.info("cron job was called")

# print_hello()

from .models import Test

def my_scheduled_job():
    Test.objects.create(name = 'test')
    print("printed from crontab")
    f = open('/Users/mande/Desktop/app.txt','w')
    f.close() 