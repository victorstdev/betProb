from django.urls import path
from .views import IndexView, BetListView, BetCreateView, BetDeleteView, BetUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('lista/', BetListView.as_view(), name='lista'),
    path('cadastrar/', BetCreateView.as_view(), name='cadastrar'),
    path('editar/<int:pk>', BetUpdateView.as_view(), name='editar'),
    path('excluir/<int:pk>', BetDeleteView.as_view(), name='excluir'),
    # path('analise/', BetListView.as_view(), name='analise'),
]
