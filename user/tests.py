from django.shortcuts import render
import user.models as usermodels


def updateform(request):
    no = request.session['authuser']['no']

    # 1. 데이터를 가져오기
    result = usermodels.fetchonebyno(no)
    data = {'user': result}
    print(no)
    print(data)
    return render(request, 'user/updateform.html', data)

