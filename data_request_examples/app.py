from flask import Flask, jsonify
from flask_cors import CORS
from TimeLatLonRequest import TimeLatLonRequest
import your_existing_script as your_script


app = Flask(__name__)
CORS(app)

@app.route('/playlist-url', methods=['GET'])
def get_playlist_url():
    url = TimeLatLonRequest.get_playlist_url() # Assuming you have created a function to get the playlist URL
    return jsonify({'url': url})

if __name__ == '__main__':
    app.run(debug=True)
