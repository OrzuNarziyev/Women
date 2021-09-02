from django.shortcuts import render

# Create your views here.
from myapp.models import Women


def index(request):
    w = Women.objects.all().order_by('-time_update')[:4]
    print(w)
    return render(request,'myapp/index.html',{'women':w})

def about(request):
    return render(request,'myapp/about.html')

def post_detail(request):
    return render(request,'myapp/post_detail.html')
