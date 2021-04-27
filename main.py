from time import sleep
from flask import Flask, request, render_template, Response
from flask_restful import Resource, Api
from camera_pi import Camera
import RPi.GPIO as GPIO
import numpy as np
import board
from picamera import PiCamera
import asyncio
import dht11

GPIO.setmode(GPIO.BCM)

# Route api
app = Flask(__name__)
api = Api(app)

# Servo motors control
servoPIN = 17

GPIO.setup(servoPIN, GPIO.OUT)
servoVertical = GPIO.PWM(servoPIN, 50)
servoVertical.start(3.5)
servoVertical.ChangeDutyCycle(4)

# DTH 11 sensor (temperature and humidity)
instance = dht11.DHT11(pin = 22)

# Camera timelapse
@app.route('/timelapse')
def startTimelapse():
    camera = PiCamera()
    camera.resolution = (2592, 1944)
    for filename in camera.capture_continuous('timelapse_images/img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        sleep(5) # wait 5 seconds
    return ""

@app.route('/', methods=['POST'])
def cameraPosition():
    # Get slider Values
    slider1 = request.form["vertical_slider"]
    slider2 = request.form["horizontal_slider"]
    # Change duty cycle
    print(slider1)
    print(slider2)
    p.ChangeDutyCycle(float(slider1))
    p1.ChangeDutyCycle(float(slider2))
    # Give servo some time to move
    sleep(3)
    # Pause the servo
    p.ChangeDutyCycle(0)
    p1.ChangeDutyCycle(0)


# Default web page
@app.route('/')
def index():
    result = instance.read()

    if result.is_valid():
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
    else:
        print("Error: %d" % result.error_code)
    
    return render_template('/index.html')


# Display camera video feed using the /stream.mjpg endpoint
def gen(camera):
    #"""Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/stream.mjpg')
def video_feed():
    #"""Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True, port=5030, host='0.0.0.0',threaded=True)
