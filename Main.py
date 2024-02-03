import struct
import time
from tkinter import filedialog, Tk
Tk().withdraw()
print("\033[2J\033[H\033[0mEasy FL PPQ Tool | v1.0.1 by Happy_mimimix\n\nPlease create a blank *.flp project file and select it in the file dialog... ")
filepath = filedialog.askopenfilename(filetypes=[('FL Studio Project File', '*.flp')])
while filepath == '':
    print("\033[2J\033[H\033[0mEasy FL PPQ Tool | v1.0.1 by Happy_mimimix\n\nYou did not select any file. \nPlease create a blank *.flp project file and select it in the file dialog... ")
    filepath = filedialog.askopenfilename(filetypes=[('FL Studio Project File', '*.flp')])
targetPPQ = input("\033[2J\033[H\033[0mEasy FL PPQ Tool | v1.0.1 by Happy_mimimix\n\nType in a PPQ value: ")
while not (targetPPQ.isdigit() and int(targetPPQ) <= 0xFFFF and int(targetPPQ) >= 0x0004):
    targetPPQ = input("\033[2J\033[H\033[0mEasy FL PPQ Tool | v1.0.1 by Happy_mimimix\n\nSorry, we only accept integer values between 4 and 65535. \nPlease try again: ")
file = open(filepath, mode='r+b')
file.seek(0x0C)
file.write(struct.pack('<H', int(targetPPQ)))
file.close()
print("\033[2J\033[H\033[0mEasy FL PPQ Tool | v1.0.1 by Happy_mimimix\n\nPPQ successfully changed. ")
time.sleep(3)
