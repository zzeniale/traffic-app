from flask import Flask, render_template, request, jsonify
import numpy as np 
import requests, signal, time
from PIL import Image
# initalise app
app = Flask(__name__)

# create route
@app.route('/') # homepage
def index():
    # render the template in link
    return render_template('index.html', output = image_input[2][-1][-1][-1])


import atexit
# v2.x version - see https://stackoverflow.com/a/38501429/135978
# for the 3.x version
from apscheduler.scheduler import Scheduler

cron = Scheduler(daemon=True)
# Explicitly kick off the background thread
cron.start()

@cron.interval_schedule(seconds=5)
def job_function():
    print(1)
    # Do your work here

# # Shutdown your cron thread if the web process is stopped
# atexit.register(lambda: cron.shutdown(wait=False))



if __name__ == '__main__':
    # app.debug = True
    # run the app
    app.run()


# # set timeout
# hours = 12
# timeout = 3600 * hours # seconds

# # define a handler for the timeout
# def handler(signum, frame):
#     raise Exception(f"Download complete. End of {timeout} seconds.")

# image_input = []
# image_output = []

# def download_images():
#     print("downloading...")
#     while True:
#         results = requests.get("https://api.data.gov.sg/v1/transport/traffic-images").json()
#         cameras = results['items'][0]['cameras']
#         for camera in cameras:
#             # select the Tuas camera
#             if camera['camera_id'] == '4713':
#                 # get the image
#                 url = camera['image']
#                 response = requests.get(url, stream=True)
#                 img = Image.open(response.raw)
    
#                 image_input.append(np.array(img))
#                 if len(image_input) > 3:
#                     del(image_input[0])
                

# #                 # append first image
# #                 if n == 1:
# #                     image_output[n] = np.array(img)
# #                 # for subsequent images, check if they're the same as the previous one
# #                 elif (image_input[n] != image_input[n-1]).any():
# #                     image_output[n] = np.array(img)
 
#         time.sleep(60)

# # register the signal function handler
# signal.signal(signal.SIGALRM, handler)

# # set alarm for function end
# signal.alarm(timeout)

# try:
#     download_images()
# except Exception as exc: 
#     print (exc)


