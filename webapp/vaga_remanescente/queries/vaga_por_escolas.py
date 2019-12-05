from utils.ciedudw_connection import CIEDUDWConnection


def get_vaga_por_escolas(filtro, busca, cd_serie):
    connection = CIEDUDWConnection()

    de_para_where = {
        'DRE': f"""where split_part(esc.nm_exibicao_unidade_administrativa,' - ',2) like '%{busca}%'
             and esc_inf.vagas_cd_serie_{cd_serie} notnull 
             and esc_inf.vagas_remanecentes_{cd_serie} notnull
             and esc_inf.vagas_remanecentes_{cd_serie}>0""",

        'SUB': f"""where trim(esc.dc_sub_prefeitura) like '%{busca}%'
             and esc_inf.vagas_cd_serie_{cd_serie} notnull 
             and esc_inf.vagas_remanecentes_{cd_serie} notnull
             and esc_inf.vagas_remanecentes_{cd_serie}>0""",

        'DIS': f"""where trim(esc.nm_distrito) like '%{busca}%'
             and esc_inf.vagas_cd_serie_{cd_serie} notnull 
             and esc_inf.vagas_remanecentes_{cd_serie} notnull
             and esc_inf.vagas_remanecentes_{cd_serie}>0""",

        'ALL': f"""where esc_inf.vagas_remanecentes_{cd_serie} notnull
             and esc_inf.vagas_remanecentes_{cd_serie}>0         
                """
    }

    if filtro:
        querie_escolas = f"""
select cd_unidade_educacao,
       concat(trim(case
                                when tp_escola in (10, 11, 12) then 'CEI'
                                else sg_tp_escola end), ' ', trim(nm_unidade_educacao)) escola,
       case
           when tp_escola in (11, 12, 14, 22) then 'PARCEIRA'
           else 'DIRETA' end                                         as tipo,
       upper(endereco_completo)                                         endereco_completo,
       telefones,
       vagas_cd_serie_{cd_serie} vagas,
        vagas_remanecentes_{cd_serie} vagas_remanescente,
        nm_distrito,
        dc_sub_prefeitura,
        cd_latitude latitude,
        cd_longitude longitude

from (
    select esc_inf.cd_unidade_educacao,
    esc_inf.nm_unidade_educacao,
    esc_inf.nm_exibicao_unidade_educacao,
    esc_inf.tp_escola,
    esc_inf.sg_tp_escola,
    esc_inf.vagas_cd_serie_{cd_serie},
    esc_inf.vagas_remanecentes_{cd_serie}::int,
    esc_inf.sg_tipo_situacao_unidade,
    esc.nm_exibicao_unidade_administrativa,
    esc.nm_unidade_administrativa,
    esc.nm_distrito,
    esc.dc_sub_prefeitura,
    esc.cd_latitude,
    esc.cd_longitude,
    u.endereco_completo,
    u.telefones
    from dw_dims.unidades_educacionais_infantil_vagas_seriev2 esc_inf
    inner join dw_dims.unidades_educacionais esc
    on esc.cd_unidade_educacao = esc_inf.cd_unidade_educacao
    inner join dw_dims.unidades_educacionais_ativas_endereco_contato AS u
    on esc.cd_unidade_educacao = u.cd_unidade_educacao


    {de_para_where.get(filtro)}
    order by esc_inf.vagas_remanecentes_{cd_serie} DESC, esc_inf.nm_unidade_educacao
    ) juntado
                
                """

        escolas = connection.querie(querie_escolas)
        return escolas['results']

    return {'Falta filtro URL'}
