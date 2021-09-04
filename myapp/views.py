from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from .models import Women


def index(request):
    w = Women.objects.all().order_by('-time_update')
    print(w)
    return render(request,'myapp/index.html',{'women':w})

def about(request):
    return render(request,'myapp/about.html')

def post_detail(request,post_id):
    w = Women.objects.get(id=post_id)
    print(w.photo)
    context = {"w":w}
    return render(request,'myapp/post_detail.html',context=context)

def contact(request):
    return HttpResponse('contact us')

def help(request):
    return HttpResponse('help')

def search(request):
    return render(request,'myapp/search.html')
