# ponto_app/gestor_ponto/models.py
from django.db import models
from datetime import timedelta

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="funcionarios")

    def __str__(self):
        return self.nome


class Ponto(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name="pontos")
    data = models.DateField(auto_now_add=True)
    entrada = models.TimeField()
    saida = models.TimeField(null=True, blank=True)

    def calcular_horas_trabalhadas(self):
        if self.saida:
            entrada_timedelta = timedelta(hours=self.entrada.hour, minutes=self.entrada.minute)
            saida_timedelta = timedelta(hours=self.saida.hour, minutes=self.saida.minute)
            return saida_timedelta - entrada_timedelta
        return timedelta(0)

    def __str__(self):
        return f"{self.funcionario.nome} - {self.data}"
