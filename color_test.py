from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = MoveHub()
sensor = ColorDistanceSensor(Port.D)
train_motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE) #I put it Counterclockwise because the motor runs the wrong way and i dont want to rebuild it.
train_motor_right = Motor(Port.B)

while True:
    train_motor_left.run_time(500, 10000, wait=False)
    train_motor_right.run_time(500, 10000, wait=False)
    color = sensor.color()
    print(color)
    wait(100)