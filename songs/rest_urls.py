from django.urls import path

from rest_views import *

urlpatterns = [
    path('artists/', ArtistsListView.as_view(), name='artists-list'),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artists-detail'),
    path('albums/', AlbumsListView.as_view(), name='albums-list'),
    path('albums/<int:pk>/', AlbumDetailView.as_view(), name='albums-detail'),
    path('songs/', SongsListView.as_view(), name='songs-list'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='songs-detail'),
    path('users/', UserListView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='users-detail'),
    path('playlists/', PlaylistListView.as_view(), name='playlists-list'),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlists-detail'),
    path('interactions/', InteractionListView.as_view(), name='interactions-list'),
    path('interactions/<int:pk>/', InteractionDetailView.as_view(), name='interactions-detail'),
]
