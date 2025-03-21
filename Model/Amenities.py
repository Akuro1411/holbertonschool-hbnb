from Model.Interface import Interface


class Amenity(Interface):
    def __init__(self, name: str):
        super().__init__()
        self.amenity_name = name
        self.places = []  # This list contains places (place id) with given amenity.
