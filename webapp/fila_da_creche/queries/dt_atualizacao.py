from utils.db_fila_creche_connection import FilaDBConnection


def get_dt_atualizacao():
    connection = FilaDBConnection()
    querie_atualizacao = f"""
            SELECT dt_solicitacao as updated_at
            FROM solicitacao_matricula_grade_dw_atualizacao
    """
    dt_atualizacao = connection.querie(querie_atualizacao)
    return dt_atualizacao['results'][0]["updated_at"]
