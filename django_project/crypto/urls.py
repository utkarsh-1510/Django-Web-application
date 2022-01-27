from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('crypto/', views.crypto, name='Cryptography'),
    # path('blog-paper/', views.paper, name='blog-paper'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)