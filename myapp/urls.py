from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from .views import *

urlpatterns = [
    path('home/', WomenList.as_view(), name='index'),
    path('', WomenList.as_view(), name='home'),
    # path('post/<slug:post_slug>', post_detail, name='post_detail'),

    path('post/<slug:post_slug>',DetailViews.as_view(),name='post_detail'),

    path('categorie/<slug:cat_slug>', show_categorie, name='categorie'),
    path('search/', search_result, name='search_result'),
    path('create/', WomenCreateViews.as_view(), name='create'),
    path('update/<int:pk>', WomenUpdateViews.as_view(), name='update'),



    # other page
    path('help/', help, name='help'),
    path('contacts/', contact, name='contact'),
    path('about/', about, name='about'),

    # authentication
    path('register/', register, name='register'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
