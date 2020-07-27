# import datetime

from django.db import models
# from django.utils import timezone


class Email(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email
