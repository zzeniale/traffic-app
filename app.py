import numpy as np 
import os

import cv2 as cv
# from skimage.util import img_as_ubyte
# from skimage.restoration import denoise_tv_chambolle
# from scipy import ndimage as ndi

from flask import Flask, render_template, request

path_in = '../../../../Desktop/images/4713/'
img_files = [f for f in os.listdir(path_in) if f != '.DS_Store'][-6:]

frame_array = []

for image in img_files:
    file = cv.imread(path_in + image)

#     # crop image
#     file = file[60:320, 380:]
#     # black out unnecessary parts in cropped image
#     # right polygon
#     file[:185, 240:] = 0
#     file[:, 205:] = 0
#     file[:170, 200:] = 0
#     file[:165, 180:] = 0
#     file[:158, 160:] = 0
#     file[:153, 150:] = 0
#     file[:143, 144:] = 0
#     file[50:135, 130:] = 0
#     file[60:130, 120:] = 0
#     file[70:125, 110:] = 0
#     file[80:115, 100:] = 0
#     file[90:110, 95:] = 0
#     # top left polygon
#     for length, width in zip(np.arange(5,96,5), np.arange(150,0,-10)):
#         file[:length,:width]=0
#     # bottom left polygon
#     for length, width in zip(np.arange(150,245, 5), np.arange(0,190,10)):
#         file[length:,:width]=0

#     # save frame
#     frame_array.append(file)

# # background subtractor
# bg_sub = cv.createBackgroundSubtractorMOG2(history = 5, varThreshold=100, detectShadows=False)
# n=1

# processed_images = []
# for frame in frame_array:
#     # apply background subtractor to frames
#     fg = bg_sub.apply(frame,learningRate=0.7)
    
#     # preprocessing
#     denoise_tv = denoise_tv_chambolle(fg, weight=0.15, multichannel=False)
#     ret,thresh = cv.threshold(denoise_tv,0.15,255,cv.THRESH_BINARY)
#     fill = ndi.binary_fill_holes(thresh)
#     fill = img_as_ubyte(fill)
#     processed_images.append(fill)

# initalise app
app = Flask(__name__)

# create route
@app.route('/') # homepage
def index():
    # render the template in link
    return render_template('index.html', output = img_files[-1])

if __name__ == '__main__':
    app.debug = True
    # run the app
    app.run()
