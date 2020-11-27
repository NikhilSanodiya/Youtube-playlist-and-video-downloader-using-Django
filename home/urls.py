from django.contrib import admin
from django.urls import path
from home import views
app_name='downloader'
urlpatterns = [
    path('',views.home,name='home'),
    path('downloadvideo/',views.downloadvideo,name='downloadvideo'),
    path('downloading/<resolution>/',views.downloading,name='downloading'),
    path('downloadingaudio/<itag>/',views.downloadingaudio,name='downloadingaudio'),
    path('playlist/',views.playlist,name="playlist"),



    
]