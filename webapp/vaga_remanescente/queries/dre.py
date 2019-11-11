from utils.ciedudw_connection import CIEDUDWConnection


def get_dre():
    connection = CIEDUDWConnection()

    querie_dre = f"""
                select replace(nm_unidade_administrativa, 'DIRETORIA REGIONAL DE EDUCACAO ', '') nm_dre,
       split_part(nm_exibicao_unidade_administrativa, ' - ', 2)                  dre
from dw_dims.unidades_educacionais esc
         inner join dw_dims.unidades_educacionais_infantil_vagas_seriev2 esc_inf
                    on esc_inf.cd_unidade_educacao = esc.cd_unidade_educacao
group by nm_unidade_administrativa, nm_exibicao_unidade_administrativa
                """

    dre = connection.querie(querie_dre)
    return dre['results']
