from django.db import models


class Memorial(models.Model):
    id = models.AutoField(primary_key=True)
    num_obtuario = models.CharField(max_length=100)
    falecido = models.CharField(max_length=100)
    data_nascimento = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    data_falecimento = models.CharField(max_length=100)
    detalhes = models.CharField(max_length=300)

    def __str__(self):
        return self.falecido


    class Meta:
        verbose_name = 'Obituário'
        verbose_name_plural = 'Obituários'
