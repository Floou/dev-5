from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from mainapp.models import Photo
import random


@login_required()
def index(request):
    num_img = Photo.objects.filter()
    context = {
        'title': 'главная',
        'num_img': random.choices(num_img),
    }
    return render(request, 'mainapp/index.html', context)
