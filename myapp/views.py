from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound

# Create your views here.
from myapp.models import Women, Categories

cats = Categories.objects.all()


def index(request):
    w = Women.objects.all()
    cat_selected = 0
    context = {
        'women': w,
        'cats': cats,
        'cat_selected': cat_selected,
        'title': 'home'
    }
    return render(request, 'myapp/index.html', context=context)


def about(request):
    return render(request, 'myapp/about.html')


def post_detail(request, post_id):
    post = Women.objects.get(id=post_id)
    context = {
        'post': post,
        'cats': cats,
        'title': 'posts'
        # 'cat_selected': cat_id

    }
    print(post.title)
    return render(request, 'myapp/post_detail.html', context=context)


def show_categorie(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    # get filter all exclude
    # icontains
    # iexact

    if len(posts) == 0:
        raise Http404()

    context = {
        'women': posts,
        'cats': cats,
        'cat_selected': cat_id,
        'title': 'categorie',

    }

    return render(request, 'myapp/index.html', context=context)
    # return render(request,'myapp/show_cat.html')


def PageNotFound(request, exception):
    return HttpResponseNotFound(f'not found')


def search_result(request):
    query = request.GET.get('search')
    search_obj = Women.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    print(query)
    context = {
        'women': search_obj,
        'query': query
    }
    return render(request, 'myapp/search.html', context=context)
