from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import pandas as pd

# initalise app
app = Flask(__name__)

# # configure database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://syabijfoqfvajg:e6a840c9052355747fc5846aeb7c30496e66e9791da2d34344cab27a088d52ea@ec2-23-21-70-39.compute-1.amazonaws.com:5432/dd9l90skhvq2c0'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


 # load data from Heroku PostgreSQL
# db_url = os.environ['postgres://syabijfoqfvajg:e6a840c9052355747fc5846aeb7c30496e66e9791da2d34344cab27a088d52ea@ec2-23-21-70-39.compute-1.amazonaws.com:5432/dd9l90skhvq2c0']
# conn = psycopg2.connect(db_url, sslmode='require')
# query = "SELECT time FROM {}".format(settings.traffic_images)
# df = pd.read_sql(query, con=conn)
db_url = 'postgres://syabijfoqfvajg:e6a840c9052355747fc5846aeb7c30496e66e9791da2d34344cab27a088d52ea@ec2-23-21-70-39.compute-1.amazonaws.com:5432/dd9l90skhvq2c0'
engine = SQLAlchemy.create_engine(db_url, {})
df = pd.read_sql_query("SELECT time FROM traffic_images", engine)



# create route
@app.route('/') # homepage
def index():


    return df.head()
    # render the template in link
    # return render_template('index.html', output = "testest")


if __name__ == '__main__':
    # run the app
    app.run()