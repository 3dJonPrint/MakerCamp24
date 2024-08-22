from pyxboxcontroller import XboxController, XboxControllerState
import gpiozero
import funktionen as fu

controller = XboxController(0)

while True:
    state: XboxControllerState = controller.state

    left_stick_x: float = state.l_thumb_x
    left_stick_y: float = state.l_thumb_y
    fu.dirve(left_stick_x,left_stick_y)
    print(left_stick_x, left_stick_y)