from gpiozero import  Button, LED
from signal import pause
import subprocess

power_button = Button(3, hold_time=5)

def shutdown():
	subprocess.call(["sudo", "shutdown", "now"])

red_led =  LED(17)
#green_led = LED(18)

red_led.source = power_button
#green_led.source = power_button


power_button.when_held = shutdown
pause()




