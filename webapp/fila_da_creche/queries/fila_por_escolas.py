from utils.db_fila_creche_connection import FilaDBConnection


def get_fila_por_escolas(cd_serie, lon, lat, raio):
    connection = FilaDBConnection()
    querie_escolas = f"""
            select juntado.cd_unidade_educacao,
           tipo,
           escola,
           upper(endereco_completo) endereco_completo,
           telefones,
           cd_longitude longitude,
           cd_latitude latitude,
           total
    from (
             SELECT u.cd_unidade_educacao,
                    case
                        when tp_escola in (11, 12, 14, 22) then 'PARCEIRA'
                        else 'DIRETA' end as                                       tipo,
                    concat(trim(case
                                when tp_escola in (10, 11, 12) then 'CEI'
                                else sg_tp_escola end), ' ', trim(u.nm_unidade_educacao)) escola,
                    u.endereco_completo,
                    u.telefones,
                    u.cd_longitude,
                    u.cd_latitude,
                    count(distinct cd_solicitacao_matricula_random)                total
             FROM unidades_educacionais_ativas_endereco_contato AS u
                      LEFT JOIN solicitacao_matricula_grade_dw AS s
                                ON u.cd_unidade_educacao::integer = s.cd_unidade_educacao
             WHERE ST_DWithin(geom::geography, ST_SetSRID(ST_MakePoint({lon}, {lat}), 4326), {raio})
               AND s.cd_serie_ensino = {cd_serie}
         group by u.cd_unidade_educacao, u.nm_unidade_educacao,
                  u.endereco_completo, u.telefones, u.cd_longitude, u.cd_latitude, sg_tp_escola, tp_escola
         ) juntado

            """
    escolas = connection.querie(querie_escolas)
    return escolas['results']
