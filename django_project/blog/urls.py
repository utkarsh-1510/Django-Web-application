from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('sy/', views.sy, name='sy'),
    path('ty/', views.ty, name='ty'),
    path('fy/', views.fy, name='fy'),
    path('fypaper/', views.fypaper, name='fypaper'),
    path('fybook/', views.fybook, name='fybook'),
    path('sypaper/', views.sypaper, name='sypaper'),
    path('sybook/', views.sybook, name='sybook'),
    path('typaper/', views.typaper, name='typaper'),
    path('tybook/', views.tybook, name='tybook'),
   
    path('studymaterial/', views.studymaterial, name='studymaterial'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)