import vgamepad as vg


class Controller:
    def __init__(self):
        self.pad = vg.VX360Gamepad()

    def update(self, packet):
        # yaw / roll
        self.pad.left_joystick(x_value=int(packet[0]), y_value=int(packet[1]))
        # pitch
        self.pad.right_joystick(x_value=int(packet[2]), y_value=int(packet[2]))

        self.pad.update()

# This version accepts values between -32768 and 32767
# self.pad.left_joystick(x_value=int(packet[0]), y_value=int(packet[1]))


# Float version takes a value between 0.0 and 1.0
# gamepad.left_joystick_float(x_value_float=-0.5, y_value_float=0.0)  # values between -1.0 and 1.0
