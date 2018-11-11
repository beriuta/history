from django.shortcuts import render

# Create your views here.
def ccc(request):
    name = 'Beriuta'
    return render(request,'t1.html',{'name':name})