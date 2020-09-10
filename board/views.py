from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

import board.models as boardmodels

def index(request):
    page = request.GET['page']
    results = boardmodels.fetchlist(page)
    data = {'boardlist': results, 'page': page}
    return render(request, 'board/index.html', data)


def write(request):
    return render(request, 'board/write.html')


def writedata(request):
    title = request.POST['title']
    content = request.POST['content']
    boardmodels.register(title, content)

    return HttpResponseRedirect('/board/write')


def register(request):
    title = request.POST['title']
    content = request.POST['content']
    name = request.POS['name']

    boardmodels.register(title, content, name)

    return HttpResponseRedirect('/board?page=1')


def view(request):
    no = request.GET['no']
    result = boardmodels.fetchone(no)
    boardmodels.hit(no)
    data = {'view': result}

    return render(request, 'board/view.html', data)


def delete(request):
    no = request.GET['no']

    boardmodels.delete(no)

    return HttpResponseRedirect('/board')
