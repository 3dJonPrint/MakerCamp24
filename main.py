import xbox
import gpiozero
import funktionen as fu
import time

joy = xbox.Joystick()

while True:
    l_x = joy.leftX()
    l_y = joy.leftY()
    #drive
    fu.drive(l_y,l_x)
    print(l_y, l_x)

time.sleep(100)