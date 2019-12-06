from django.db import models


class HistoricoBuscaEndereco(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    cd_serie = models.IntegerField(blank=True, null=True, default=0)
    dt_pesquisa = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'pesq_historico_busca_endereco'

    def __str__(self):
        return f'latitude: {self.latitude} - longitude:{self.longitude} - serie:{self.cd_serie}'
