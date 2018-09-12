from django.db import models
from django.db import models
from django.conf import settings

settings.configure()

class Item(models.Model):
    text = models.TextField(default="")


