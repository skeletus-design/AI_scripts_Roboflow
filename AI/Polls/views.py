from django.shortcuts import render

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Player

def display_video(request):
    context = {
        "video": Player.objects.all()[0]
    }
    
    return render(request, template_name='Polls/video_template.html', context=context)