from django import forms
from produtos.models import Categoria, Produto

class CategoriaForm(forms.ModelForm):
    class Meta:
     model = Categoria
     fields = ['nome']
     labels = {'nome' : 'Nome da Categoria'}

class ProdutoForm(forms.ModelForm):
   class Meta:
     model = Produto
     fields = ['nome', 'valor', 'categoria', 'quantidade', 'descricao', 'imagem']
     labels = {'nome' : 'Nome do Produto',
               'valor' : 'Preço(R$)',
               'categoria' : 'Categoria',
               'quantidade' : 'Quantidade',
               'descricao' : 'Descrição',
               'imagem' : 'Imagem do Produto'}