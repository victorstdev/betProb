from django.contrib.auth.models import User
from django.db import models
from datetime import date
# Create your models here.

MERCADOS = (
    ('ml', 'ML'),
    ('am', 'Ambas Marcam'),
    ('ov', 'Over'),
    ('un', 'Under'),
    ('mu', 'Múltipla'),
    ('ea', 'Empate Anula')
)

RESULTADOS = (
    ('g', 'Green'),
    ('r', 'Red'),
    ('d', 'Devolvida'),
    ('e', 'Encerrada'),
    ('p', 'Pendente')
)

class Bet(models.Model):
    data = models.DateField("Data do Evento", auto_now=False)
    evento = models.CharField("Nome do Evento", max_length=50)
    mercado = models.CharField("Mercado", max_length=10, choices=MERCADOS, default='ml')
    valor_aposta = models.DecimalField("Valor da Aposta", max_digits=10, decimal_places=2, default=1)
    odd = models.DecimalField("Odd", max_digits=10, decimal_places=2, default=1)
    resultado = models.CharField("Resultado da Aposta", choices=RESULTADOS, max_length=10, default='g')
    editar_lucro = models.BooleanField("Editar Lucro")
    lucro = models.DecimalField("Lucro", max_digits=10, decimal_places=2, default=0)
    roi = models.DecimalField("ROI", max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.evento
    
    def save(self, *args, **kwargs):

        if self.editar_lucro == False:
            if self.resultado == 'g':
                total = self.valor_aposta * self.odd
                self.lucro = total - self.valor_aposta
            elif self.resultado == 'r':
                self.lucro = self.valor_aposta * -1
            elif self.resultado == 'd':
                self.lucro = 0

        self.roi = (self.lucro / self.valor_aposta) * 100

        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-data']
