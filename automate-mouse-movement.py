import keyboard
import pyautogui

def auto_move():
	while True:
		if keyboard.is_pressed('w'):
			break
		else:
			print(pyautogui.position())
			pyautogui.moveTo(766,376,duration = 2)
			print(pyautogui.position())

			pyautogui.moveTo(927, 372, duration = 2)
			print(pyautogui.position())

			pyautogui.moveTo(936, 531, duration = 2) 
			print(pyautogui.position())

			pyautogui.moveTo(760, 518, duration = 2) 
			print(pyautogui.position())

while True:
	try: #if key is pressed start automatic mouse movemnet
		if keyboard.is_pressed('q'):
			# automatic movement code here
			auto_move()
		elif keyboard.is_pressed('w'):
			break
	except: # exits loop if key is pressed
		break