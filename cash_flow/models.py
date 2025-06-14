from django.db import models

class FlowType(models.TextChoices):
    ENTER = "Entrada"
    OUT = "Saida"

class CashFlow(models.Model):
    created_at = models.DateField()
    name = models.TextField()
    value = models.FloatField()
    description = models.TextField()
    type = models.TextField(FlowType)
    
    def __str__(self): 
        return self.name