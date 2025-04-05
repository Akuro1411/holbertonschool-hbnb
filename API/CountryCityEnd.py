from flask import Blueprint, request, jsonify
from iso3166 import countries
from Persistance import simple_db
from Model.Cities import City

CountryCity = Blueprint("countries_cities", __name__)


@CountryCity.route('/countries')
def get_list_of_countries():
    country_data = {country.name: country.alpha2 for country in countries}
    return jsonify(country_data), 200


@CountryCity.route('/countries/<country_code>')
def get_country_with_code(country_code):
    try:
        country = countries.get(country_code)
        details = {'Name': country.name,
                   'Alpha2': country.alpha2,
                   'Alpha3': country.alpha3,
                   'Numeric': country.numeric,
                   'Apolitical_Name': country.apolitical_name}
        return jsonify(details)
    except Exception:
        return jsonify({"Error": "There is no such country"})


@CountryCity.route('/countries/<country_code>/cities')
def get_cities_of_country(country_code='AZ'):
    try:
        country_db = simple_db.data_dict['Country']
        if country_db:
            for key in country_db:
                if country_db[key]['country_code'] == country_code:
                    return jsonify({country_db[key]['country_name']: country_db[key]['cities']})
        else:
            return jsonify({"Error": "There is no such country in the database"})
    except Exception:
        return jsonify({"Error": "There is no such country"})


@CountryCity.route('/cities', methods=['POST'])
def post_city():
    data = request.get_json()
    new_city = City(name=data["cityName"], code=data["countryCode"])
    simple_db.save(new_city)
    return jsonify({'Success': 'New city is added'})


@CountryCity.route('/cities')
def get_all_cities():
    cities = simple_db.data_dict['City']
    if cities:
        return cities
    else:
        return jsonify("There is no city yet")


@CountryCity.route('/cities/<city_id>')
def get_city_with_id(city_id):
    city = simple_db.get(city_id, 'City')
    return city


@CountryCity.route('/cities/<city_id>', methods=['PUT'])
def update_city_with_id(city_id):
    city = simple_db.get(city_id, 'City')
    update_data = request.get_json()
    city.update(update_data)
    updated_city = City(name=city['name'], code=city['country_code'])
    updated_city.object_id = city_id
    simple_db.update(updated_city)
    return jsonify({"Success": "City is updated successfully"})


@CountryCity.route('/cities/delete/<city_id>', methods=['DELETE'])
def delete_city_with_id(city_id):
    city = simple_db.delete(city_id, 'City')
    if city is None:
        return jsonify({'Error': 'City is not found'}), 404
    return jsonify({"Success": "Delete on a resource is successful."})

# The problem occurs due to url argument <city_id> and after removing it code works successfully.
# There is some problem here with the error message:
# This route hasn't allowance for required method

# Update:
# I didn't understand why there was error at this route. At first, I changed route, then deleted all changes.
# It works now. I mean same code didn't work at first, then it worked

# Handle:
# It is possible to add same city to same country multiple times. Provide a function which prevents it adding

