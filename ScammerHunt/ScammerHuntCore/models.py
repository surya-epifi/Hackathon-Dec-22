SOURCE_TYPE = (
    ( 'TWITTER', 'TWITTER'),
)

from django.db import models

# Mainly tweets
class ScrapeData(models.Model):
    text_data = models.TextField()
    score = models.IntegerField()
    scammer = models.ForeignKey("Scammer", on_delete=models.CASCADE)
    reference_link = models.TextField()
    keywords = models.ManyToManyField("Keywords")
    mentioned_users = models.ManyToManyField("PriorityUser")
    source = models.CharField(default='TWITTER', choices=SOURCE_TYPE, max_length=50)

class Scammer(models.Model):
    name = models.CharField(max_length=300, default='')
    phone_number = models.CharField(max_length=300)
    email = models.CharField(max_length=300, default='')

class Keywords(models.Model):
    name = models.CharField(max_length=300, default='')

class PriorityUser(models.Model):
    user_name = models.CharField(max_length=300, default='')