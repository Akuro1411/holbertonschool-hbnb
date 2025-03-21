from Interface import Interface
from iso3166 import countries


class Country(Interface):
    def __init__(self, country_name):
        super().__init__()
        self.country_code = countries.get(country_name).alpha2
        self.country_name = country_name
        self.cities = []  # This list contains cities (city id) of given country.
