from django.urls import path, include
from videoapp import views
from .views import HomePageView, AboutPageView, ViewsPageView


urlpatterns = [
    # path('test', views.home, name='index'),
    # path('', views.index, name='index'),
    path('', HomePageView.as_view(), name='index'),
    path('about-camera', AboutPageView.as_view(), name='about-camera'),
    path('views-camera', ViewsPageView.as_view(), name='views-camera'),
    path('livecam_feed', views.livecam_feed, name='livecam_feed'),
    path('livecam_feed2', views.livecam_feed2, name='livecam_feed2'),
]