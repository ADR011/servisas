from django.db import models

class Klientas(models.Model):
    kliento_vardas = models.CharField(max_length=20)
    kliento_pavarde = models.CharField(max_length=40)
    