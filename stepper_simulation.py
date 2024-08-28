#import keyboard
#import board
#from adafruit_motor import stepper
#from adafruit_motorkit import MotorKit
import time
import sys

# kit == HAT controller
#kit = MotorKit(i2c=board.I2C())

def shutdown():
    #kit.stepper2.release()
    #kit.stepper1.release()
    print("motor released from cancelation prompt")
    time.sleep(1)
    sys.exit()


def turn_left():
    print("left")
    #kit.stepper2.onestep()
    #kit.stepper2.onestep(style=stepper.DOUBLE)

def turn_right():
    print("right")
    #kit.stepper2.onestep(direction=stepper.BACKWARD)
    #kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)

def turn_left_no2():
    print("left")
    #kit.stepper1.onestep()
    #kit.stepper2.onestep(style=stepper.DOUBLE)

def turn_right_no2():
    print("right")
    #kit.stepper1.onestep(direction=stepper.BACKWARD)
    #kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)



