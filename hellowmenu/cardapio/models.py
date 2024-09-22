import uuid
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(
        verbose_name="Nome", max_length=100, unique=True, null=False, blank=False, help_text="Nome da categoria")

    def __str__(self):
        return self.nome

class Produto(models.Model):
    ID_Categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, verbose_name="Categoria", null=True, help_text="Id da categoria do produto")
    img = models.ImageField(
        verbose_name="Imagem", upload_to="produtos", null=True, blank=True, help_text="Imagem do produto")
    name = models.CharField(
        verbose_name="Nome", max_length=100, unique=True, null=False, blank=False, help_text="Nome do produto")
    dsc = models.TextField(
        verbose_name="Descrição", null=True, blank=True, help_text="Descrição do produto")
    price = models.DecimalField(
        verbose_name="Preço", max_digits=10, decimal_places=2, null=False, blank=False, help_text="Preço do produto")
    

    def __str__(self):
        return self.name

class Restaurante(models.Model):
        nome_restaurante = models.CharField(
            verbose_name="Nome", max_length=100, unique=True, null=False, blank=False, help_text="Nome do produto")
        nome_proprietario = models.CharField(
            verbose_name="Nome", max_length=100, unique=True, null=False, blank=False, help_text="Nome do produto")
        numero_Proprietario = models.CharField(
            verbose_name="Número", max_length=10, null=False, blank=False, help_text="Número do endereço")
        numero_contato = models.CharField(
            verbose_name="Número", max_length=10, null=False, blank=False, help_text="Número do endereço")
        rua = models.CharField(
            verbose_name="Rua", max_length=100, null=False, blank=False, help_text="Rua do endereço")
        numero = models.CharField(
            verbose_name="Número", max_length=10, null=False, blank=False, help_text="Número do endereço")
        bairro = models.CharField(
            verbose_name="Bairro", max_length=100, null=True, blank=True, help_text="Bairro do endereço")
        cidade = models.CharField(
            verbose_name="Cidade", max_length=100, null=False, blank=False, help_text="Cidade do endereço")
        cep = models.CharField(
            verbose_name="CEP", max_length=8, null=False, blank=False, help_text="CEP do endereço")

        def __str__(self):
            return self.nome_restaurante

class Pedido(models.Model):
    ID_produto = models.ForeignKey(
        Produto, on_delete=models.SET_NULL, verbose_name="Produto", null=True, help_text="Id do Produto")
    ID_restaurante = models.ForeignKey(
        Restaurante, on_delete=models.SET_NULL, verbose_name="Restaurante", null=True, help_text="ID do Restaurante")
    rua = models.CharField(
        verbose_name="Rua", max_length=100, null=False, blank=False, help_text="Rua do endereço")
    numero = models.CharField(
        verbose_name="Número", max_length=10, null=False, blank=False, help_text="Número do endereço")
    complemento = models.CharField(
        verbose_name="Complemento", max_length=100, null=True, blank=True, help_text="Complemento do endereço")
    bairro = models.CharField(
        verbose_name="Bairro", max_length=100, null=True, blank=True, help_text="Bairro do endereço")
    cidade = models.CharField(
        verbose_name="Cidade", max_length=100, null=False, blank=False, help_text="Cidade do endereço")
    cep = models.CharField(
        verbose_name="CEP", max_length=8, null=False, blank=False, help_text="CEP do endereço")

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}"
        
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False, help_text="nome do usuario")
    senha = models.CharField(max_length=100, null=False, blank=False, help_text="senha do usuario")
    email = models.EmailField(max_length=100, null=False, blank=False, help_text="email do usuario")
    cpf = models.CharField(max_length=14, null=False, blank=False, help_text="cpf do usuario")
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'nome: {self.nome} | cpf: {self.cpf}'

    class Meta:
        abstract = False

    