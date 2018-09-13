from django.db import models
from django.conf import settings


# class Item(object):
#     pass

class Item(models.Model):
    text = models.TextField(default='')


