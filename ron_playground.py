from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = MoveHub()

train_motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE) #I put it Counterclockwise because the motor runs the wrong way and i dont want to rebuild it.
train_motor_right = Motor(Port.B)
target_motor_degrees = 510
smalltarget_motor_degrees = 90


train_motor_left.run_angle(500, rotation_angle=smalltarget_motor_degrees)