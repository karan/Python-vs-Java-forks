import csv 

language = 'python'
lines = csv.reader(open(language + "-data.csv", "rb"))

javas = []

for row in lines:
    lat = row[0]
    lon = row[1]
    intensity = row[3]
    try:
        float(lat)
        float(lon)
        javas += (lat, lon, intensity)
    except:
        pass

print "[[\"Java\", [%s]]]" % (",".join(javas))
