from django.http import Http404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ArtistsListSerializer, ArtistDetailSerializer, AlbumsListSerializer, AlbumDetailSerializer, \
    SongsListSerializer, SongsDetailSerializer, UsersListSerializer, UserDetailSerializer, PlaylistListSerializer, \
    PlaylistDetailSerializer, InteractionListSerializer, InteractionDetailSerializer
from .models import *


class ArtistsListView(APIView):

    def get(self, request):
        artists = Artists.objects.all()
        serializer = ArtistsListSerializer(artists, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArtistDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArtistDetailView(APIView):

    def get(self, request, pk):
        try:
            artist = Artists.objects.get(pk=pk)
        except Artists.DoesNotExist:
            return Http404
        serializer = ArtistDetailSerializer(artist, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            artist = Artists.objects.get(pk=pk)
        except Artists.DoesNotExist:
            return Http404
        serializer = ArtistDetailSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            artist = Artists.objects.get(pk=pk)
        except Artists.DoesNotExist:
            return Http404
        artist.delete()
        return Response({'detail', 'The artist deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class AlbumsListView(APIView):

    def get(self, request):
        albums = Albums.objects.all()
        serializer = AlbumsListSerializer(albums, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AlbumDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetailView(APIView):

    def find(self, pk):
        try:
            a = Albums.objects.get(pk=pk)
        except Albums.DoesNotExist:
            raise Http404
        return a

    def get(self, request, pk):
        album = self.find(pk)
        serializer = AlbumDetailSerializer(album)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        album = self.find(pk)
        serializer = AlbumDetailSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        album = self.find(pk)
        album.delete()
        return Response({'detail': 'The album deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class SongsListView(APIView):

    def get(self, request):
        songs = Songs.objects.all()
        serializer = SongsListSerializer(songs, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SongsDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongDetailView(APIView):

    def find(self, pk):
        try:
            a = Songs.objects.get(pk=pk)
        except Songs.DoesNotExist:
            raise Http404
        return a

    def get(self, request, pk):
        song = self.find(pk)
        serializer = SongsDetailSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        song = self.find(pk)
        serializer = SongsDetailSerializer(song, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        song = self.find(pk)
        song.delete()
        return Response({'detail': 'The song deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class UserListView(APIView):

    def get(self, request):
        users = Users.objects.all()
        serializer = UsersListSerializer(users, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):

    def find(self, pk):
        try:
            a = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404
        return a

    def get(self, request, pk):
        user = self.find(pk)
        serializer = UserDetailSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user = self.find(pk)
        serializer = UserDetailSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.find(pk)
        user.delete()
        return Response({'detail': 'user deleted successfully.'})


class PlaylistListView(APIView):

    def get(self, request):
        playlist = Playlists.objects.all()
        serializer = PlaylistListSerializer(playlist, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PlaylistDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlaylistDetailView(APIView):

    def find(self, pk):
        try:
            a = Playlists.objects.get(pk=pk)
        except Playlists.DoesNotExist:
            raise Http404
        return a

    def get(self, request, pk):
        playlist = self.find(pk)
        serializer = PlaylistDetailSerializer(playlist)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        playlist = self.find(pk)
        serializer = PlaylistDetailSerializer(playlist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        playlist = self.find(pk)
        playlist.delete()
        return Response({'detail': 'The playlist deleted successfully.'})


class InteractionListView(APIView):

    def get(self, request):
        interaction = Interactions.objects.all()
        serializer = InteractionListSerializer(interaction, many=True, context={"request": request})
        return Response(data=serializer.data)

    def post(self, request):
        serializer = InteractionDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InteractionDetailView(APIView):

    def find(self, pk):
        try:
            a = Interactions.objects.get(pk=pk)
        except Interactions.DoesNotExist:
            raise Http404
        return a

    def get(self, request, pk):
        interaction = self.find(pk)
        serializer = InteractionDetailSerializer(interaction)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        interaction = self.find(pk)
        serializer = InteractionDetailSerializer(interaction, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        interaction = self.find(pk)
        interaction.delete()
        return Response({'detail': 'The interaction deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
