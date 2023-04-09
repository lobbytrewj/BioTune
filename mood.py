import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import random

client_id = '6bae4451c248407d84e5808925840377'
client_secret = '8d400f2e23ef4a27931e680fd9493db4'
client_uri = 'http://localhost:8080/callback'
cache_path = ".cache"
if os.path.exists(cache_path):
    os.remove(cache_path)

scope = 'playlist-modify-public'
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=client_uri, scope=scope, cache_path=None, show_dialog=True)
sp = spotipy.Spotify(auth_manager=auth_manager)

user = sp.current_user()['id']

# Define playlist categories
high_energy_music = ['techno', 'house', 'hip hop', 'metal', 'rock']
low_energy_music = ['blues', 'classical', 'instrumental']
exciting_music = ['pop', 'dance', 'r&b', 'reggae', 'latin']
depressed_music = ['r&b', 'ambient', 'jazz']

# Ask user for input
playlist_category = input('Please select a playlist category - happy, relaxation, hype or depressed: ')

# Create playlist based on user input
if playlist_category == 'happy':
    track_results = []
    for genre in high_energy_music:
        offset = random.randint(0, 100)
        results = sp.search(q='genre:' + genre, type='track', limit=5, offset=offset)
        for track in results['tracks']['items']:
            track_results.append(track['uri'])
    playlist = sp.user_playlist_create(user, name='Happy', public=True, description='Playlist of happiness')
    sp.user_playlist_add_tracks(user, playlist_id=playlist['id'], tracks=track_results)

elif playlist_category == 'relaxation':
    track_results = []
    for genre in low_energy_music:
        offset = random.randint(0, 100)
        results = sp.search(q='genre:' + genre, type='track', limit=5, offset=offset)
        for track in results['tracks']['items']:
            track_results.append(track['uri'])
    playlist = sp.user_playlist_create(user, name='Relaxation', public=True, description='Playlist of relaxation')
    sp.user_playlist_add_tracks(user, playlist_id=playlist['id'], tracks=track_results)

elif playlist_category == 'hype':
    track_results = []
    for genre in exciting_music:
        offset = random.randint(0, 100)
        results = sp.search(q='genre:' + genre, type='track', limit=5, offset=offset)
        for track in results['tracks']['items']:
            track_results.append(track['uri'])
    playlist = sp.user_playlist_create(user, name='Hype', public=True, description='Playlist of hype music')
    sp.user_playlist_add_tracks(user, playlist_id=playlist['id'], tracks=track_results)

elif playlist_category == 'depressed':
    track_results = []
    for genre in depressed_music:
        offset = random.randint(0, 100)
        results = sp.search(q='genre:' + genre, type='track', limit=5, offset=offset)
        for track in results['tracks']['items']:
            track_results.append(track['uri'])
    playlist = sp.user_playlist_create(user, name='Depressed', public=True, description='Playlist of depressing music')
    sp.user_playlist_add_tracks(user, playlist_id=playlist['id'], tracks=track_results)

else:
    print('Invalid playlist category')