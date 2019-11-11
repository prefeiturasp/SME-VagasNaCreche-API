from utils.ciedudw_connection import CIEDUDWConnection


def get_sub_prefeituras():
    connection = CIEDUDWConnection()

    querie_subpref = f"""
select dc_sub_prefeitura
from dw_dims.unidades_educacionais esc
         inner join dw_dims.unidades_educacionais_infantil_vagas_seriev2 esc_inf
                    on esc_inf.cd_unidade_educacao = esc.cd_unidade_educacao
group by dc_sub_prefeitura
order by dc_sub_prefeitura;
                """

    subpref = connection.querie(querie_subpref)
    return subpref['results']
