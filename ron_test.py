from pybricks.hubs import MoveHub
from pybricks.pupdevices import Motor, ColorDistanceSensor, DCMotor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


hub = MoveHub()

left_motor = DCMotor(Port.A)

left_motor.dc(50)
