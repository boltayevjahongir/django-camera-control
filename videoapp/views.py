from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from videoapp.camera import LiveWebCam
from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = 'index.html'

class AboutPageView(TemplateView):
	template_name = 'about-camera.html'

class ViewsPageView(TemplateView):
	template_name = 'views-camera.html'

# def home(request):
# 	return render(request, 'videoapp/index.html')
def index(request):
	return render(request, 'videoapp/home.html')
def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen2(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def livecam_feed(request):
    return StreamingHttpResponse(gen(LiveWebCam("rtsp://admin:12345asd@213.230.97.43:226/Streaming/channels/1")),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

def livecam_feed2(request):
    return StreamingHttpResponse(gen2(LiveWebCam("rtsp://admin:12345asd@213.230.97.43:202/Streaming/channels/1")),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
