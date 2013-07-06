import csv
import pickle

language = 'python'

lines = csv.reader(open(language + '.csv', 'rb'))

out = open(language + '-countries.txt', 'wb')

locations = []

for line in lines:
    locations.append(line[1])

pickle.dump(locations, out)
