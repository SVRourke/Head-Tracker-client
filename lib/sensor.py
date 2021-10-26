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
        print("Hello")
        ports = [i for i in serial.tools.list_ports.comports()]
        port = [i for i in ports if "Arduino Micro" in i.description]
        self.port = port[0].name

    def port(self):
        print(self.port)

    def connect(self):
        # Handle Handshake and calibration
        self.connection = serial.Serial(self.port, self.baud, self.timeout)

    def read_value(self):
        line = self.connection.readline().decode('ascii').strip()
        # parse Frame
        return line

    # def parseframe(frame):
    # splitframe = frame.split("|")
    # try:
    #     return {
    #         "x": splitframe[0],
    #         "y": splitframe[1],
    #         "z": splitframe[2],
    #     }
    # except:
    #     pass
