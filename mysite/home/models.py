from django.db import models

# Create your models here.



class Prisoner(models.Model):
    pid= models.IntegerField()
    name= models.CharField(max_length=50)
    EnteranceDate = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    ReleaseDate = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    SecurityLevel = models.CharField(max_length=50)
    cellSharing = models.CharField( max_length=50)
    CurrentDate = models.DateTimeField((""), auto_now=False, auto_now_add=False)

    def __str__(self):
       return self.name

class Visitor(models.Model):
    vid= models.IntegerField()
    name= models.CharField(max_length=50)
    gender= models.CharField(max_length=50)
    address= models.CharField( max_length=50)

    def __str__(self):
       return self.name
   



class Guard(models.Model):
    Gid= models.IntegerField()
    name= models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    address= models.CharField( max_length=50)
    shift= models.CharField( max_length=50)

    def __str__(self):
       return self.name       