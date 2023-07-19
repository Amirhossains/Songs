from django.db import models


class Artists(models.Model):
    name = models.CharField(verbose_name="name", max_length=32)
    image = models.CharField(verbose_name="image", max_length=32, blank=True)
    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)

    class Meta:
        db_table = "artists"
        verbose_name = "artist"
        verbose_name_plural = "artists"

    def __str__(self):
        return f'{self.name} {self.image}'


class Albums(models.Model):
    artist = models.ForeignKey(to="artists", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="name", max_length=20)
    cover = models.CharField(verbose_name="cover", max_length=32)
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated at", auto_now=True)

    class Meta:
        db_table = "albums"
        verbose_name = "album"
        verbose_name_plural = "albums"

    def __str__(self):
        return f'{self.artist} {self.name}'


class Songs(models.Model):
    album = models.ForeignKey(to="albums", on_delete=models.CASCADE)
    artist = models.ForeignKey(to="artists", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="title", max_length=20)
    length = models.FloatField(verbose_name="length", max_length=10)
    track = models.IntegerField(verbose_name="track", blank=True)
    disc = models.IntegerField(verbose_name="disc")
    lyrics = models.TextField(verbose_name="lyrics")
    path = models.TextField(verbose_name="path")
    mtime = models.IntegerField(verbose_name="mtime")
    created_at = models.DateTimeField("created_at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)

    class Meta:
        db_table = "songs"
        verbose_name = "song"
        verbose_name_plural = "songs"

    def __str__(self):
        return f'{self.album} {self.artist} {self.title}'


class Users(models.Model):
    name = models.CharField(verbose_name="Name", max_length=15)
    email = models.CharField(verbose_name="Email", max_length=30)
    password = models.CharField(verbose_name="password", max_length=20)
    is_admin = models.BooleanField(verbose_name="is admin")
    preferences = models.TextField(verbose_name="preferences", blank=True)
    remember_token = models.CharField(verbose_name="remember token", max_length=30, blank=True)
    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)

    class Meta:
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f'{self.name} {self.email}'


class Playlists(models.Model):
    user = models.ForeignKey(to="users", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="name", max_length=15)
    rules = models.TextField(verbose_name="rules", blank=True)
    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)

    class Meta:
        db_table = "playlists"
        verbose_name = "playlist"
        verbose_name_plural = "playlists"

    def __str__(self):
        return f'{self.user} {self.name}'


class Playlist_song(models.Model):
    playlist = models.ForeignKey(to="playlists", on_delete=models.CASCADE)
    song = models.ForeignKey(to="songs", on_delete=models.CASCADE)

    class Meta:
        db_table = "playlist_song"
        verbose_name = "playlist_song"
        verbose_name_plural = "playlist_songs"

    def __str__(self):
        return f'{self.playlist} {self.song}'


class Interactions(models.Model):
    user = models.ForeignKey(to="users", on_delete=models.CASCADE)
    song = models.ForeignKey(to="songs", on_delete=models.CASCADE)
    liked = models.BooleanField(verbose_name="liked", default=False)
    play_count = models.IntegerField(verbose_name="play count")
    created_at = models.DateTimeField(verbose_name="created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated at", auto_now=True)

    class Meta:
        db_table = "interactions"
        verbose_name = "interaction"
        verbose_name_plural = "interactions"

    def __str__(self):
        return f'{self.user} {self.song} {self.liked} {self.play_count}'
