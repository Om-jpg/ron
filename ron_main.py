from pybricks.parameters import Color, Port, Direction
from pybricks.pupdevices import ColorDistanceSensor, Motor
from pybricks.tools import wait, multitask, run_task
from pybricks.hubs import MoveHub

last_turn = None
train_motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE) # I put it Counterclockwise because the motor runs the wrong way and i dont want to rebuild it.
train_motor_right = Motor(Port.B)
sensor = ColorDistanceSensor(Port.D)
hub = MoveHub()
target_motor_degrees = 510
smalltarget_motor_degrees = 90

async def small_turn_right(tleft):
    await tleft.run_angle(500, smalltarget_motor_degrees)

async def small_turn_left(tright):
    await tright.run_angle(500, smalltarget_motor_degrees)

async def bothforward(tleft, tright):
    tleft.run(500)
    tright.run(500)

async def bothbackwards(tleft, tright):
    tleft.run(-500)
    tright.run(-500)

async def forward_and_backwards(tleft, tright):
    await multitask(tleft.run_time(500, 1000), tright.run_time(500, 1000))
    await multitask(tleft.run_time(-500, 1000), tright.run_time(-500, 1000))

async def turn_right(tleft):
    await tleft.run_angle(500, target_motor_degrees)

async def turn_left(tright):
    await tright.run_angle(500, target_motor_degrees)

async def stop_motors():
    train_motor_left.stop()
    train_motor_right.stop()

async def colorsensing(desiredcolor):
    while (await sensor.color()) != desiredcolor:
        await wait(10)
    print('found it!')

async def drivesequence():
    while True:
        await forward_and_backwards(train_motor_left, train_motor_right)
        await turn_right(train_motor_left)  

async def driveforcolor(desiredcolor):
    await multitask(colorsensing(desiredcolor), drivesequence(), race=True)

async def findcolor():
    await driveforcolor(Color.BLUE)
    await stop_motors()

async def followcolor(desiredcolor):
    global last_turn
    while True:
        current_color = await sensor.color()
        if current_color == desiredcolor:
            await bothforward(train_motor_left, train_motor_right)
        else:
            await stop_motors()
            
            if last_turn is None:
                await small_turn_right(train_motor_left)
                if (await sensor.color()) == desiredcolor:
                    last_turn = 'right'
                else:
                    await small_turn_left(train_motor_right)
                    await small_turn_left(train_motor_right)
                    if (await sensor.color()) == desiredcolor:
                        last_turn = 'left'
            
            elif last_turn == 'left':
                await small_turn_left(train_motor_right)
                if (await sensor.color()) != desiredcolor:
                    await small_turn_right(train_motor_left)
                    await small_turn_right(train_motor_left)
                    if (await sensor.color()) == desiredcolor:
                        last_turn = 'right'

            elif last_turn == 'right':
                await small_turn_right(train_motor_left)
                if (await sensor.color()) != desiredcolor:
                    await small_turn_left(train_motor_right)
                    await small_turn_left(train_motor_right)
                    if (await sensor.color()) == desiredcolor:
                        last_turn = 'left'
                        
        await wait(10)

async def main():
    await findcolor()
    await followcolor(Color.BLUE)

run_task(main())