from gpiozero import  Button, LED
from signal import pause
import subprocess
from datetime import datetime

power_button = Button(3, hold_time=5)
allow_shutdown = False
pressed_time = datetime.now()

def shutdown():
	time_delta = (datetime.now() - pressed_time).total_seconds()
	if(allow_shutdown and time_delta > 10):
		allow_shutdown = False
	elif(allow_shutdown and time_delta <= 10):
		subprocess.call(["sudo", "shutdown", "now"])

def change_state():
	allow_shutdown = True
	pressed_time = datetime.now()

red_led =  LED(17)

red_led.source = power_button

power_button.when_held = change_state
power_button.when_released = shutdown

pause()




