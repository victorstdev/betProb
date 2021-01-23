from django.urls import path
from .views import IndexView, BetListView, BetCreateView, BetDeleteView, BetUpdateView, BetDetailView, BetAnaliseListView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('lista/', BetListView.as_view(), name='lista'),
    path('visualizar/<int:pk>', BetDetailView.as_view(), name='visualizar'),
    path('cadastrar/', BetCreateView.as_view(), name='cadastrar'),
    path('editar/<int:pk>', BetUpdateView.as_view(), name='editar'),
    path('excluir/<int:pk>', BetDeleteView.as_view(), name='excluir'),
    path('analise/', BetAnaliseListView.as_view(), name='analise'),
]
