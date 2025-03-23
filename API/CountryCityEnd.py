from flask import Blueprint, request, jsonify
from iso3166 import countries
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
