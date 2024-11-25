from django.db import models
from django.core.validators import FileExtensionValidator

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=100, null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null= False)
    quantidade = models.IntegerField(null= False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    imagem = models.ImageField(upload_to= "produto/", null=True, blank = True, 
                               validators= [FileExtensionValidator(['png', 'jpg', 'jpeg', 'jfif'])])

    def __str__(self):
        return self.nome