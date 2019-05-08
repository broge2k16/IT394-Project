import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Sport(models.Model):
    genderCategory = models.CharField(max_length=15) #make a choose 2
    sportName = models.CharField(max_length=50)
    
    def __str__(self):
        return self.sportName

class Location(models.Model):
    campusLocation = models.CharField(max_length=30)
    venue = models.CharField(max_length=30)
    
    def __str__(self):
        return (self.venue + ", " + self.campusLocation)
    
class Game(models.Model):
    homeTeam = models.CharField(max_length=30)
    awayTeam = models.CharField(max_length=30)
    gameTime = models.DateTimeField()
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def latest_games():
        now = datetime.datetime.now()
        return Game.objects.filter(gameTime__gte=now).order_by('-gameTime')
    






