3.UML Diagram to Create a music player web app using html, oops, typescript and bootstrap with the following features and convert them into python class and methods.

class Song:
    def __init__(self, title, artist, album, duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration

    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist.get_name()

    def get_album(self):
        return self.album.get_details()

    def get_duration(self):
        return self.duration


class Artist:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Album:
    def __init__(self, title, artist, release_year):
        self.title = title
        self.artist = artist
        self.release_year = release_year

    def get_details(self):
        return f"{self.title} by {self.artist.get_name()}, {self.release_year}"


class Genre:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_song = None
        self.is_playing = False

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        self.playlist.remove(song)

    def play(self):
        self.is_playing = True
        # Add logic to start playing the current song

    def pause(self):
        self.is_playing = False
        # Add logic to pause the current song

    def next(self):
        # Add logic to play the next song in the playlist
        pass

    def previous(self):
        # Add logic to play the previous song in the playlist
        pass
