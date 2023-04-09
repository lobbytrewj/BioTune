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
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
user = sp.current_user()['id']

# Define playlist categories
high_energy_music = ['techno', 'house', 'hip hop', 'metal', 'rock']
low_energy_music = ['jazz', 'blues', 'classical', 'instrumental', 'ambient']
exciting_music = ['pop', 'dance', 'r&b', 'reggae', 'latin']

# Ask user for input
playlist_category = input('Please select a playlist category - high energy, low energy, or exciting: ')

# Create playlist based on user input
if playlist_category == 'high energy':
    track_results = []
    for genre in high_energy_music:
        offset = random.randint(0, 100)
        results = sp.search(q='genre:' + genre, type='track', limit=5, offset=offset)
        for track in results['tracks']['items']:
            track_results.append(track['uri'])
    playlist = sp.user_playlist_create(user, name='High Energy Playlist', public=True, description='Playlist of high energy music')
    sp.user_playlist_add_tracks(user, playlist_id=playlist['id'], tracks=track_results)

elif playlist_category == 'low energy':
    track_results = []
    for genre in low_energy_music:
        offset = random.randint(0, 100)
        results = sp.search(q='genre:' + genre, type='track', limit=5, offset=offset)
        for track in results['tracks']['items']:
            track_results.append(track['uri'])
    playlist = sp.user_playlist_create(user, name='Low Energy Playlist', public=True, description='Playlist of low energy music')
    sp.user_playlist_add_tracks(user, playlist_id=playlist['id'], tracks=track_results)

elif playlist_category == 'exciting':
    track_results = []
    for genre in exciting_music:
        offset = random.randint(0, 100)
        results = sp.search(q='genre:' + genre, type='track', limit=5, offset=offset)
        for track in results['tracks']['items']:
            track_results.append(track['uri'])
    playlist = sp.user_playlist_create(user, name='Exciting Playlist', public=True, description='Playlist of exciting music')
    sp.user_playlist_add_tracks(user, playlist_id=playlist['id'], tracks=track_results)

else:
    print('Invalid playlist category')