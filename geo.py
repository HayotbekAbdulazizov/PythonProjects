from geopy import GoogleV3

place = "221 b Baker Street, London"
location = GoogleV3().geocode(place)

print(location.address)
print(location.location)
