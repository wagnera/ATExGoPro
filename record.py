from weather_balloon_control import ATEXGoPro
import time

a=ATEXGoPro()
while 1:
	print("Start Recording")
	a.record(30)
	print("Finished Recording")