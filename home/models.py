from django.db import models

# Create your models here.

# class Product(models.Model):
#     id    = models.AutoField(primary_key=True)
#     name  = models.CharField(max_length = 100) 
#     info  = models.CharField(max_length = 100, default = '')
#     price = models.IntegerField(blank=True, null=True)
#     def __str__(self):
#         return self.name
   

class Produtos(models.Model):
    id    = models.AutoField(primary_key=True)
    nome  = models.CharField(max_length = 100, default = '')
    tipo  = models.CharField(max_length = 1000, default = '')
    tipo2  = models.CharField(max_length = 1000, default = '')
    def __str__(self):
        return self.nome
    

class Comissoes_BTG(models.Model):
    id    = models.AutoField(primary_key=True)
    # tipo  = models.CharField(max_length = 1000, default = '')
    # nome  = models.CharField(max_length = 100, default = '')
    nome  = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    corretagem_percentual = models.FloatField(blank=True, null=True)
    corretagem_fixa = models.FloatField(blank=True, null=True)
    criterio = models.CharField(max_length = 100, default = 'maximo')
    observacao = models.CharField(max_length = 1000, default = '')
    def __str__(self):
        return ' - '.join([str(self.id), str(self.nome)])


class Comissoes_AAI(models.Model):
    id    = models.AutoField(primary_key=True)
    # tipo  = models.CharField(max_length = 1000, default = '')
    # nome  = models.CharField(max_length = 100, default = '')
    nome  = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    corretagem_percentual = models.FloatField(blank=True, null=True)
    def __str__(self):
        return ' - '.join([str(self.id), str(self.nome)])
   