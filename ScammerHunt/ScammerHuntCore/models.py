SOURCE_TYPE = (
    ( 'TWITTER', 'TWITTER'),
)

from django.db import models

class Keywords(models.Model):
    name = models.CharField(max_length=300, default='')

class UPI(models.Model):
    id = models.CharField(max_length=300, default='', primary_key=True)

class PriorityUser(models.Model):
    username = models.CharField(max_length=300, default='')

# Mainly tweets
class ScrapeData(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['reference_link',]),
        ]

    text_data = models.TextField()
    score = models.IntegerField(default=0)
    sentiment_score = models.FloatField(default=0.0)
    scammer = models.ManyToManyField("Scammer")
    reference_link = models.TextField(default='', primary_key=True, unique=True)
    reply_count = models.IntegerField(default=0)
    retweet_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    keywords = models.ManyToManyField(Keywords)
    mentioned_users = models.ManyToManyField(PriorityUser, related_name="data_mentioned_users")
    source = models.CharField(default='TWITTER', choices=SOURCE_TYPE, max_length=50)

class Scammer(models.Model):
    name = models.CharField(max_length=300, default='')
    phone_number = models.CharField(max_length=300, primary_key=True)
    email = models.CharField(max_length=300, default='')
    timezone = models.CharField(max_length=300, default='')
    carrier = models.CharField(max_length=300, default='')
    geocoder = models.CharField(max_length=300, default='')
    upi_ids = models.ManyToManyField("UPI", null=True, default=None)
