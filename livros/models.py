from django.db import models

class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_altor = models.CharField(max_length = 30)
    data_cadastro = models.DateField()
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length = 30)
    data_emprestado = models.DateTimeField()
    data_devolucao = models.DateTimeField()
    tempo_duracao = models.TimeField()

    class Meta:
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome