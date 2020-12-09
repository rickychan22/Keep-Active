import keyboard
import pyautogui
from tkinter import *
import time
import signal
import sys

import tkinter as tk
    
switch = True
#set switch to False
#causes frezze with Tkinter GUI due to while loop
#Solution is to implement threading see threading branch
def off():
	switch ==  False

#function to set switch to True
#execute move function
def on():
	switch == True
	auto_move()


def auto_move():

	#move in a square patern for the duration while loop is active
	#trigger while loop with boolean switch
	while switch:
		print(switch)
		print(pyautogui.position())
		pyautogui.moveTo(766,376,duration = 1)
		print(pyautogui.position())
		time.sleep(10)

		pyautogui.moveTo(927, 372, duration = 1)
		print(pyautogui.position())
		time.sleep(10)

		pyautogui.moveTo(936, 531, duration = 1) 
		print(pyautogui.position())
		time.sleep(10)

		pyautogui.moveTo(760, 518, duration = 1) 
		print(pyautogui.position())
		time.sleep(10)

#creates basic GUI for script
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

#stop button
button = tk.Button(frame, 
                   text="Start", 
                   command=on)
button.pack(side=tk.LEFT)
root.mainloop()

"""while True:
	try: #if key is pressed start automatic mouse movemnet
		if keyboard.is_pressed('q'):
			# automatic movement code here
			auto_move()
		elif keyboard.is_pressed('w'):
			break
	except: # exits loop if key is pressed
		break
		"""