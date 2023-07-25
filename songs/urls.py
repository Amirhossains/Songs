from django.urls import path

from .views import artists_list_view, artist_detail_view, albums_list_view, album_detail_view, songs_list_view, \
    song_detail_view, users_list_view, user_detail_view, playlists_list_view, playlist_detail_view, \
    interactions_list_view, interaction_detail_view

urlpatterns = [
    path('artists/', artists_list_view),
    path('artists/<int:pk>/', artist_detail_view),
    path('albums/', albums_list_view),
    path('albums/<int:pk>/', album_detail_view),
    path('songs/', songs_list_view),
    path('songs/<int:pk>/', song_detail_view),
    path('users/', users_list_view),
    path('users/<int:pk>/', user_detail_view),
    path('playlists/', playlists_list_view),
    path('playlists/<int:pk>/', playlist_detail_view),
    path('interactions/', interactions_list_view),
    path('interactions/<int:pk>/', interaction_detail_view)
]
