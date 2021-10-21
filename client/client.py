from tkinter import *
from tkinter import ttk

# window = tk.Tk()

# comframe = tk.Frame(window)
# comframe.pack()

# com port select
# label = tk.Label(text="Select Input Device", master=comframe)
# label.pack()

# combobox
# options = ['COM3', 'COM4', 'COM5']
# combo = ttk.Combobox(comframe, values = options)
# combo.set("Select your device")
# combo.pack()

# submit
# selectCom = tk.Button(comframe, text = "Select")
# selectCom.pack()

# centerButton = tk.Button(comframe, text = "center")
# centerButton.pack()

# startButton = tk.Button(comframe, text = "center")
# startButton.pack()

# joystickframe = tk.Frame(window)
# joystickframe.pack()

# connectbutton = tk.Button(joystickframe, text='Start Joystick')
# connectbutton.pack()

# joystick output representation 
# jus text for now

# head position representation 
# just text for now


# window.mainloop()


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
