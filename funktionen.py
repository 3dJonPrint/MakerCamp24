import gpiozero
import pins

#Fahrfunktion:
def drive(speed = 1.0, steer = 0.0):
  print("speed:",speed,"steer",steer)
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
    pins.for_left.on()
    pins.for_right.on()
    pins.rev_left.on()
    pins.rev_right.on()
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
      pins.for_left.on()
      pins.rev_left.off()
    elif left < 0:
      pins.rev_left.on()
      pins.for_left.off()
    if right > 0:
      pins.for_right.on()
      pins.rev_right.off()
    elif right < 0:
      pins.rev_right.on()
      pins.for_right.off()
  print("MotSpeed: ",left,right)
  left = abs(left)
  right = abs(right)
  print("MotContollSpeed: ",left,right)
  pins.speed_left.value = left
  pins.speed_right.value = right
  print()

def map(x, in_min, in_max, out_min, out_max):
  # Berechnen des umgewandelten Werts
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

drive()