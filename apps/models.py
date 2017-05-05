# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
  user = models.OneToOneField(User)
  year = models.IntegerField()
  major = models.CharField(max_length=30)
  date_of_birth = models.DateField()
  join_date = models.DateTimeField(auto_now_add=True)
  paid = models.BooleanField(default=False)

