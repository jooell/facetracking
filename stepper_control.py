import keyboard
import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

# kit == HAT controller
kit = MotorKit(i2c=board.I2C())

def shutdown():
    kit.stepper2.release()
    kit.stepper1.release()
    print("motor released from cancelation prompt")
    time.sleep(1)
    sys.exit()


def turn_left():
    print("left")
    kit.stepper2.onestep()
    #kit.stepper2.onestep(style=stepper.DOUBLE)

def turn_right():
    print("right")
    kit.stepper2.onestep(direction=stepper.BACKWARD)
    #kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)

def turn_left_no2():
    print("left")
    kit.stepper1.onestep()
    #kit.stepper2.onestep(style=stepper.DOUBLE)

def turn_right_no2():
    print("right")
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    #kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)


def main():

    while True:
        # disable
        if keyboard.is_pressed('space'):
            shutdown()
            break

        # safety
        if keyboard.is_pressed('a') and keyboard.is_pressed('d'):
            continue
        if keyboard.is_pressed('q') and keyboard.is_pressed('e'):
            continue

        # upper axis A D
        if keyboard.is_pressed('a') and not keyboard.is_pressed('d'):
            turn_left()
            while keyboard.is_pressed('a') and not keyboard.is_pressed('d'):
                time.sleep(0.01)
                turn_left()

        if keyboard.is_pressed('d') and not keyboard.is_pressed('a'):
            turn_right()
            while keyboard.is_pressed('d') and not keyboard.is_pressed('a'):
                time.sleep(0.01)
                turn_right()

        # lower axis Q E
        if keyboard.is_pressed('q') and not keyboard.is_pressed('e'):
            turn_left_no2()
            while keyboard.is_pressed('q') and not keyboard.is_pressed('e'):
                time.sleep(0.01)
                turn_left_no2()

        if keyboard.is_pressed('e') and not keyboard.is_pressed('q'):
            turn_right_no2()
            while keyboard.is_pressed('e') and not keyboard.is_pressed('q'):
                time.sleep(0.01)
                turn_right_no2()


if __name__ == "__main__":
    main()