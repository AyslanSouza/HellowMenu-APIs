from django.contrib import admin
from django.urls import path
from cardapio import views 
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from cardapio.views import lista_produtos

from . import views

urlpatterns = [
    path('', views.get_users, name ='get_all_users'),
    #path('user/<int:id>', views.get_by_nick),
    #path('data/', views.user_manager)
    path('users/', views.get_users, name='get_users'),  # Para listar ou buscar usuários
    path('users/create/', views.create_user, name='create_user'),  # Para criar um novo usuário
    path('users/<int:id>/update/', views.update_user, name='update_user'),  # Para atualizar um usuário
    path('users/<int:id>/delete/', views.delete_user, name='delete_user'),  # Para deletar um usuário
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)