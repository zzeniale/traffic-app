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
images = pd.read_sql_query("SELECT image FROM traffic_images ORDER BY db_id DESC LIMIT 6", engine)

# process images
processed_images = []
bg_sub = cv.createBackgroundSubtractorMOG2(history = 5, varThreshold=100, detectShadows=False)
for image in images.values:
    image = np.array(image[0])
    # crop image
    image = image[60:320, 380:]
    image[:185, 240:] = 0
    image[:, 205:] = 0
    image[:170, 200:] = 0
    image[:165, 180:] = 0
    image[:158, 160:] = 0
    image[:153, 150:] = 0
    image[:143, 144:] = 0
    image[50:135, 130:] = 0
    image[60:130, 120:] = 0
    image[70:125, 110:] = 0
    image[80:115, 100:] = 0
    image[90:110, 95:] = 0
    for length, width in zip(np.arange(5,96,5), np.arange(150,0,-10)):
        image[:length,:width]=0
    for length, width in zip(np.arange(150,245, 5), np.arange(0,190,10)):
        image[length:,:width]=0
    # subtract background
    fg = bg_sub.apply(image,learningRate=0.7)
    denoise_tv = denoise_tv_chambolle(fg, weight=0.15, multichannel=False)
    ret,thresh = cv.threshold(denoise_tv,0.15,255,cv.THRESH_BINARY)
    fill = ndi.binary_fill_holes(thresh)
    fill = img_as_ubyte(fill)
    processed_images.append(fill)

# import model
from xgboost import XGBRegressor
import joblib
model = joblib.load('xgb.model')
prediction = model.predict(processed_images[-1])

# create route
@app.route('/') # homepage
def index():
    return prediction
    
    # render the template in link
    # return render_template('index.html', output = "testest")


if __name__ == '__main__':
    # run the app
    app.run()