# This script takes a JSON data file input and converts it to a CSV file.
# It can be run from the terminal command-line using:
#
#       python convert_spire_json_to_csv.py
#
import json
import csv


def get_json_data(inputfile):
    """
    A function for loading the Spire Weather Route Forecast API response data
    that has been stored in JSON format in the same directory as this script
    """
    with open(inputfile) as jsonfile:
        response = json.load(jsonfile)
        return response["data"]


# This is where the script starts:
if __name__ == "__main__":
    # Set the input filename where the Spire Weather data is stored
    inputfile = "spire_weather_api_reponse.json"
    # Set the output filename
    outputfile = "my_output.csv"
    # Print to indicate the script has started
    print("\nConverting `{}` from JSON to CSV:".format(inputfile))
    # Load the weather data that has been saved in JSON format
    data = get_json_data(inputfile)
    # Set up the CSV writer
    with open(outputfile, "w") as csvfile:
        # Create the CSV header
        header = [
            "time",
            "latitude",
            "longitude",
            "wind_gust",
            "wind_speed",
            "wind_direction",
            "surface_visibility",
            "air_pressure_at_sea_level",
            "air_temperature",
            "dew_point_temperature",
            "relative_humidity",
            "surface_visibility",
            "total_cloud_cover",
            "precipitation_rate",
            "sea_water_speed",
            "sea_water_direction",
            "sea_surface_wave_significant_height",
            "sea_surface_wave_mean_direction",
            "sea_surface_wave_mean_period",
        ]
        # Initialize the CSV writer
        writer = csv.DictWriter(csvfile, fieldnames=header)
        # Write the CSV header
        writer.writeheader()
        # Progress counter
        i = 1
        # Write CSV rows
        for d in data:
            # Parse the time and geo-coordinate from the JSON data
            # and add them to the CSV output row
            row = {
                "time": d["times"]["valid_time"],
                "latitude": d["location"]["coordinates"]["lat"],
                "longitude": d["location"]["coordinates"]["lon"],
            }
            # Iterate through the weather data values in the JSON data
            for key, value in d["values"].items():
                # Check if the weather field is in the `header` list above
                if key in header:
                    # Add the weather field to the data row
                    row[key] = value
            # Write the data row to the CSV output file
            writer.writerow(row)
            # Print an indication of the script's current progress
            print("\tWriting row {}/{}...".format(i, len(data)))
            # Increment progress counter
            i += 1
    # Print to indicate the script has completed
    print("Data saved to: `{}`\n".format(outputfile))
