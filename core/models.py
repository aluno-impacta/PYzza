from django.db import models
import uuid
from django.db.models import Avg

import core.models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Produto(Base):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False)
    nome = models.CharField('Nome do Produto', max_length=100, help_text='nome do produto')
    categoria = models.CharField('Categoria', max_length=200, help_text='Ex: frios, massas')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2, help_text='R$')
    medida = models.CharField('Medida', max_length=2, help_text='Ex: kg, Un')
    estoqueatual = models.IntegerField('Estoque Atual')
    estoqueminimo = models.IntegerField('Estoque Minimo')
    nomeempresa = models.CharField('Nome da Empresa', max_length=100)
    situacaoestoque = models.CharField('Situação do Estoque', max_length=100, help_text='Ex: Regular/Negativo')

    class Meta:
        unique_together = ('nome', 'nomeempresa',)

    def __str__(self):
        return self.nomeempresa


class Fornecedor(Base):
    empresa = models.ForeignKey(Produto,  on_delete=models.CASCADE)
    cnpj = models.CharField('CNPJ', max_length=18)
    telefone = models.CharField('Telefone', max_length=12, help_text='Digite o numero do Telefone')
    email = models.EmailField('E-mail', max_length=100, help_text='Digite seu email')

    class Meta:
        verbose_name_plural = 'Fornecedores'
        unique_together = ('empresa', 'cnpj', 'telefone', 'email',)


class SituacaoEstoque(Base):
    pass


class RepresentanteComercial(Base):
    empresa = models.OneToOneField(Produto, on_delete=models.CASCADE)
    nomecontato = models.CharField('Nome do Representante', max_length=100)
    endereco = models.CharField('Endereço', max_length=100)
    bairro = models.CharField('Bairro', max_length=100)
    cep = models.CharField('CEP', max_length=10)
    cidade = models.CharField('Cidade', max_length=20)
    estado = models.CharField('Estado', max_length=2)
    cpf = models.CharField('CPF', max_length=20)

    class Meta:
        verbose_name_plural = 'Representantes Comerciais'
        unique_together = ('nomecontato', 'endereco', 'cpf',)

    def __str__(self):
        return self.nomecontato








