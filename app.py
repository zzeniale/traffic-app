from flask import Flask, render_template, request
import numpy as np 
from keras.models import load_model
# import os
# import cv2 as cv
# from skimage.util import img_as_ubyte
# from skimage.restoration import denoise_tv_chambolle
# from scipy import ndimage as ndi

test = np.load('test.npy')

# import model
model = load_model("model.hdf5")

# predict with model
processed_images = np.array([x.reshape(260,260,1) for x in test[-3:]])
processed_images = processed_images.astype('float32')/255
processed_images = processed_images.reshape(1,3,260,260,1)
predictions = int(round(model.predict(processed_images)[0][0],0))

# initalise app
app = Flask(__name__)

# create route
@app.route('/') # homepage
def index():
    # render the template in link
    return render_template('index.html', output = predictions)

if __name__ == '__main__':
    app.debug = True
    # run the app
    app.run()
