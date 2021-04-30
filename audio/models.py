
# Create your models here.
from django.db import models

class Participants(models.Model):
    name                      = models.CharField(max_length = 150, null=False, blank = False)

    def __str__(self):
        return self.name

class Song(models.Model):
    name                      = models.CharField(max_length = 150, null=False, blank = False)
    duration                  = models.IntegerField(null=False, blank = False)
    uploaded                  = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Podcast(models.Model):
    name                      = models.CharField(max_length = 150, null=False, blank = False)
    duration                  = models.IntegerField(null=False, blank = False)
    uploaded                  = models.DateTimeField(auto_now_add = True)
    host                      = models.ForeignKey('audio.Participants', on_delete=models.SET_NULL,null=True, related_name ="host")
    participants              = models.ManyToManyField('audio.Participants', related_name = "participants")

    def __str__(self):
        return self.name

class AudioBook(models.Model):
    name                      = models.CharField(max_length = 150, null=False, blank = False)
    duration                  = models.IntegerField(null=False, blank = False)
    uploaded                  = models.DateTimeField(auto_now_add = True)
    author                    = models.ForeignKey('audio.Participants', on_delete=models.SET_NULL,null=True, related_name="author")
    narrator                  = models.ForeignKey('audio.Participants', on_delete=models.SET_NULL,null=True, related_name="narrator")

    def __str__(self):
        return self.name
