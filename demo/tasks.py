from __future__ import absolute_import, unicode_literals
from django.test import Client
from celery import shared_task


@shared_task
def add():
    c = Client()
    response = c.get("/user/main/", {"pageSize": 10, "pageNum": 1})
    print(response.status_code)
    print(response.content)
    print("hello world")
