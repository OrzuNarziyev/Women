from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseNotFound
from datetime import date

from django.views.generic.edit import CreateView, UpdateView, ModelFormMixin
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic import View, TemplateView

# from .forms import WomenForms

# Create your views here.
from myapp.models import Women, Categories
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib import messages


class WomenList(ListView):
    model = Women
    template_name = 'myapp/index.html'
    paginate_by = 3
    queryset = Women.objects.order_by('-id')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['cat_selected'] = 0
        print(self.request.user.username)
        context['today'] = date.today()
        return context




    # def get_queryset(self):
    #     return Women.objects.filter()


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


class DetailViews(DetailView):
    model = Women
    template_name = 'myapp/post_detail.html'
    context_object_name = 'post'
    # pk_url_kwarg = 'post_id'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] =
        return context


# def post_detail(request, post_slug):
#     # post = Women.objects.get(slug=post_slug)
#     post = get_object_or_404(Women, slug=post_slug)
#     context = {
#         'post': post,
#         'title': post_slug
#     }
#     return render(request, 'myapp/post_detail.html', context=context)

# @login_required
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


# def register(request):
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             #log the user in
#             return redirect('index')
#     else:
#         form = CreateUserForm()
#     return render(request, 'login', {'form':form})


def register(request):
    form = CreateUserForm()
    context = {'form': form}

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        # print(form)
        if form.is_valid():
            print('succses')


            user = form.cleaned_data.get('username')
            messages.success(request, 'bu foydalanuvch' + user + 'royhatdan otgan')
            form.save()
            return redirect('login')



    return render(request, 'myapp/register.html', context=context)


# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(request,username=username,password=password)
#
#         if user is not None:
#             login(request,user)
#         else:
#             messages.info(request,'username yoki parol xato')


# def logoutpage(request):
#     logout(request)
#     return redirect('home')



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
