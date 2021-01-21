from django.contrib import admin
from .models import Bet
# Register your models here.

class BetAdmin(admin.ModelAdmin):
    list_display = ('evento', 'resultado', 'data')
    
admin.site.register(Bet, BetAdmin)