from utils.db_fila_creche_connection import FilaDBConnection


def get_espera(cd_serie, lon, lat, raio):
    connection = FilaDBConnection()
    querie_espera = f"""
            SELECT count(DISTINCT cd_solicitacao_matricula_random)
            FROM unidades_educacionais_ativas_endereco_contato AS u
            LEFT JOIN solicitacao_matricula_grade_dw AS s
            ON u.cd_unidade_educacao::integer = s.cd_unidade_educacao
            WHERE ST_DWithin(geom::geography, ST_SetSRID(ST_MakePoint({lon}, {lat}), 4326), {raio})
              AND s.cd_serie_ensino = {cd_serie}
    """
    espera = connection.querie(querie_espera)
    print(espera)
    return espera['results'][0]['count']
