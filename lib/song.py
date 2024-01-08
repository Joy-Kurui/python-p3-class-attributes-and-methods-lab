# class Song:
#     count = 0
#     genres = []
#     artist = []
#     genre_count = {}
#     artist_count = {}
#     def __init__(self, name, artist, genre):
#         self.name = name
#         self.artist = artist
#         self.genre = genre
#         Song.add_song_to_count()
#         Song.add_to_genres()
#         Song.add_to_artists()
#         Song.add_to_genre_count()
#         Song.add_to_artist_count()

#     @classmethod
#     def add_song_to_count(cls, increment=1):
#         cls.count += increment
#     @classmethod
#     def add_to_genres(cls):
#         if cls.genre not in cls.genres:
#             cls.genres.append(cls.genre)
#     @classmethod
#     def add_to_artists(cls):
#         if cls.artist not in cls.artists:
#             cls.artists.append(cls.artist)
#     @classmethod
#     def add_to_genre_count(cls):
#         if cls.genre in cls.genre_count:
#             cls.genre_count[cls.genre] += 1
#         else:
#             cls.genre_count[cls.genre] = 1
#     @classmethod
#     def add_to_artist_count(cls):
#         if cls.artist in cls.artist_count:
#             cls.artist_count[cls.artist] += 1
#         else:
#             cls.artist_count[cls.artist] = 1

class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)  
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    @classmethod
    def add_to_artists(cls, artist):  
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


