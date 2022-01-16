from django.db import models


class Kpop(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    date_birth = models.DateField()

