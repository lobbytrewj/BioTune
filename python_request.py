# This is an example (using cURL syntax) of how to make a Spire Route Forecast API request.
# Please note that the "time", "lat", and "lon" values are ** not realistic ** in this example.
# It can be run from the terminal command-line using:
#
#       python python_example_request.py
#
# JSON response data can then be copy/paste/saved to a local file for further analysis.
# In the `convert_spire_json_to_csv.py` script, the JSON response data is expected to be
# in a local file called `spire_weather_data.json`.
# You can of course change the code if you would like to name the input file something different.

import requests
import json

url = "https://api.wx.spire.com/forecast/route"
payload = json.dumps(
    {
        "route": {
            "name": "my_example_route",
            "waypoints": [
                {"time": "2023-04-8T12:00:00", "lat": 40.526101, "lon": -74.039306},
            ],
        },
        "bundles": "basic,maritime",
    }
)
headers = {
    "spire-api-key": "DaVrozYhAZbbVJVb37AccvH8PjucQXTe",
    "Content-Type": "application/json",
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
