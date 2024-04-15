from lib.album_repository import *
from lib.album import *
from lib.database_connection import DatabaseConnection

connection = DatabaseConnection()
connection.connect()

connection.seed("seeds/music_library.sql")

album_repository = AlbumRepository(connection)
albums = album_repository.all()

for album in albums:
    print(album)