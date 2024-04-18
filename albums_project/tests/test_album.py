from lib.album import *

"""
constructs with 
id, title, release_year, and artist_id
"""

def test_constructs_with_fields():
    album = Album(1,"Dark Side", 1995, 2)
    assert album.id == 1
    assert album.title == "Dark Side"
    assert album.release_year == 1995
    assert album.artist_id == 2

def test_artists_are_equal():
    album1 = Album(1, "Dark Side", 1995, 2)
    album2 = Album(1, "Dark Side", 1995, 2)
    assert album1 == album2

def test_album_format_nicely():
    album = Album(1, "title", "release_year", "artist_id")
    assert str(album) == "Album(1, title,release_year, artist_id)"
