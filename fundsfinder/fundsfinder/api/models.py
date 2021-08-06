from django.db import models
import uuid
# Create your models here.

class FundoImobiliario(models.Model):
    SETOR_CHOICES = [
        ('hospital', 'Hospital'),('hotel', 'Hotel'), ('hibrido', 'Hibrido'),
        ('lajes_corporativas', 'Lajes Corporativas'),
        ('logistica', 'Logística'), ('outros', 'Outros'),
        ('residencial', 'Residencial'),
        ('títulos_valores_imobiliarios', 'Títulos e Valores Imobiliarios')
    ]
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True)
        
    codigo = models.CharField(
        max_length=8,
        null=False,
        blank=False)
        
    #CPF = models.CharField(
    #    max_length=11,
    #    null=False,
    #    blank=True,
    #    default='SOME STRING')
    #RG = models.CharField(
    #    max_length=7,
    #    null=False,
    #    blank=True,
    #    default='SOME STRING')
    
    setor = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=SETOR_CHOICES)
        
    dividend_yield_medio_12m = models.DecimalField(
        null=False,
        blank=False,
        max_digits=5,
        decimal_places=2)
        
    vacancia_financeira = models.DecimalField(
        null=False,
        blank=False,
        max_digits=5,
        decimal_places=2)
        
    vacancia_fisica = models.DecimalField(
        null=False,
        blank=False,
        max_digits=5,
        decimal_places=2)
        
    quantidade_ativos = models.IntegerField(
        null=False,
        blank=False,
        default=0)
     
