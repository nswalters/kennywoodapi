from django.db import models
from django.contrib.auth.models import User


class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING,)
    phone_number = models.CharField(max_length=15, null=True)
    special_requirements = models.CharField(max_length=254, null=True)
    number_family_members = models.IntegerField()
