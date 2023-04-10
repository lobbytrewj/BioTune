from flask import Flask, request, jsonify
from flask_cors import CORS
from TimeLatLonRequest import TimeLatLonRequest
import TimeLatLonRequest as Body

app = Flask(__name__)
CORS(app)

@app.route('/send_data', methods=['POST'])
def send_data():
    data = request.get_json()
    print(data)
    response = jsonify({'message': 'Data received successfully'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response, 200
if __name__ == '__main__':
    app.run(debug=True, port=3000)


@app.route('/playlist-url', methods=['GET'])
def get_playlist_url():
    ##url = TimeLatLonRequest.get_playlist_url() # Assuming you have created a function to get the playlist URL
    ##return jsonify({'url': url})
    url = TimeLatLonRequest.get_playlist_url() # Assuming you have created a function to get the playlist URL
    response = jsonify({'url': url})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response, 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
