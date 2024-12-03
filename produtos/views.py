from django.urls import reverse_lazy
from produtos.forms import CategoriaForm, ProdutoForm
from produtos.models import Categoria, Produto
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class CategoriaListView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'tcategoria/categoria_list.html'
    login_url = "login"

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'tcategoria/categoria_form.html'
    success_url = reverse_lazy('categoria_list')
    login_url = "login"

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'tcategoria/categoria_form.html'
    success_url = reverse_lazy('categoria_list')
    login_url = "login"

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'tcategoria/categoria_confirmar_exclusao.html'
    success_url = reverse_lazy('categoria_list')
    login_url = "login"

####

class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'tproduto/produto_list.html'
    login_url = "login"

class ProdutoDetailView(LoginRequiredMixin, DetailView):
    model = Produto
    template_name = 'tproduto/produto_detail.html'
    login_url = "login"

class ProdutoCreateView(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'tproduto/produto_form.html'
    success_url = reverse_lazy('produto_list')
    login_url = "login"

class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'tproduto/produto_form.html'
    success_url = reverse_lazy('produto_list')
    login_url = "login"

class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'tproduto/produto_confirmar_exclusao.html'
    success_url = reverse_lazy('produto_list')
    login_url = "login"