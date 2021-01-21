from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Bet
from .forms import CadastrarBetForm
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class BetListView(ListView):
    model = Bet
    template_name = "lista_bets.html"
    context_object_name = 'bets'
    paginate_by = 10

class BetCreateView(CreateView):
    model = Bet
    template_name = "cadastrar_bet.html"
    form_class = CadastrarBetForm
    success_url = reverse_lazy("lista")

class BetUpdateView(UpdateView):
    model = Bet
    template_name = "editar_bet.html"
    fields = '__all__'
    success_url = reverse_lazy("lista")

class BetDeleteView(DeleteView):
    model = Bet
    template_name = "excluir_bet.html"
    context_object_name = 'bet'
    success_url = reverse_lazy("lista")
