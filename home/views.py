from django.shortcuts import render,redirect
from pytube import YouTube,Playlist
import os
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')


def downloadvideo(request):
    global url
    url= request.GET.get('url')
    yt = YouTube(url)
    strm = []
    strm= yt.streams.filter(progressive=True)
    Title=yt.title
    thumb = yt.thumbnail_url
    audio = yt.streams.get_audio_only('mp4')
    v = yt.views
    r = yt.rating
    
    return render(request,'downloadvideo.html', {'strm':strm,'Title':Title,'thumbnail':thumb,'url':url,'audio':audio,'views':v,'rating':r})

def downloading(request,resolution):
    global url 
    homedir = os.path.expanduser('~')
    dirs = homedir + '/Downloads'
    if request.method == 'POST':
        YouTube(url).streams.get_by_resolution(resolution).download(dirs)
        messages.success(request, 'Download Complete !')
    return redirect(request.META['HTTP_REFERER'])

def downloadingaudio(request,itag):
    global url
    homedir = os.path.expanduser('~')
    dirs = homedir + '/Downloads'
    if request.method == 'POST':
        YouTube(url).streams.get_by_itag(itag).download(dirs)
        messages.success(request, 'Download Complete !')
    return redirect(request.META['HTTP_REFERER'])

def playlist(request):
    global purl
    purl= request.GET.get('url')

    # playlist = Playlist(purl)
    # print('Number of videos in playlist: %s' % len(playlist.video_urls))
    # for video_url in playlist.video_urls:
    #     print(video_url)

    return render(request,'playlist.html')


