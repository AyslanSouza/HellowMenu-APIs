from django.shortcuts import render
from .models import Produto
from django.contrib.auth.decorators import login_required 
import datetime
from .models import  Produto, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json



# Create your views here.
def home(request):
    produtos = Produto.objects.all()  # Busca todos os produtos se nenhum ID de categoria for fornecido
    return render(request, 'home.html', {'produtos': produtos})

def itensCarrinho(request):
    return render(request, 'itensCarrinho.html')

def localEntrega(request):
    return render(request, 'localEntrega.html')

def resumoCarrinho(request):
    return render(request, 'resumoCarrinho.html')

def lista_produtos(request, ID_Categoria=None):
    if ID_Categoria:
        produtos = Produto.objects.filter(ID_Categoria=ID_Categoria)  # Filtra produtos por categoria
    else:
        produtos = Produto.objects.all()  # Busca todos os produtos se nenhum ID de categoria for fornecido
    return render(request, 'home.html', {'produtos': produtos})

@login_required
def minha_conta(request):
    return render(request, 'cardapio/minha_conta.html')

class UserCreateView(LoginRequiredMixin, generic.CreateView):
    model = User
    fields = ['nome','senha', 'email', 'cpf', 'restaurante']
    template_name = 'cardapio/user_form.html'
    success_url = reverse_lazy('minha_conta')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.data_inicio = datetime.date.today()
        return super().form_valid(form)
    
class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ['senha', 'email', 'cpf', 'restaurante']
    template_name = 'cardapio/user_form_update.html'
    success_url = reverse_lazy('minha_conta')


@api_view(['GET'])
def get_users(request):
    if request.method == 'GET':
        # Se um ID for passado como parâmetro de consulta
        user_id = request.GET.get('id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                serializer = UserSerializer(user)
                return Response(serializer.data)
            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def update_user(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_user(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        