from django.db import models
from django.contrib.auth.models import User


class Nation(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField()
    
    industry = models.IntegerField()
    economy = models.IntegerField()
    social_freedom = models.IntegerField()
    political_freedom = models.IntegerField()
    religion = models.IntegerField()
    education = models.IntegerField()
    environment = models.IntegerField()
    employment = models.IntegerField()
    crime = models.IntegerField()
    health = models.IntegerField()
    military = models.IntegerField()
    happiness = models.IntegerField()
    
    motto = models.CharField(max_length=255)
    animal = models.CharField(max_length=63)
    currency = models.CharField(max_length=63)

class Issue(models.Model):
    problem = models.TextField()
    
class Option(models.Model):
    issue = models.ForeignKey(Issue)
    solution = models.TextField()
    
class Ruler(models.Model):
    user = models.ForeignKey(User)
    power = models.IntegerField()
    money = models.IntegerField()
    corruption = models.IntegerField()
    rank = models.IntegerField()
    title = models.CharField(max_length = 63)



            
    