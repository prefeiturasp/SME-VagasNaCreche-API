from django.db import models


class HistoricoBuscaEndereco(models.Model):
    latitute = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    cd_serie = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        db_table = 'pesq_historico_busca_endereco'

    def __str__(self):
        return f'latitude: {self.latitute} - longitude:{self.longitude}'
