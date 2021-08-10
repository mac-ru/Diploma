from django.db import models

# Create your models here.

class cdata(models.Model):
        cd = models.CharField(max_length=50,default='',unique='True',primary_key='True')
        code = models.CharField(max_length=3,default='')
        date = models.CharField(max_length=50,default='')
        confirmed = models.IntegerField(default=0)
        deaths = models.IntegerField(default=0)
        stringency_actual = models.CharField(max_length=50,default='',null='True')
        stringency = models.CharField(max_length=50,default='',null='True')

class cntr(models.Model):
        name = models.CharField(max_length=3,default='')

        def __str__(self):
                return self.name

