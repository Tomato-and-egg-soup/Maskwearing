from django.shortcuts import render
from django.http import HttpResponse
from mymask import settings
import os

import sys
import argparse
from .yolobody import YOLO
from PIL import Image

# Create your views here.

def index(request):
    #return HttpResponse("hello world")
    return render(request, 'index.html')

def maskinfo(request):
    if request.method == "POST":
        f1 = request.FILES['pic1']
        fname = '%s/pic/%s' % (settings.MEDIA_ROOT, 'test.jpg')
        with open (fname, 'wb') as pic:
            for c in f1.chunks():
                pic.write(c)

        yolo = YOLO()
        img = 'media/pic/test.jpg'
        image = Image.open(img)
        image = yolo.detect_image(image)
        image.save("static/img/ky.jpg")
        return render(request, 'detect.html')
    else:
        return HttpResponse("error")