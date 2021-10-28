import serial
import serial.tools.list_ports


class Sensor:
    def __init__(self, baud=9600, timeout=1):
        self.baud = baud
        self.timeout = timeout

        self.port = None
        self.connection = None
        self.find_port()

    def find_port(self):
        ports = [i for i in serial.tools.list_ports.comports()]
        port = [i for i in ports if "Arduino Micro" in i.description]
        self.port = port[0].name

    def port(self):
        print(self.port)

    def connect(self):
        # Handle Handshake and calibration
        self.connection = serial.Serial(self.port, 115200, timeout=1)

    def calibrate(self):
        self.connection.write("start".encode('ascii'))
        calibrating = True
        while calibrating:
            packet = self.read_value()
            if "CALIBRATION FINISHED" in packet:
                calibrating = False
        print("calibrated")
        return True

    def disconnect(self):
        self.connection.close()

    # Not getting most recent line maybe needs buffer setup, need to send struct from arduino to rectify partial line issues
    def read_value(self):
        # self.connection.flushInput()
        line = self.connection.readline().decode('ascii').strip()
        return line.split("|")

    def parseframe(frame):
        splitframe = frame.split("\t")
        try:
            return {
                "x": splitframe[0],
                "y": splitframe[1],
                "z": splitframe[2],
            }
        except:
            pass
