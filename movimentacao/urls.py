from django.urls import path
from .views import MovimentacaoCreateView, MovimentacaoListView, MovimentacaoUpdateView, MovimentacaoDeleteView

urlpatterns = [
    path("movimentacao/", MovimentacaoListView.as_view(), name= 'movimentacao_list'),
    path("movimentacao/criar/", MovimentacaoCreateView.as_view(), name= 'movimentacao_form'),
    path("movimentacao/<int:pk>/editar/", MovimentacaoUpdateView.as_view(), name= 'movimentacao_update'),
    path("movimentacao/<int:pk>/excluir/", MovimentacaoDeleteView.as_view(), name= 'movimentacao_delete')
]