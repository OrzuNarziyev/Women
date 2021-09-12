from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from .views import index, post_detail, about, show_categorie, search_result, contact

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('post/<int:post_id>', post_detail, name='post_detail'),
    path('categorie/<int:cat_id>', show_categorie, name='categorie'),
    path('search/', search_result, name='search_result'),
    path('contacts/',contact ,name='contact' ),
    path('help/', help, name='help'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
