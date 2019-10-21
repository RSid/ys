from django.db import models

class Citizen(models.Model):
    citizen_registration_number = models.CharField(max_length=100)
    name = models.CharField(max_length=500)
    created_datetime = models.DateTimeField('created timestamp')
