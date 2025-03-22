from Model.Cities import City
from Model.Places import Place


class CityManagement:
    def __init__(self, city: City):
        self.city = city

    def add_place_to_city(self, place: Place):
        self.city.places.append({place.object_id: place.name})

