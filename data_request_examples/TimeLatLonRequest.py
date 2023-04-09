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
from datetime import date
from datetime import datetime

url = "https://api.wx.spire.com/forecast/route"
today = date.today()
now = datetime.now()
dt_string = now.strftime("%H:%M:%S")
input1 = str(today) + "T" + str(dt_string)

payload = json.dumps(
    {
        "route": {
            "name": "my_example_route",
            "waypoints": [
                {"time": input1, "lat": 60, "lon": 60},
            ],
        },
        "bundles": "basic,maritime",
    }
)
headers = {
    "spire-api-key": "DaVrozYhAZbbVJVb37AccvH8PjucQXTe",
    "Content-Type": "application/json",
}
response1 = requests.request("POST", url, headers=headers, data=payload)
# print(response.text)

x = input()
zip = str(x)
response = requests.get('https://thezipcodes.com/api/v1/search?zipCode=' + zip + '&countryCode=US&apiKey=ded7388190c42055780b299ec6c41b14')
json_string = response.text

latIndex = json_string.find("latitude") + 11
latitude = ""
while(json_string[latIndex] != '"'):
    latitude += json_string[latIndex]
    latIndex += 1


longIndex = json_string.find("longitude")  + 12
longitude = ""
while(json_string[longIndex] != '"'):
    longitude += json_string[longIndex]
    longIndex += 1

print(latitude, longitude) 


