from Interface import Interface


class City(Interface):
    def __init__(self, name, code):
        super().__init__()
        self.name = name
        self.country_code = code
        self.places = []  # This list contains places (place id) of given city
