import pandas as pd
import numpy as np
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

import datetime
now = datetime.datetime.now()

from googleplaces import GooglePlaces, types, lang
import config

api_key = config.gmaps_api

geocoder = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36')
geocode = RateLimiter(geocoder.geocode, min_delay_seconds=1, return_value_on_exception=None)

df = pd.read_csv('data/data1.csv')
df1 = df.drop(['price', 'postcode', 'year', 'latitude', 'longitude', 'distance1',  'distance2', 'city'], axis=1)

ams_avg_distance1 = np.average(df[df['city'] == 'Amsterdam']['distance1'])
dhg_avg_distance1 = np.average(df[df['city'] == 'Den Haag']['distance1'])
ein_avg_distance1 = np.average(df[df['city'] == 'Eindhoven']['distance1'])
rot_avg_distance1 = np.average(df[df['city'] == 'Rotterdam']['distance1'])
utr_avg_distance1 = np.average(df[df['city'] == 'Utrecht']['distance1'])

ams_avg_price = np.average(df[df['city'] == 'Amsterdam']['price'])
dhg_avg_price = np.average(df[df['city'] == 'Den Haag']['price'])
ein_avg_price = np.average(df[df['city'] == 'Eindhoven']['price'])
rot_avg_price = np.average(df[df['city'] == 'Rotterdam']['price'])
utr_avg_price = np.average(df[df['city'] == 'Utrecht']['price'])

def coordinates(postcode):
    location = geocode(postcode)
    return [location.latitude, location.longitude]

def std_distance(latitude, longitude, cityname):
    if cityname == 'Amsterdam':
        point1 = (52.3791, 4.9003) #amsterdam centraal
        distance1 = geodesic((latitude, longitude), point1).km
        std_distance_1 = distance1 / ams_avg_distance1

    if cityname == 'Den Haag':
        point1 = (52.0811, 4.3242) #den haag centraal
        distance1 = geodesic((latitude, longitude), point1).km
        std_distance_1 = distance1 / dhg_avg_distance1

    if cityname == 'Eindhoven':
        point1 = (51.4431, 5.4803)  # eindhoven centraal
        distance1 = geodesic((latitude, longitude), point1).km
        std_distance_1 = distance1 / ein_avg_distance1

    if cityname == 'Rotterdam':
        point1 = (51.9243, 4.4700)  # rotterdam centraal
        distance1 = geodesic((latitude, longitude), point1).km
        std_distance_1 = distance1 / rot_avg_distance1

    if cityname == 'Utrecht':
        point1 = (52.0894, 5.1100) #utrecht centraal
        distance1 = geodesic((latitude, longitude), point1).km
        std_distance_1 = distance1 / utr_avg_distance1

    return std_distance_1

def google_maps_rating(latitude, longitude):
    lat = latitude
    lng = longitude

    google_places = GooglePlaces(api_key=api_key)

    query_result = google_places.nearby_search(
        lat_lng={'lat': lat, 'lng': lng},
        radius=1000,
        types=[types.TYPE_FOOD])

    count1 = 0

    place_rating = []

    while count1 <= len(query_result.places) - 1:
        place = query_result.places[count1]
        try:
            place.get_details()
            reviews = place.details['reviews']

            score = []
            count2 = 0

            while count2 <= len(reviews) - 1:
                score.append(reviews[count2]['rating'])
                count2 += 1

            place_rating.append(np.average(score))

        except:
            place_rating = 0

        count1 += 1

    return np.average(place_rating)

def predict(postcode, size, kamers, year, cityname):

    lat = coordinates(postcode)[0]
    lng = coordinates(postcode)[1]

    newdata = pd.DataFrame().reindex_like(df1)
    newdata.fillna(value=0, inplace=True)
    del newdata['std price']
    newdata = newdata.iloc[[1]]

    newdata['size'] = size
    newdata['kamers'] = kamers
    newdata['age'] = now.year - year
    newdata['nearby rating'] = google_maps_rating(lat, lng)
    newdata['std distance1'] = std_distance(lat, lng, cityname)

    predicted_std_price = rf.predict(newdata)[0]

    if cityname == 'Amsterdam':
        predicted_price = predicted_std_price * ams_avg_price

    if cityname == 'Den Haag':
        predicted_price = predicted_std_price * dhg_avg_price

    if cityname == 'Eindhoven':
        predicted_price = predicted_std_price * ein_avg_price

    if cityname == 'Rotterdam':
        predicted_price = predicted_std_price * rot_avg_price

    if cityname == 'Utrecht':
        predicted_price = predicted_std_price * utr_avg_price

    return predicted_price

predict('1102AA', 20, 1, 2014, 'Amsterdam')

