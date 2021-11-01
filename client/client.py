
from tkinter import ttk
import tkinter as tk
import sys
sys.path.insert(1, '../lib')

from gamepad import Controller
from sensor import Sensor



window = tk.Tk()
window.title("ArduTrack")
# window.geometry('500x300')

# ============================================
# Sensor Frame
# ============================================
# frame
sensor = tk.Frame(window)
sensor.grid(column=0, row=0, columnspan=2, pady=15, padx=25)
# Frame Label
sensorFrameLabel = ttk.Label(sensor, text='Sensor')
sensorFrameLabel.grid(columnspan=1, rowspan=1)

# Connect Button
connectButton = tk.Button(sensor, text="connect", width=40)
connectButton.grid(column=0, row=1, rowspan=1, columnspan=1)

# Calibrate Button
calibrateButton = tk.Button(sensor, text="calibrate", width=40)
calibrateButton.grid(column=0, row=2, rowspan=1, columnspan=1)

# Calibrate Button
readButton = tk.Button(sensor, text="read", width=40)
readButton.grid(column=0, row=3, rowspan=1, columnspan=1)


# ============================================
# Gamepad Frame
# ============================================
# gamepad = tk.Frame(window)
# gamepad.grid(column=2, row=0, columnspan=2, rowspan=1, pady=15, padx=8)

# gamepadFrameLabel = ttk.Label(gamepad, text='Gamepad', width=50)
# gamepadFrameLabel.grid(columnspan=1, rowspan=1)

window.mainloop()
