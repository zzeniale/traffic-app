#!/usr/bin/env python

import requests, shutil
import numpy as np
import cv2 as cv

results = requests.get("https://api.data.gov.sg/v1/transport/traffic-images").json()
cameras = results['items'][0]['cameras']

for camera in cameras:
    # Tuas checkpoint camera ID        
    if camera['camera_id'] == '4713':
        # get image url
        url = camera['image']
        # get timestamp
        timestamp = camera['timestamp'].split('+')[0]
        # download from image url
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(f"./images/4713_{timestamp}.png", 'wb') as file:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, file)   

        image = cv.imread(f"./images/4713_{timestamp}.png")

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

        cv.imwrite(f"./images/4713_{timestamp}.png", image)