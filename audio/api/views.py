from rest_framework import status, viewsets
from audio.models import AudioBook, Song, Participants, Podcast
from audio.api.serializers import SongSerializer, ParticipantSerializer, AudioBookSerializer, PodcastSerializer

class AudioBookViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        types = self.request.GET.get('type')
        if types == 'song':
            return Song.objects.all()
        elif types == 'audiobook':
            return AudioBook.objects.all()
        elif types == 'podcast':
            return Podcast.objects.all()
    
    def get_serializer_class(self):
        types = self.request.GET.get('type')
        if types == 'song':
            return SongSerializer
        elif types == 'audiobook':
            return AudioBookSerializer
        elif types == 'podcast':
            return PodcastSerializer

    
    lookup_field = 'id'
    """
    queryset = AudioBook.objects.all()
    serializer_class = AudioBookSerializer
    lookup_field = 'id'

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'id'

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    lookup_field = 'id'

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participants.objects.all()
    serializer_class = ParticipantSerializer
    lookup_field = 'id'"""
