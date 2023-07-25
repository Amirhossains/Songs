from rest_framework import serializers

from models import *


class ArtistsListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artists
        fields = ['id', 'name', 'url']


class ArtistDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ['id', 'name', 'image']


class AlbumsListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Albums
        fields = ['id', 'artist', 'name', 'url']


class AlbumDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = ['id', 'artist', 'name', 'cover']


class SongsListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Songs
        fields = ['id', 'artist', 'album', 'title', 'track', 'url']


class SongsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ['id', 'artist', 'album', 'title', 'length', 'track', 'disc', 'lyrics', 'path', 'mtime']


class UsersListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'email', 'is_admin', 'url']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'name', 'password', 'email', 'is_admin', 'preferences', 'remember_token']


class PlaylistListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlists
        fields = ['id', 'song', 'user', 'name', 'url']


class PlaylistDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlists
        fields = ['id', 'song', 'user', 'name', 'rules']


class InteractionListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interactions
        fields = ['id', 'user', 'song', 'liked', 'url']


class InteractionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interactions
        fields = ['id', 'user', 'song', 'liked', 'play_count', 'created_at']
