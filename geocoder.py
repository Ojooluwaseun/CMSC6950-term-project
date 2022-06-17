from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geocoder")

class geocoder:
    def __init__(self, address):
        self.address = address
        
    def geocode(address):
        location = geolocator.geocode(address, timeout=None)
        if location is None:
            return 0, 0
        else :
            return location.latitude, location.longitude
        