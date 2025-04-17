from API.UserEnd import users
from API.CountryCityEnd import CountryCity
from API.AmenityEnd import amenities
from API.PlaceEnd import places
from flask import Flask
from Persistance import simple_db

app = Flask(__name__)
app.register_blueprint(users, url_prefix='/user_api')
app.register_blueprint(CountryCity, url_prefix='/country_api')
app.register_blueprint(amenities, url_prefix='/amenity_api')
app.register_blueprint(places, url_prefix='/place_api')


@app.route('/')
def say_hello():
    return "Hello World!"


@app.route('/db')
def get_db():
    return simple_db.data_dict


if __name__ == '__main__':
    app.run(debug=True)


