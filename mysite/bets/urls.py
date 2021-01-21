from django.urls import path
from .views import IndexView, BetListView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('lista/', BetListView.as_view(), name='lista'),
    # path('analise/', BetListView.as_view(), name='analise'),
]
