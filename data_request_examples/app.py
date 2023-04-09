from flask import Flask, request, jsonify
from flask_cors import CORS
from TimeLatLonRequest import TimeLatLonRequest
import TimeLatLonRequest as Body



app = Flask(__name__)
CORS(app)

@app.route('/send_data', methods=['POST'])
def receive_data():
    data = request.get_json()

    # Call your existing script functions and pass the data
    Body.your_function(data)

    return jsonify({"message": "Data received successfully."})

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/playlist-url', methods=['GET'])
def get_playlist_url():
    url = TimeLatLonRequest.get_playlist_url() # Assuming you have created a function to get the playlist URL
    return jsonify({'url': url})

if __name__ == '__main__':
    app.run(debug=True)
