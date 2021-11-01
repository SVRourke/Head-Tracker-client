from time import sleep
import threading

class App:
    # App provides a simple interface to all
    # of the lower level actions of both Sensor
    # and Controller classes
    def __init__(self):
        self.processing = False

    def connect(self):
        print("not implemented")

    # Start The process of reading the sensor, translating for
    # gamepad and updating the gamepad
    def activate(self):
        # separate thread?
        self.processing = True
        while self.processing:
            print("reading")
            sleep(1)
        print("not implemented")

    def deactivate(self):
        print("not implemented")
