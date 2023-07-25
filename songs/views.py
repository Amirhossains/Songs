from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import Artists, Albums, Songs, Users, Playlists, Interactions


@api_view(["GET", "POST"])
def artists_list_view(request):
    artists_list = []
    qs = Artists.objects.all()
    for i in qs:
        artists = {"id": i.id, "name": i.name}
        artists_list.append(artists)
    return Response({"artists": artists_list})


@api_view(["GET"])
def artist_detail_view(request, pk):
    try:
        qs = Artists.objects.get(pk=pk)
    except Artists.DoesNotExist:
        return JsonResponse({"detail": "404 error"})
    artist = model_to_dict(qs)
    return Response(artist)


def albums_list_view(request):
    albums_list = []
    qs = Albums.objects.all()
    for i in qs:
        albums = {"id": i.id, "artist": str(i.artist), "name": i.name}
        albums_list.append(albums)
    return JsonResponse({"albums": albums_list})


def album_detail_view(request, pk):
    try:
        qs = Artists.objects.get(pk=pk)
    except Artists.DoesNotExist:
        return JsonResponse({"detail": "404 error"})
    album = model_to_dict(qs)
    return JsonResponse(album)


def songs_list_view(request):
    songs_list = []
    qs = Songs.objects.all()
    for i in qs:
        songs = {"id": i.id, "album": str(i.album), "artist": str(i.artist), "title": i.title, "track": i.track,
                 "lyrics": i.lyrics}
        songs_list.append(songs)
    return JsonResponse({"songs": songs_list})


def song_detail_view(request, pk):
    try:
        qs = Songs.objects.get(pk=pk)
    except Songs.DoesNotExist:
        return JsonResponse({"detail": "404 error"})
    song = model_to_dict(qs)
    return JsonResponse(song)


def users_list_view(request):
    users_list = []
    qs = Users.objects.all()
    for i in qs:
        users = {"id": i.id, "name": i.name, "email": i.email}
        users_list.append(users)
    return JsonResponse({"users": users_list})


def user_detail_view(request, pk):
    try:
        qs = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return JsonResponse({"detail": "404 error"})
    user = model_to_dict(qs)
    return JsonResponse(user)


def playlists_list_view(request):
    playlists_list = []
    qs = Playlists.objects.all()
    for i in qs:
        playlist = {"id": i.id, "user": str(i.user), "name": i.name}
        playlists_list.append(playlist)
    return JsonResponse({"playlists": playlists_list})


def playlist_detail_view(request, pk):
    try:
        qs = Playlists.objects.get(pk=pk)
    except Playlists.DoesNotExist:
        return JsonResponse({"detail": "404 error"})
    playlist = model_to_dict(qs)
    return JsonResponse(playlist)


def interactions_list_view(request):
    interactions_list = []
    qs = Interactions.objects.all()
    for i in qs:
        interaction = {"id": i.id, "user": str(i.user), "song": str(i.song)}
        interactions_list.append(interaction)
    return JsonResponse({"interactions": interactions_list})


def interaction_detail_view(request, pk):
    try:
        qs = Interactions.objects.get(pk=pk)
    except Interactions.DoesNotExist:
        return JsonResponse({"detail": "404 error"})
    interaction = model_to_dict(qs)
    return JsonResponse(interaction)
