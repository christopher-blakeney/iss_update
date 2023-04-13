#!/usr/bin/env python3

import requests
import json
from datetime import datetime
from geopy.geocoders import Nominatim
import time

"""
MILESTONES
------------------------------------------------------------------------------------------
• 
------------------------------------------------------------------------------------------
TODO
• 
"""

__author__ = "Christopher J. Blakeney"
__version__ = "0.1.0"
__license__ = ""


def jprint(obj):
    # create formatted string of python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_add(lat, lon):
    # returns an address from latitude and longitude
    coordinates = f"{lat}, {lon}"
    time.sleep(1)
    try:
        return geolocator.reverse(coordinates).raw
    except:
        return get_add(lat, lon)


def main():
    # generate current timestamp
    date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # get request for number of people in space & their information
    request = requests.get("http://api.open-notify.org/astros.json")
    people = request.json()
    n_in_space = people["number"]

    # calculate how many aboard ISS
    n_in_iss = 0
    in_iss = []
    for person in people["people"]:
        if person["craft"] == "ISS":
            n_in_iss += 1
            in_iss.append(person["name"])

    # find current lat and long of ISS
    request2 = requests.get("http://api.open-notify.org/iss-now.json")
    loc = request2.json()
    lat = loc["iss_position"]["latitude"]
    lon = loc["iss_position"]["longitude"]

    print(
        f"\nAs of {date_time}"
        f"\nThe International Space Station is at:"
        f"\n    latitude {lat}"
        f"\n    longitude {lon}"
        f"\n\n{n_in_space} people in space\n"
        f"{n_in_iss} aboard the ISS:"
    )
    for name in in_iss:
        print(f"    {name}")
    print("\n")


if __name__ == "__main__":
    main()
