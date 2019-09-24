from django.db import models

class Pessoas(models.model):
   nome = models.CharField(max_length=255, verbose_name='Nome')
   
   sobrenome = models.CharField(max_length=255,
   verbose_name='sobrenome')

   data_nasc = models.CharField(default=timezone.now, 
   verbose_name= 'data de nascimento')

   cpf= models.CharField(max_length=11,
   verbose_name='cpf')
    cep= models.CharField(max_length=8,
    verbose_name='cep')
    item_de_doacao= models.CharField(max_length=255,
    verbose_name='item de doação')
    ativo= models.BooleanField(default=True)
    data_criacao= models.DateTimeField(default=timezone.now)