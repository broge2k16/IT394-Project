import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Game(models.Model):
    homeTeam = models.CharField(max_length=30)
    awayTeam = models.CharField(max_length=30)
    gameDate = models.CharField(max_length=15)
    gameTime = models.CharField(max_length=15)
    gameScore = gameDate = models.CharField(max_length=15)
    sportID = models.ForeignKey(Sport, on_delete=models.CASCADE)
    locationID = models.ForeignKey(Location, on_delete=models.CASCADE)

class Location(models.Model):
    campusLocation = models.CharField(max_length=30)
    stadiumName = models.CharField(max_length=30)

class Sport(models.Model):
    genderCategory = models.CharField(max_length=15)
    sportName = models.CharField(max_length=15)

class Player(models.Model):
    lastName = models.CharField(max_length=15)
    firstName = models.CharField(max_length=15)
    playerPosition = models.CharField(max_length=15)
    sportID = models.ForeignKey(Sport, on_delete=models.CASCADE)

'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
        
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
class Choice(models.Model):
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
'''
