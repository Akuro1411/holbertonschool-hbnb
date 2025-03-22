from Model.Amenities import Amenity
from Model.Places import Place


class AmenityManagement:
    def __init__(self, amenity: Amenity):
        self.amenity = amenity

    def add_place_to_amenity(self, place: Place):
        if place.object_id not in self.amenity.places:
            self.amenity.places.append({place.object_id: place.name})
            return "Place is successfully added to place list in amenity"
        return "Place is already exists in Amenity"

