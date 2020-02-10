from utils.db_fila_creche_connection import FilaDBConnection


def get_dt_atualizacao():
    connection = FilaDBConnection()
    querie_atualizacao = f"""
            SELECT to_timestamp(concat((current_date - 1), ' 06:00:00'), 'YYYY/MM/DD HH') as updated_at
    """
    dt_atualizacao = connection.querie(querie_atualizacao)
    return dt_atualizacao['results'][0]["updated_at"]
