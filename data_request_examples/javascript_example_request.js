// This is an example (using JavaScript syntax) of how to make a Spire Route Forecast API request.
// Please note that the "time", "lat", and "lon" values are ** not realistic ** in this example.
// It can be run by:
// 
//    embedding into a web page with HTML/CSS
//
//    OR copy/pasting directly into the browser's JavaScript Developer Console
//
// JSON response data can then be copy/paste/saved to a local file for further analysis.
// In the `convert_spire_json_to_csv.py` script, the JSON response data is expected to be
// in a local file called `spire_weather_data.json`.
// You can of course change the code if you would like to name the input file something different.

var myHeaders = new Headers();
myHeaders.append("spire-api-key", "DaVrozYhAZbbVJVb37AccvH8PjucQXTe");
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "route": {
    "name": "my_example_route",
    "waypoints": [
      {
        "time": "2023-04-8T12:00:00",
        "lat": 40.526101,
        "lon": -74.039306
      },
      {
        "time": "2023-04-8T13:00:00",
        "lat": 39.97322,
        "lon": -71.954218
      },
      {
        "time": "2023-04-8T14:00:00",
        "lat": 39.485893,
        "lon": -66.749471
      },
      {
        "time": "2023-04-8T15:00:00",
        "lat": 37.434774,
        "lon": -53.753772
      },
      {
        "time": "2023-04-8T16:00:00",
        "lat": 36.693392,
        "lon": -42.424287
      }
    ]
  },
  "bundles": "basic,maritime"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://api.wx.spire.com/forecast/route", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));