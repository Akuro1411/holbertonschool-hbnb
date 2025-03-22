from Model.Countries import Country
from Model.Cities import City


class CountryManagement:
    def __init__(self, country: Country):
        self.country = country

    def add_city_to_country(self, city: City):
        self.country.cities.append({city.object_id: city.name})
