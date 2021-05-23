import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from mainapp.models import FullName


@login_required()
def index(request):
    fill_name = FullName.objects.all()
    random_name = random.choices(fill_name)
    context = {
        'title': 'главная',
        'random_name': random_name,
    }
    return render(request, 'mainapp/index.html', context)
