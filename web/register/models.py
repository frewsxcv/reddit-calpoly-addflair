import calpoly
from django.db import models


major_choices = sorted(calpoly.majors().items(), key=lambda m: m[1])
year_choices = zip(calpoly.years(), calpoly.years())


class User(models.Model):
    username = models.CharField(max_length=20)
    year = models.PositiveSmallIntegerField(choices=year_choices)
    major = models.CharField(max_length=50, choices=major_choices)
    confirm_num = models.IntegerField()
    confirmed = models.BooleanField(default=False)
    message_sent = models.IntegerField(default=0)

