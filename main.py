import xbox
import gpiozero
import funktionen as fu

joy = xbox.Joystick()

while True:
    l_x = joy.leftX()
    l_y = joy.leftY()

    fu.drive(l_y,l_x)
    print(l_y, l_x)