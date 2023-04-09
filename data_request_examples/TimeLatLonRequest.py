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
print(input1)

payload = json.dumps(
    {
        "route": {
            "name": "my_example_route",
            "waypoints": [
                {"time": input1, "lat": latitude, "lon": longitude},
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
spire_string = response1.text
windSpeedIndex = spire_string.find("wind_speed") + 12
temperatureIndex = spire_string.find("air_temperature") + 17
precipiationIndex = spire_string.find("precipitation_rate") + 20
cloudCoverIndex = spire_string.find("total_cloud_cover") + 19
humidityIndex = spire_string.find("relative_humidity") + 19
wind_speed = ""
air_temperature = ""
precipitation_rate = ""
total_cloud_cover = ""
relative_humidity = ""
while(spire_string[windSpeedIndex] != '}'):
    wind_speed += spire_string[windSpeedIndex]
    windSpeedIndex += 1
while(spire_string[temperatureIndex] != ','):
    air_temperature += spire_string[temperatureIndex]
    temperatureIndex += 1
while(spire_string[precipiationIndex] != ','):
    precipitation_rate += spire_string[precipiationIndex]
    precipiationIndex += 1
while(spire_string[cloudCoverIndex] != ','):
    total_cloud_cover += spire_string[cloudCoverIndex]
    cloudCoverIndex += 1
while(spire_string[humidityIndex] != ','):
    relative_humidity += spire_string[humidityIndex]
    humidityIndex += 1

# print(response1.text)
# print("Wind speed:",wind_speed)
# print("temperature:", air_temperature)
# print("precipitation:", precipitation_rate)
# print("Cloud cover:", total_cloud_cover)
# print("humidity:",relative_humidity)


airTempF = (1.8 * (float(air_temperature)-273.15)) + 32
print(airTempF)
