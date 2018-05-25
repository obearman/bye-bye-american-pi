#rocket code
from L3GD20 import L3GD20
import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
import time
from datetime import date
from datetime import time
from datetime import datetime
camera = PiCamera()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.output(6,GPIO.HIGH)

# Communication object
s = L3GD20(busId = 1, slaveAddr = 0x6b, ifLog = False, ifWriteBlock=False)

# Preconfiguration
s.Set_PowerMode("Normal")
s.Set_FullScale_Value("250dps")
s.Set_AxisX_Enabled(True)
s.Set_AxisY_Enabled(True)
s.Set_AxisZ_Enabled(True)

time.sleep(10)
counter = 0

GPIO.output(17,GPIO.HIGH)
# Print current configuration
s.Init()
s.Calibrate()

# Calculate angle
dt = 0.02
x = 0
y = 0
z = 0
camera.start_preview(fullscreen=False,window=(100,200,300,400))
camera.start_recording("/home/pi/rocketvids/test.h264")
while counter < 20:
        
        time.sleep(dt)
        dxyz = s.Get_CalOut_Value()
        x += dxyz[0]*dt;
        y += dxyz[1]*dt;
        z += dxyz[2]*dt;
        print("{:7.2f} {:7.2f} {:7.2f}".format(x, y, z))

        time.sleep(.5)
        counter = counter + 1
camera.stop_recording()
camera.stop_preview()
GPIO.output(6,GPIO.LOW)
GPIO.output(17,GPIO.LOW)


# here is some new stuff.  cool.
