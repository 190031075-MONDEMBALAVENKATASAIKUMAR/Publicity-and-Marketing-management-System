from django.db import models

class samsungp(models.Model):
    image = models.ImageField(upload_to='images/')
    height=models.IntegerField()
    width=models.CharField(max_length=1001)
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    price = models.IntegerField()
    def str(self):
        return '%s' % (self.name)

class realmep(models.Model):
    image = models.ImageField(upload_to='images/')
    height=models.IntegerField()
    width=models.CharField(max_length=1001)
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    price = models.IntegerField()
    def str(self):
        return '%s' % (self.name)

class applep(models.Model):
    image = models.ImageField(upload_to='images/')
    height=models.IntegerField()
    width=models.CharField(max_length=1001)
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    price = models.IntegerField()
    def str(self):
        return '%s' % (self.name)

class epsonp(models.Model):
    image = models.ImageField(upload_to='images/')
    height=models.IntegerField()
    width=models.CharField(max_length=1001)
    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    price = models.IntegerField()
    def str(self):
        return '%s' % (self.name)


class contactu(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=500)
