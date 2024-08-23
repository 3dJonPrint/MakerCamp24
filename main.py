import xbox
import gpiozero
import funktionen as fu
import time

joy = xbox.Joystick()

while True:
    l_x = joy.leftX()
    l_y = joy.leftY()
    l = joy.rightThumbstick()
    #drive
    fu.drive(l_y,l_x,l)
    print(l_y, l_x,l)

    time.sleep(0.1)