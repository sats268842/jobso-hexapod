from __future__ import division
import time
import os

from flask import Flask, render_template,redirect, Response

from flask_restful import Api
from flask_cors import CORS, cross_origin
import logging
import sys
# from models.hexapod.view import app
app = Flask(__name__, template_folder='./templates/')
app.secret_key = "Secret Key"
api = Api(app)
cors = CORS(app)

app.secret_key = os.urandom(24)
app.config['CORS_HEADERS'] = 'Content-Type'
# app.register_bluseprint(app, url_prefix="/hexapod")





# Import the PCA9685 module.
# from 
import Adafruit_PCA9685
# import adafruit_pca9685
# import RPi.GPIO as GPIO  
from time import sleep  



pwm1 = Adafruit_PCA9685.PCA9685(address=0x40)
pwm2 = Adafruit_PCA9685.PCA9685(address=0x41)
# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm1.set_pwm(channel, 0, pulse)
    pwm2.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm1.set_pwm_freq(60)
pwm2.set_pwm_freq(60)


import json
import datetime
import uuid




@app.route('/right', methods=['GET', 'POST'])
def right():
    pwm2.set_pwm(1, 0, 150)
    pwm1.set_pwm(4, 0, 150)
    pwm2.set_pwm(7, 0, 150)
    time.sleep(0.5)

    pwm2.set_pwm(0, 0, 300)
    pwm1.set_pwm(3, 0, 300)
    pwm2.set_pwm(6, 0, 300)
    time.sleep(0.5)

    pwm2.set_pwm(1, 0, 280)
    pwm1.set_pwm(4, 0, 260)
    pwm2.set_pwm(7, 0, 260)
    time.sleep(0.5)

    pwm2.set_pwm(4, 0, 150)
    pwm1.set_pwm(7, 0, 150)
    pwm1.set_pwm(1, 0, 150)
    time.sleep(0.5)
    
    pwm2.set_pwm(0, 0, 400)
    pwm1.set_pwm(3, 0, 400)
    pwm2.set_pwm(6, 0, 400)
    time.sleep(0.5)

    pwm2.set_pwm(3, 0, 300)
    pwm1.set_pwm(6, 0, 300)
    pwm1.set_pwm(0, 0, 300)
    time.sleep(0.5)

    pwm2.set_pwm(4, 0, 250)
    pwm1.set_pwm(7, 0, 250)
    pwm1.set_pwm(1, 0, 250)
    time.sleep(0.5)

    pwm2.set_pwm(1, 0, 150)
    pwm1.set_pwm(4, 0, 150)
    pwm2.set_pwm(7, 0, 150)
    time.sleep(0.5)

    pwm2.set_pwm(3, 0, 400)
    pwm1.set_pwm(6, 0, 400)
    pwm1.set_pwm(0, 0, 400)
    time.sleep(0.5)

    pwm2.set_pwm(1, 0, 280)
    pwm1.set_pwm(4, 0, 260)
    pwm2.set_pwm(7, 0, 260)
    time.sleep(0.5)
    return redirect("http:127.0.0.1:6200", code=200)


@app.route('/left', methods=['GET', 'POST'])
def left():
    print("left")
    pwm2.set_pwm(1, 0, 150)
    pwm1.set_pwm(4, 0, 150)
    pwm2.set_pwm(7, 0, 150)
    time.sleep(0.5)

    pwm2.set_pwm(0, 0, 500)
    pwm1.set_pwm(3, 0, 500)
    pwm2.set_pwm(6, 0, 500)
    time.sleep(0.5)

    pwm2.set_pwm(1, 0, 280)
    pwm1.set_pwm(4, 0, 260)
    pwm2.set_pwm(7, 0, 260)
    time.sleep(0.5)

    pwm2.set_pwm(4, 0, 150)
    pwm1.set_pwm(7, 0, 150)
    pwm1.set_pwm(1, 0, 150)
    time.sleep(0.5)
    
    pwm2.set_pwm(0, 0, 400)
    pwm1.set_pwm(3, 0, 400)
    pwm2.set_pwm(6, 0, 400)
    time.sleep(0.5)

    pwm2.set_pwm(3, 0, 500)
    pwm1.set_pwm(6, 0, 500)
    pwm1.set_pwm(0, 0, 500)
    time.sleep(0.5)

    pwm2.set_pwm(4, 0, 250)
    pwm1.set_pwm(7, 0, 250)
    pwm1.set_pwm(1, 0, 250)
    time.sleep(0.5)

    pwm2.set_pwm(1, 0, 150)
    pwm1.set_pwm(4, 0, 150)
    pwm2.set_pwm(7, 0, 150)
    time.sleep(0.5)

    pwm2.set_pwm(3, 0, 400)
    pwm1.set_pwm(6, 0, 400)
    pwm1.set_pwm(0, 0, 400)
    time.sleep(0.5)

    pwm2.set_pwm(1, 0, 280)
    pwm1.set_pwm(4, 0, 260)
    pwm2.set_pwm(7, 0, 260)
    time.sleep(0.5)
    print("success")
    return redirect("http:127.0.0.1:6200", code=200)

@app.route('/up', methods=['GET', 'POST'])
def halfMotion():
    pwm2.set_pwm(5, 0, 150)
    pwm2.set_pwm(4, 0, 150)
    pwm1.set_pwm(7, 0, 280)
    pwm1.set_pwm(8, 0, 230)
    pwm1.set_pwm(2, 0, 250)
    pwm1.set_pwm(1, 0, 230)
    time.sleep(0.5)

    pwm2.set_pwm(3, 0, 330)
    time.sleep(0.5)

    pwm2.set_pwm(4, 0, 250)
    pwm1.set_pwm(0, 0, 420)
    pwm1.set_pwm(2, 0, 150)
    time.sleep(0.5)

    pwm1.set_pwm(4, 0, 200)
    pwm2.set_pwm(1, 0, 200)
    pwm2.set_pwm(7, 0, 200)
    time.sleep(0.5)

    pwm1.set_pwm(0, 0, 400)
    pwm1.set_pwm(1, 0, 280)
    pwm1.set_pwm(2, 0, 190)
    pwm1.set_pwm(7, 0, 250)
    pwm1.set_pwm(8, 0, 150)
    pwm2.set_pwm(3, 0, 400)
    standUp()
    return redirect("http:127.0.0.1:6200", code=200)


@app.route('/standup', methods=['GET', 'POST'])
def standUp():
    pwm1.set_pwm(0, 0, 400)
    pwm1.set_pwm(3, 0, 400)
    pwm1.set_pwm(6, 0, 400)
    pwm2.set_pwm(0, 0, 400)
    pwm2.set_pwm(3, 0, 400)
    pwm2.set_pwm(6, 0, 400)

    time.sleep(1)

    pwm1.set_pwm(2, 0, 150)
    pwm1.set_pwm(5, 0, 150)
    pwm1.set_pwm(8, 0, 150)
    pwm2.set_pwm(2, 0, 150)
    pwm2.set_pwm(5, 0, 150)
    pwm2.set_pwm(8, 0, 150)
    time.sleep(1)
    pwm1.set_pwm(1, 0, 250)
    pwm1.set_pwm(4, 0, 260)
    pwm1.set_pwm(7, 0, 250)
    pwm2.set_pwm(1, 0, 280)
    pwm2.set_pwm(4, 0, 250)
    pwm2.set_pwm(7, 0, 260)
    time.sleep(1)
    return redirect("http:127.0.0.1:6200", code=200)
    





@app.route('/')
def index():
    return render_template('ui.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True, port=5000, threaded=True)



import cv2
camera = cv2.VideoCapture(0)  # use 0 for web camera
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera
# for local webcam use cv2.VideoCapture(0)

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
