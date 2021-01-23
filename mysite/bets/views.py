from django.shortcuts import render, Http404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Avg
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

class BetAnaliseListView(ListView):
    model = Bet
    template_name = "analise.html"
    context_object_name = 'bets'
    def get_queryset(self):
        queryset = {
            'all_bets':Bet.objects.count(),
            'avg_lucro':Bet.objects.aggregate(Avg('lucro'))
        }
        return super().get_queryset()
    

class BetDetailView(DetailView):
    model = Bet
    template_name = "visualizar_bet.html"
    context_object_name = 'bet'

class BetCreateView(CreateView):
    model = Bet
    template_name = "cadastrar_bet.html"
    form_class = CadastrarBetForm
    success_url = reverse_lazy("lista")

class BetUpdateView(UpdateView):
    model = Bet
    template_name = "editar_bet.html"
    form_class = CadastrarBetForm
    success_url = reverse_lazy("lista")

class BetDeleteView(DeleteView):
    model = Bet
    template_name = "excluir_bet.html"
    context_object_name = 'bet'
    success_url = reverse_lazy("lista")
