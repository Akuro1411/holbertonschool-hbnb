from API.UserEnd import users
from flask import Flask

app = Flask(__name__)
app.register_blueprint(users, url_prefix='/api')


@app.route('/')
def say_hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)from API.UserEnd import users
from flask import Flask

app = Flask(__name__)
app.register_blueprint(users, url_prefix='/api')


@app.route('/')
def say_hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
