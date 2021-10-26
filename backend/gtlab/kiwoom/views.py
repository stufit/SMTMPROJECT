from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'kiwoom/mainpage.html')
    '''
    if request.method == 'GET':
        return render(request, 'kiwoom/mainpage.html')
    
    elif request.method == 'POST':
        username = request.POST.get('아이디',None)
        password = request.POST.get('비밀번호',None)

        res_data={}
    ''' 