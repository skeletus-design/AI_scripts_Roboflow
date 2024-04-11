from django.shortcuts import render

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, HttpResponse
from .models import Player

def display_video(request):
    context = {
        "video": Player.objects.all()[0]
    }
    
    return render(request, template_name='Polls/video_template.html', context=context)

def download_cheatsheet(request):
    cheatsheet = get_object_or_404(Player.objects.all())
    file_path = cheatsheet.file.path
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = 'application/octet-stream'
    return response