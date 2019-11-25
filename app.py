import numpy as np 
# import os
# import cv2 as cv
# from skimage.util import img_as_ubyte
# from skimage.restoration import denoise_tv_chambolle
# from scipy import ndimage as ndi
from flask import Flask, render_template, request

test = np.load('test.npy')

# initalise app
app = Flask(__name__)

# create route
@app.route('/') # homepage
def index():
    # render the template in link
    return render_template('index.html', output = test.shape[0])

if __name__ == '__main__':
    app.debug = True
    # run the app
    app.run()
