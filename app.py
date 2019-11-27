from flask import Flask, render_template, request, jsonify
import numpy as np 
import os
from PIL import Image
# from flask_apscheduler import APScheduler

# initalise app
app = Flask(__name__)

# import (cropped) images
img_files = [f for f in os.listdir("./images") if f != '.DS_Store']
img_files = img_files[-6:]

# background subtraction


# create route
@app.route('/') # homepage
def index():
    # render the template in link
    return render_template('index.html', output = "testest")


if __name__ == '__main__':
    # app.debug = True
    # run the app
    app.run()