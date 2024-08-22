import xbox
import gpiozero
import funktionen as fu

joy = xbox.Joystick()

while True:
    l_x = joy.leftX()
    l_y = joy.leftY()

    fu.dirve(l_x,l_y)
    print(l_x, l_y)