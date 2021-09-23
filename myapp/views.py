from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from datetime import date

from django.views.generic.edit import CreateView, UpdateView, ModelFormMixin
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic import View,TemplateView

# from .forms import WomenForms

# Create your views here.
from myapp.models import Women, Categories


class WomenCreateViews(CreateView):
    # model = Women
    model = Women
    fields = '__all__'
    template_name = 'myapp/women_form.html'
    success_url = '/create'

class WomenUpdateViews(UpdateView):
    # model = Women
    model = Women
    fields = '__all__'
    template_name = 'myapp/women_form.html'
    success_url = '/'


# class WomenViews(ListView):
#     paginate_by = 2
#     model = Women
#     template_name = 'myapp/index.html'
#
#     def get_context_data(self, object_list=None, **kwargs):
#         print(self.object_list)
#         context = super(WomenViews, self).get_context_data(**kwargs)
#         context['cat_selected'] = 0
#         context['title'] = 'home_page'


# def index(request):
#     w = Women.objects.all()
#     cat_selected = 0
#     context = {
#         'women': w,
#         'cat_selected': cat_selected,
#         'title': 'home'
#     }
#     return render(request, 'myapp/index.html', context=context)

def about(request):
    return render(request, 'myapp/about.html')


def post_detail(request, post_id):
    post = Women.objects.get(id=post_id)
    context = {
        'post': post,
        'title': 'posts'

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
        'object_list': posts,
        'cat_selected': cat_id,
        'title': 'categorie',

    }

    return render(request, 'myapp/index.html', context=context)



def PageNotFound(request, exception):
    return HttpResponseNotFound(f'not found')


def search_result(request):
    query = request.GET.get('search')
    search_obj = Women.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    context = {
        'women': search_obj,
        'query': query
    }
    return render(request, 'myapp/search.html', context=context)




def contact(request):
    return HttpResponse('contact us')


def help(request):
    return HttpResponse('help')


def search(request):
    return render(request, 'myapp/search.html')

class WomenList(ListView):
    model = Women
    template_name = 'myapp/index.html'
    paginate_by = 3



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WomenList, self).get_context_data(**kwargs)
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.order_by('id')




