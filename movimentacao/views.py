from django.urls import reverse_lazy
from movimentacao.forms import MovimentacaoForm
from movimentacao.models import Movimentacao
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class MovimentacaoListView(LoginRequiredMixin, ListView):
    model = Movimentacao
    template_name = 'movimentacao_list.html'
    login_url = "login"

class MovimentacaoCreateView(LoginRequiredMixin, CreateView):
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacao_form.html'
    success_url = reverse_lazy('movimentacao_list')
    login_url = "login"

class MovimentacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacao_form.html'
    success_url = reverse_lazy('movimentacao_list')
    login_url = "login"

class MovimentacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Movimentacao
    template_name = 'movimentacao_confirm_delete.html'
    success_url = reverse_lazy('movimentacao_list')
    login_url = "login"

