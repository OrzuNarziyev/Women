from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from myapp.views import index,post_detail,about

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('post/', post_detail, name='post_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
