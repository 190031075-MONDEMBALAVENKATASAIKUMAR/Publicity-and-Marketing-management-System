from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tra(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    link = models.CharField(max_length=100)

    def str(self):
        return '%s' % (self.name)















