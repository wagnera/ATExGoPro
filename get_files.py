from weather_balloon_control import ATEXGoPro
import time

a=ATEXGoPro()
print("Starting Up")
time.sleep(10)
dt = 0
while 1:
	if dt < 30:
		time.sleep(30-dt)
	dt = a.get_last()