from django.shortcuts import render,HttpResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        ret = request.POST.get('name')
        print(ret)
        return HttpResponse(ret)
    return render(request, 'index.html')
