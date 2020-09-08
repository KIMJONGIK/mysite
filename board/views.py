from django.http import HttpResponseRedirect
from django.shortcuts import render

import board.models as boardmodels


def index(request):
    return render(request, 'board/index.html')


def write(request):
    return render(request, 'board/write.html')


def registersuccess(request):
    return render(request, 'board/registersuccess.html')


def register(request):
    title = request.POST['title']
    content = request.POST['content']

    boardmodels.register(title, content)
    return HttpResponseRedirect('/board/registersuccess')



