from django.urls import path
from .views import ProdutoSaldoView

urlpatterns = [
    path('homepage/', ProdutoSaldoView.as_view(), name='homepage'),
]
