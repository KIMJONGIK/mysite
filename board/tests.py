from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

import board.models as boardmodels
import user.models as usermodels

from django.test import TestCase


def delete(request):
    no = '1'
    result = boardmodels.fetchone(no)
    print(type(result))

    return HttpResponseRedirect('/board?page=1')