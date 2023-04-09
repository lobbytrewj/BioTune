import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

client_id = '6bae4451c248407d84e5808925840377'
client_secret = '8d400f2e23ef4a27931e680fd9493db4'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


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
        results = sp.search(q='genre:' + genre, type='track', limit=5)
        for track in results['tracks']['items']:
            track_results.append(track['uri'])
    user = input('Your Username: ')
    sp.user_playlist_create(user, name='High Energy Playlist', public=True, description='Playlist of high energy music')
    sp.user_playlist_add_tracks(user, playlist_id='your_playlist_id', tracks=track_results)

elif playlist_category == 'low energy':
    track_results = []
    for genre in low_energy_music:
        results = sp.search(q='genre:' + genre, type='track', limit=5)
        for track in results['tracks']['items']:
            track_results.append(track['uri'])
    user = input('Your Username: ')
    sp.user_playlist_create(user, name='Low Energy Playlist', public=True, description='Playlist of low energy music')
    sp.user_playlist_add_tracks(user, playlist_id='your_playlist_id', tracks=track_results)

elif playlist_category == 'exciting':
    track_results = []
    for genre in exciting_music:
        results = sp.search(q='genre:' + genre, type='track', limit=5)
        for track in results['tracks']['items']:
            track_results.append(track['uri'])
    user = input('Your Username: ')
    sp.user_playlist_create(user, name='Exciting Playlist', public=True, description='Playlist of exciting music')
    sp.user_playlist_add_tracks(user, playlist_id='your_playlist_id', tracks=track_results)

else:
    print('Invalid playlist category')