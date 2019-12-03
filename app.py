from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from xgboost import XGBRegressor
import joblib

import cv2 as cv
from skimage.util import img_as_ubyte
from skimage.restoration import denoise_tv_chambolle
from scipy import ndimage as ndi

# initalise app
app = Flask(__name__)

# connect to Heroku PostgreSQL
db_url = 'postgres://syabijfoqfvajg:e6a840c9052355747fc5846aeb7c30496e66e9791da2d34344cab27a088d52ea@ec2-23-21-70-39.compute-1.amazonaws.com:5432/dd9l90skhvq2c0'
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
engine = db.create_engine(db_url, {})

# import model
model = joblib.load('xgb.model')



# create route
@app.route('/') # homepage
def index():
    images = pd.read_sql_query("SELECT image FROM traffic_images ORDER BY db_id DESC LIMIT 6", engine)

    # process images
    white_px = []
    img = []
    split_img = pd.DataFrame(columns=np.arange(1,17))
    bg_sub = cv.createBackgroundSubtractorMOG2(history = 5, varThreshold=100, detectShadows=False)

    def split_image(input_img):
        width = int(input_img.shape[0]/4)
        split = []
        for h in [1,2,3,4]:
            for w in [1,2,3,4]:
                img = input_img[(h - 1)*width : width*h,
                                (w - 1)*width : width*w]
                split.append(img)
        return split

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
        
        foreground = fill.ravel()
        white_px.append(len(foreground[foreground == 255]))
        img.append(fill)

        split = split_image(fill)
        split_df = pd.DataFrame([split], columns=np.arange(1,17))
        split_img = split_img.append(split_df)

    foreground = pd.DataFrame({'whites':white_px,
                            'image':img})
    split_img.reset_index(inplace=True)
    foreground = foreground.join(split_img)
    foreground.drop('index',axis=1,inplace=True)
    foreground_px = foreground[[col for col in foreground if col != 'whites']].applymap(lambda x:x.mean())
    foreground_px = foreground_px.join(foreground.whites)

    prediction = model.predict(foreground_px.loc[5:,:])
    value = int(prediction[0])

    return render_template('index.html', output = value)


if __name__ == '__main__':
    app.debug = True
    # run the app
    app.run()