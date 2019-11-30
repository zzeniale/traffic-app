from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import pandas as pd
import matplotlib.pyplot as plt

# initalise app
app = Flask(__name__)

# connect to Heroku PostgreSQL
db_url = 'postgres://syabijfoqfvajg:e6a840c9052355747fc5846aeb7c30496e66e9791da2d34344cab27a088d52ea@ec2-23-21-70-39.compute-1.amazonaws.com:5432/dd9l90skhvq2c0'
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
engine = db.create_engine(db_url, {})
df = pd.read_sql_query("SELECT image FROM traffic_images ORDER BY db_id DESC LIMIT 6", engine)

# create route
@app.route('/') # homepage
def index():
    sample = df.loc[0,'image']
    return plt.imshow(sample)
    # render the template in link
    # return render_template('index.html', output = "testest")


if __name__ == '__main__':
    # run the app
    app.run()