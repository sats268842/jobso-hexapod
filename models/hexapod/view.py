from __future__ import division
import time
from flask import Blueprint, jsonify,  render_template, request, redirect, url_for, session, make_response, send_file
from flask.wrappers import Response


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

hexapod_blueprint = Blueprint('hexapod', __name__)

# @vehicles_blueprint.route('/')
# def index():
# 	print("all")
# 	# Doctors = Doctor.all()


@hexapod_blueprint.route('/right', methods=['GET', 'POST'])
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


@hexapod_blueprint.route('/left', methods=['GET', 'POST'])
def left():
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

@hexapod_blueprint.route('/up', methods=['GET', 'POST'])
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


@hexapod_blueprint.route('/standup', methods=['GET', 'POST'])
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
