from flask import Flask, request, jsonify
from flask_cors import CORS
from TimeLatLonRequest import TimeLatLonRequest
import TimeLatLonRequest as Body

'''app = Flask(__name__)
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
'''
from flask import Flask, jsonify, request
from tools import retrieve_info
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):

        data = "hello world"
        return jsonify({'data': data})

@app.route('/get_info', methods = ['GET'])
def disp():
    print(request.args)
    data = retrieve_info(request.args.get("url"))
    
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=43)