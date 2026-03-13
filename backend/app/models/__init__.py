# TODO: Defina seus models/queries de banco aqui
# Tabelas esperadas: users, polls, options, votes
#
# Sugestão: crie um arquivo por entidade (user_model.py, poll_model.py, etc.)
# com funções que encapsulam as queries SQL usando db_utils.run_query()
#
# Exemplo:
# from app.utils.db_utils import run_query
#
# def create_user(email: str, password_hash: str):
#     return run_query(
#         "INSERT INTO users (email, password_hash) VALUES (%s, %s) RETURNING *",
#         (email, password_hash),
#         fetch="one"
#     )
