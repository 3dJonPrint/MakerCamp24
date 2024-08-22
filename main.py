import xbox
import gpiozero as gpio
#import funktionen as fu

#motor pins
rev_left_pin = 1
for_left_pin = 7
speed_left_pin = 12

for_right_pin = 14
rev_right_pin = 15
speed_right_pin = 18

#motor pins initalisirung
for_left = gpio.DigitalOutputDevice(for_left_pin)
rev_left = gpio.DigitalOutputDevice(rev_left_pin)
speed_left = gpio.PWMOutputDevice(speed_left_pin)

for_right = gpio.DigitalOutputDevice(for_left_pin)
rev_right = gpio.DigitalInputDevice(rev_left_pin)
speed_right = gpio.PWMOutputDevice(speed_left_pin)

#Fahrfunktion
def drive(speed = 1.0, steer = 0.0):
  brake = False
  speed2 = speed
  speed = abs(speed)
  right = 0.0
  left = 0.0
  if (speed == 0 and not steer == 0):
    left = 1.0*steer
    right = -1.0*steer
  elif (speed == 0 and steer == 0):
    brake = True
    for_left.on()
    for_right.on()
    rev_left.on()
    rev_right.on()
    left = 1
    right = 1
  else:
    if steer < 0:
      left = map(1+steer, -1, 0, 0, speed)
      right = speed
    elif steer > 0:
      right = map(1-steer, 0, 1, speed, 0)
      left = speed
    elif steer == 0:
      left,right = speed,speed
    i = 1
    if speed2 > 0:
      i = 1
    elif speed2 < 0:
      i = -1
    left = left*i
    right = right*i
  if not brake:
    if left > 0:
      for_left.on()
      rev_left.off()
    elif left < 0:
      rev_left.on()
      for_left.off()
    if right > 0:
      for_right.on()
      rev_right.off()
    elif right < 0:
      rev_right.on()
      for_right.off()
  print("MotSpeed: ",left,right)
  left = abs(left)
  right = abs(right)
  print("MotContollSpeed: ",left,right)
  speed_left.value = left
  speed_right.value = right

def map(x, in_min, in_max, out_min, out_max):
  # Berechnen des umgewandelten Werts
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min




joy = xbox.Joystick()

while True:
    l_x = joy.leftX()
    l_y = joy.leftY()

    drive(l_x,l_y)
    print(l_x, l_y)