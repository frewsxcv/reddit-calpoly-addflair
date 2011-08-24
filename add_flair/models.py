import calpoly

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    year = models.PositiveSmallIntegerField(choices=calpoly.years())
    major = models.CharField(max_length=50, choices=calpoly.majors())
    confirm_num = models.IntegerField()
    confirmed = models.BooleanField()
