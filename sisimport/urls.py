from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name ='inicio'),
    path('sobre', views.sobre, name='sobre'),
    path('produtos',views.produtos, name='produtos'), 
    path('produtos/criar',views.criar, name='criar'), 
    path('produtos/editar',views.editar, name='editar'), 
    path('apagar/<int:id>',views.apagar, name='apagar'),
    path('produtos/editar/<int:id>',views.editar, name='editar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)