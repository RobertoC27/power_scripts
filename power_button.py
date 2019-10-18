from gpiozero import  Button, LED
from signal import pause
import subprocess
from datetime import datetime

power_button = Button(3, hold_time=5)
allow_shutdown = False
pressed_time = datetime.now()

def shutdown():
	global allow_shutdown
	global pressed_time
	time_delta = abs((datetime.now() - pressed_time).total_seconds())
	if(allow_shutdown and time_delta <= 12):
		subprocess.call(["sudo", "shutdown", "now"])
	elif(time_delta > 12):
		allow_shutdown = False

def change_state():
	global allow_shutdown
	global pressed_time
	allow_shutdown = True
	pressed_time = datetime.now()

red_led =  LED(17)

red_led.source = power_button

power_button.when_held = change_state
power_button.when_released = shutdown

pause()




