from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


# initalise app
app = Flask(__name__)


# create route
@app.route('/') # homepage
def index():


    return "test"
    # render the template in link
    # return render_template('index.html', output = "testest")


if __name__ == '__main__':
    # run the app
    app.run()