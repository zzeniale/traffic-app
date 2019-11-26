from flask import Flask, render_template, request
import numpy as np 


# initalise app
app = Flask(__name__)

# create route
@app.route('/') # homepage
def index():
    # render the template in link
    return render_template('index.html', output = "asdfadf")

if __name__ == '__main__':
    app.debug = True
    # run the app
    app.run()
