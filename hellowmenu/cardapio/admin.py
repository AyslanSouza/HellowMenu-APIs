from django.contrib import admin
from .models import Categoria, Produto, Restaurante, Pedido, User

admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Restaurante)
admin.site.register(Pedido)
admin.site.register(User)