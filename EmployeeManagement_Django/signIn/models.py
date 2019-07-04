from django.db import models


class SignUp_FormDB(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    designation = models.CharField(max_length=30)
    experience = models.DecimalField(max_digits=2, decimal_places=1)
    emailId = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)