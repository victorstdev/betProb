from django import forms
from .models import Bet

class CadastrarBetForm(forms.ModelForm):
    
    class Meta:
        model = Bet
        fields = '__all__'   
