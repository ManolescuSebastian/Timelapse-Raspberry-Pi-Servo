from time import sleep
from flask import Flask, request, render_template, Response
from flask_restful import Resource, Api
from camera_pi import Camera
import RPi.GPIO as GPIO
import numpy as np
from picamera import PiCamera
import asyncio
import tty, sys, termios

GPIO.setmode(GPIO.BCM)

# Route api
app = Flask(__name__)
api = Api(app)

# Servo motors control
servoPIN = 17

GPIO.setup(servoPIN, GPIO.OUT)
servoVertical = GPIO.PWM(servoPIN, 50)
servoVertical.start(2.5)

# Camera timelapse
@app.route('/timelapse')
def startTimelapse():
    camera = PiCamera()
    camera.resolution = (2592, 1944)
    for filename in camera.capture_continuous('images/img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        sleep(15) # wait 15 seconds
    return ""

#default web page
@app.route('/')
def index():
    return render_template('/index.html')

#display camera video feed using the /stream.mjpg endpoint
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

      
# min 5 / max 12.5
verticalMotorValue = 5
horizontalMotorValue = 5

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
x = 0
while 1:
  x=sys.stdin.read(1)[0]
  if x == "w":
      print('w pressed')
      if verticalMotorValue >= 5 and verticalMotorValue <= 12.5:
          verticalMotorValue += 0.5
          servoVertical.ChangeDutyCycle(verticalMotorValue)
          sleep(0.3)
          print('up')
          break

termios.tcsetattr(sys.stdin, termios.TCSADRAIN,filedescriptors)

if __name__ == '__main__':
    app.run(debug=True, port=5030, host='192.168.1.9',threaded=True)
