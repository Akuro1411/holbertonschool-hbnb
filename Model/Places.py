from Model.Interface import Interface
from Model.Users import User

class Place(Interface):
    def __init__(self, place_name, place_description, place_address, place_longitude, place_latitude,
                 place_price, guest_number, place_bathroom, count_rooms):
        super().__init__()
        self.name = place_name
        self.description = place_description
        self.address = place_address
        self.longitude = place_longitude
        self.latitude = place_latitude
        self.price_per_night = place_price
        self.max_guest = guest_number
        self.bathroom = place_bathroom
        self.rooms = count_rooms
        self.host_id = []
        self.amenities = []  # This list contains amenities (amenity id) of given place.
        self.reviews = []  # This list contains reviews of given place
