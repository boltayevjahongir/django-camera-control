import cv2

class LiveWebCam(object):
	def __init__(self, urls):
		self.url = cv2.VideoCapture(urls)

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self, url=None):
		success,imgNp = self.url.read()
		resize = cv2.resize(imgNp, (2120, 1220), interpolation = cv2.INTER_LINEAR)
		ret, jpeg = cv2.imencode('.jpg', resize)
		return jpeg.tobytes()
