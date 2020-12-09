import keyboard
import pyautogui
from tkinter import *
import time
import threading


import tkinter as tk
    
switch = True

def start():
	def auto_move():
		while switch == True:
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

			if switch == False:
				break
	thread = threading.Thread(target = auto_move)
	thread.start()
def on():
	switch == True
	start()

def off():
	switch ==  False

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="Stop", 
                   fg="red",
                   command=root.destroy)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Start",
                   command=on)
slogan.pack(side=tk.LEFT)

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