from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Bet
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class BetListView(ListView):
    model = Bet
    template_name = "lista_bets.html"
    context_object_name = 'bets'
