# This is an example (using cURL syntax) of how to make a Spire Route Forecast API request.
# Please note that the "time", "lat", and "lon" values are ** not realistic ** in this example.
# It can be run from the terminal command-line using:
#
#       ./curl_example_request.sh
#
# JSON response data can then be copy/paste/saved to a local file for further analysis.
# In the `convert_spire_json_to_csv.py` script, the JSON response data is expected to be
# in a local file called `spire_weather_api_reponse.json`.
# You can of course change the code if you would like to name the input file something different.

curl --location 'https://api.wx.spire.com/forecast/route' \
--header 'spire-api-key: DaVrozYhAZbbVJVb37AccvH8PjucQXTe' \
--header 'Content-Type: application/json' \
--data '{
    "route": {"name": "my_example_route", "waypoints": 
        [
            { "time": "2023-04-8T12:00:00", "lat": 40.526101, "lon": -74.039306 },
            { "time": "2023-04-8T13:00:00", "lat": 39.973220, "lon": -71.954218 },
            { "time": "2023-04-8T14:00:00", "lat": 39.485893, "lon": -66.749471 },
            { "time": "2023-04-8T15:00:00", "lat": 37.434774, "lon": -53.753772 },
            { "time": "2023-04-8T16:00:00", "lat": 36.693392, "lon": -42.424287 }
        ]
    },
    "bundles": "basic,maritime"
}'