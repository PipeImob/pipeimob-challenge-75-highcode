import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """Retorna uma conexão com o PostgreSQL usando as credenciais do .env."""
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "pipeimob_challenge"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", "5432"),
    )


def run_query(query: str, params: tuple = None, fetch: str = "one"):
    """
    Executa uma query no banco PostgreSQL.

    Parâmetros:
        query: str - SQL a ser executado (use %s para parâmetros)
        params: tuple - parâmetros para a query (evita SQL injection)
        fetch: str - "one" retorna um dict, "many" retorna lista de dicts, "none" para INSERT/UPDATE/DELETE
    """
    conn = None
    try:
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(query, params)

            if fetch == "none":
                conn.commit()
                return None

            if cur.description:
                colnames = [desc[0] for desc in cur.description]
                if fetch == "many":
                    rows = cur.fetchall()
                    result = [dict(zip(colnames, row)) for row in rows]
                else:
                    row = cur.fetchone()
                    result = dict(zip(colnames, row)) if row else None
            else:
                result = None

            conn.commit()
            return result
    except Exception:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()
