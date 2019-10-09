from gpiozero import LED, PingServer
from gpiozero.tools import negated
from signal import pause
import time

yellow_led = LED(4)
red_led = LED(17)
green_led = LED(18)

yellow_led.on()

time.sleep(15)

google = PingServer('google.com')

green_led.source_delay = 60
green_led.source = google

yellow_led.source = negated(green_led)


pause()


