import RPi.GPIO as GPIO
import time
import numpy as np
from picamera import PiCamera
import asyncio

servoPIN = 17

GPIO.setmode(GPIO.BCM)

# Camera setup
camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

time.sleep(2)

for filename in camera.capture_continuous('img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    time.sleep(15) # wait 3 seconds

# Servo motor setup
GPIO.setup(servoPIN, GPIO.OUT)

#p = GPIO.PWM(servoPIN, 50)
#p.start(2.5)


#try:
#  while True:
#      for x in np.arange(5, 12.5, 0.1):
#          p.ChangeDutyCycle(x)
#          time.sleep(0.3)
#
#except KeyboardInterrupt:
#  p.stop()
#  GPIO.cleanup()
#  camera.close()
