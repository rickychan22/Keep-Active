import keyboard

def auto_move():
	print('Hello There')

while True:
	try: #if key is pressed start automatic mouse movemnet
		if keyboard.is_pressed('q'):
			# automatic movement code here
			auto_move()
		elif keyboard.is_pressed('w'):
			break
	except: # exits loop if key is pressed
		break