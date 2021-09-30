from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseNotFound
from datetime import date

from django.views.generic.edit import CreateView, UpdateView, ModelFormMixin
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic import View, TemplateView

# from .forms import WomenForms

# Create your views here.
from myapp.models import Women, Categories


class WomenList(ListView):
    model = Women
    template_name = 'myapp/index.html'
    paginate_by = 3

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(WomenList, self).get_context_data(**kwargs)
    #     context['cat_selected'] = 0
    #     return context

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Categories.objects.all()
        context['cat'] = cat
        return context

    def get_queryset(self):
        return Women.objects.order_by('id')


class WomenCreateViews(CreateView):
    model = Women
    fields = '__all__'
    template_name = 'myapp/women_form.html'
    success_url = '/create'


class WomenUpdateViews(UpdateView):
    model = Women
    fields = '__all__'
    template_name = 'myapp/women_form.html'
    success_url = '/'


def post_detail(request, post_slug):
    # post = Women.objects.get(slug=post_slug)
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'post': post,
        'title': post_slug
    }
    return render(request, 'myapp/post_detail.html', context=context)


def show_categorie(request, cat_slug):
    # cat = Categories.objects.get(slug=cat_slug).id
    # # print(cat)
    # posts = Women.objects.filter(cat_id=cat)
    posts = Women.objects.filter(cat_id__slug__iexact=cat_slug)
    # get filter all exclude
    # icontains
    # iexact
    if len(posts) == 0:
        raise Http404()

    context = {
        'object_list': posts,
        'cat_selected': cat_slug,
        'title': cat_slug,

    }

    return render(request, 'myapp/index.html', context=context)


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


def help(request):
    return HttpResponse('help')


def search(request):
    return render(request, 'myapp/search.html')


def contact(request):
    return HttpResponse('contact us')


def about(request):
    return render(request, 'myapp/about.html')


def PageNotFound(request, exception):
    return HttpResponseNotFound(f'not found')
