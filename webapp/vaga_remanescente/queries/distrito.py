from utils.ciedudw_connection import CIEDUDWConnection


def get_distritos():
    connection = CIEDUDWConnection()

    querie_distrito = f"""
select nm_distrito
from dw_dims.unidades_educacionais esc
         inner join dw_dims.unidades_educacionais_infantil_vagas_seriev2 esc_inf
                    on esc_inf.cd_unidade_educacao = esc.cd_unidade_educacao
group by nm_distrito
order by nm_distrito;
                """

    distritos = connection.querie(querie_distrito)
    return distritos['results']
