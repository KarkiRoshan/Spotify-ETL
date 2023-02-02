from dotenv import load_dotenv
import os 
import spotipy
import json
import pandas as pd 
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()

def extraction():
    spotify_redirect_url = "http://localhost:8000"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('CLIENT_ID'),
                                                   client_secret=os.getenv('CLIENT_SECRET'),
                                                   redirect_uri=spotify_redirect_url,
                                                   scope="user-read-recently-played"))
    recently_played = sp.current_user_recently_played(limit=50)
    album_id = []
    album_name = []
    total_tracks = []
    album_link = []
    album_release_date = []
    for item in recently_played['items']:
        album_id.append(item['track']['album']['id'])
        album_name.append(item['track']['album']['name'])
        total_tracks.append(item['track']['album']['total_tracks'])
        album_release_date.append(item['track']['album']['release_date'])
        album_link.append(item['track']['album']['external_urls']['spotify'])
    album_dict = {'album_id':album_id,'album_name':album_name,'date_time':album_release_date,'total_tracks':total_tracks,'album_link':album_link}
    album_df = pd.DataFrame.from_dict(album_dict)
    artist_id = []
    artist_name = []
    artist_url = []
    for item in recently_played['items']:
        for artist in item['track']['album']['artists']:
            # print(artist['id'])
            artist_id.append(artist['id'])
            artist_name.append(artist['name'])
            artist_url.append(artist['external_urls']['spotify'])
    artist_dict = {'artist_id':artist_id,'artist':artist_name,'artist_url':artist_url}
    artist_df = pd.DataFrame.from_dict(artist_dict)
    song_name = []
    song_id = []
    song_duration = []
    song_url = []
    song_popularity = []
    song_played_at = []
    song_album_id = []
    song_artist_name = []
    for song in recently_played['items']:
        song_name.append(song['track']['name'])
        song_id.append(song['track']['id'])
        song_duration.append(song['track']['duration_ms'])
        song_url.append(song['track']['external_urls']['spotify'])
        song_popularity.append(song['track']['popularity'])
        song_played_at.append(song['played_at'])
        song_album_id.append(song['track']['album']['id'])
        song_artist_name.append(song['track']['album']['artists'][0]['name'])
    song_dict = {'song_name':song_name,'song_id':song_id,'song_duration':song_duration,'song_url':song_url,'song_popularity':song_popularity,
                'song_played_at':song_played_at,'song_album_id':song_album_id,'song_artist_name':song_artist_name}
    song_df = pd.DataFrame.from_dict(song_dict)        
extraction()                                   
