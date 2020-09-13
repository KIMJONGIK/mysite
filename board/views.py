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


def register(request):
    title = request.POST['title']
    content = request.POST['content']
    no = request.session['authuser']['no']
    boardmodels.register(title, content, no)

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
    return HttpResponseRedirect('/board?page=1')


def modifyform(request):
    no = request.GET['no']
    result = boardmodels.fetchone(no)
    data = {'modify': result}
    return render(request, 'board/modify.html', data)


def modify(request):
    no = request.GET['no']
    result = boardmodels.fetchone(no)
    data = {'modify': result}
    title = request.POST['title']
    content = request.POST['content']
    boardmodels.modify(title, content, no)

    return HttpResponseRedirect('/board?page=1', data)

