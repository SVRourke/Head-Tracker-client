import vgamepad as vg

class Controller:
    def __init__(self):
        self.pad = vg.VX360Gamepad()

    def update(packet):
        self.pad.left_joystick(x_value=int(packet[0]), y_value=int(packet[1]))
        self.pad.update()
