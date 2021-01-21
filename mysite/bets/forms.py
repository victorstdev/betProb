from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Bet

class DateInput(forms.DateInput):
    input_type = 'date'

class CadastrarBetForm(forms.ModelForm):
    
    class Meta:
        model = Bet
        fields = '__all__'
        widgets = {
            'data': DateInput()
        }