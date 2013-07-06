from geopy import geocoders as gc
import pickle
import csv

langauge = 'python'

locations = open(langauge + '-countries.txt', 'rb') #read countries from txt file
out = csv.writer(open(langauge + '-placemark.csv', 'wb')) # write placemarks to csv file

countries = pickle.load(locations)

g = gc.GoogleV3()

for country in countries:
    try:
        placemark = g.geocode(country)
        out.writerow([placemark[0], placemark[1][0], placemark[1][1]])
    except:
        out.writerow(country)
