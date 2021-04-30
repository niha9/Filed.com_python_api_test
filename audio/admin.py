from django.contrib import admin
from audio.models import Participants, AudioBook, Podcast, Song

admin.site.register(Participants)
admin.site.register(AudioBook)
admin.site.register(Podcast)
admin.site.register(Song)

# Register your models here.
