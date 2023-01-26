import serial

from roboclaw_python.roboclaw_python.roboclaw_python.roboclaw_3 import Roboclaw
import time

# address of the RoboClaw as set in Motion Studio

address = 128

# Creating the RoboClaw object, serial port and baudrate passed

# ser = serial.Serial("CO35", 38400, timeout=1)
# print(ser.isOpen())

roboclaw = Roboclaw("COM6", 38400)

# Starting communication with the RoboClaw hardware

print(roboclaw.Open())

# Start motor 1 in the forward direction at half speed

speed = 20

t_end = time.time() + 1

def forward():
    global address, speed
    print("On Track!")
    while time.time() < t_end:
        roboclaw.ForwardM1(address, speed)
        roboclaw.ForwardM2(address, speed)

def backward():
    global address, speed
    print("backward")
    while time.time() < t_end:
        roboclaw.BackwardM1(address, speed)
        roboclaw.BackwardM2(address, speed)

def left():
    global address, speed
    print("Turn Left!")
    while time.time() < t_end:
        roboclaw.ForwardM1(address, speed)
        roboclaw.BackwardM2(address, speed)

def right():
    global address, speed
    print("Turn Right!")
    while time.time() < t_end:
        roboclaw.BackwardM1(address, speed)
        roboclaw.ForwardM2(address, speed)

#While input equals previous input then continue the function
#Otherwise go to the new function

roboclaw.Close()
