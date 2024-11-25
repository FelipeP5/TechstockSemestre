from django.urls import reverse_lazy
from movimentacao.forms import MovimentacaoForm
from movimentacao.models import Movimentacao
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class MovimentacaoListView(ListView, LoginRequiredMixin):
    model = Movimentacao
    template_name = 'movimentacao_list.html'

class MovimentacaoCreateView(CreateView, LoginRequiredMixin):
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacao_form.html'
    success_url = reverse_lazy('movimentacao_list')

class MovimentacaoUpdateView(UpdateView, LoginRequiredMixin):
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacao_form.html'
    success_url = reverse_lazy('movimentacao_list')

class MovimentacaoDeleteView(DeleteView, LoginRequiredMixin):
    model = Movimentacao
    template_name = 'movimentacao_confirm_delete.html'
    success_url = reverse_lazy('movimentacao_list')

