from django.urls import path
from produtos.views import CategoriaDeleteView, CategoriaListView, CategoriaCreateView, CategoriaUpdateView, ProdutoCreateView, ProdutoDeleteView, ProdutoListView, ProdutoUpdateView, ProdutoDetailView


urlpatterns = [
    path("produtos/categoria/", CategoriaListView.as_view(), name="categoria_list"),
    path("produtos/categoria/criar", CategoriaCreateView.as_view(), name="categoria_form"),
    path("produtos/categoria/<int:pk>/editar", CategoriaUpdateView.as_view(), name="categoria_update"),
    path("produtos/categoria/<int:pk>/excluir", CategoriaDeleteView.as_view(), name="categoria_delete"),
    #######
    path("produtos/", ProdutoListView.as_view(), name="produto_list"),
    path("produtos/<int:pk>/detalhe/", ProdutoDetailView.as_view(), name="produto_detail"),
    path("produtos/criar/", ProdutoCreateView.as_view(), name="produto_form"),
    path("produtos/produto/<int:pk>/editar", ProdutoUpdateView.as_view(), name="produto_update"),
    path("produtos/produto/<int:pk>/excluir", ProdutoDeleteView.as_view(), name="produto_delete"),
]