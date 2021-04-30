from rest_framework import serializers
from audio.models import AudioBook, Song, Participants, Podcast

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = [field.name for field in model._meta.fields]
        depth = 1

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = [field.name for field in model._meta.fields]
        depth = 1

class AudioBookSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(queryset=Participants.objects.all(),source = 'author', write_only=True)
    narrator_id = serializers.PrimaryKeyRelatedField(queryset=Participants.objects.all(),source = 'narrator', write_only=True)

    class Meta:
        model = AudioBook
        fields = [field.name for field in model._meta.fields]
        fields.extend(['author_id', 'narrator_id'])
        depth = 1

        def update(self, instance, validated_data):
            
            instance.name = validated_data.get('name', instance.name)
            instance.duration = validated_data.get('duration', instance.duration)
            instance.uploaded = validated_data.get('uploaded', instance.uploaded)
            instance.author = validated_data.get('author', instance.author)
            instance.narrator = validated_data.get('narrator', instance.narrator)
            instance.save()
            return instance



class PodcastSerializer(serializers.ModelSerializer):
    host_id = serializers.PrimaryKeyRelatedField(queryset=Participants.objects.all(),source = 'host', write_only=True)
    participants_id = serializers.PrimaryKeyRelatedField(queryset=Participants.objects.all(),source = 'participants', write_only=True, many = True,required = False)
    participants = ParticipantSerializer(read_only = True, many = True)
    class Meta:
        model = Podcast
        fields = [field.name for field in model._meta.fields]
        fields.extend(['host_id', 'participants_id','participants'])
        depth = 1

    #POST
    def create(self, validated_data):
        if validated_data.get("participants"):
            participants = validated_data.pop('participants')

            podcast = Podcast.objects.create(**validated_data)

            podcast.participants.set(participants)
        else:
            podcast = Podcast.objects.create(**validated_data)
        return podcast

    #PATCH
    def update(self, instance, validated_data):
        if validated_data.get("participants"):
            participants = validated_data.pop('participants')
            for participant in participants:
                instance.participants.add(participant)

        instance.host = validated_data.get('host', instance.host)
        instance.name = validated_data.get('name', instance.name)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance