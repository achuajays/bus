from django.db import models

# Create your models here.
class bus(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    destination = models.CharField(max_length=100)
    v_no = models.IntegerField()


class reg(models.Model):
    bus = models.ForeignKey(bus , on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    addarno = models.BigIntegerField()
    nos = models.IntegerField()



class log(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    


