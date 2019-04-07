from goprocam import GoProCamera
import time


class ATEXGoPro:
	def __init__(self):
		self.Cam = GoProCamera.GoPro()

	def get_files(self):
		print("getting files")
		files_temp = self.Cam.listMedia(format=True)


	def record(self, duration):
		print("Recording")
		self.Cam.shoot_video(duration)
		print("Finished Recording")
		

	def get_last(self):
		st=time.time()
		self.Cam.downloadLastMedia()
		print("Downlado time was: " + str(time.time() - st) + " seconds")
		return time.time() - st

if __name__ == "__main__":
	a=ATEXGoPro()
	while 1:
		a.record(30)
		a.get_last()