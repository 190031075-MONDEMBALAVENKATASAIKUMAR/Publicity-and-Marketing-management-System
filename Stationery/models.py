from django.db import models

# Create your models here.
class station(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    where = models.CharField(max_length=100)
    timings = models.CharField(max_length=100)

    def str(self):
        return '%s' % (self.name)