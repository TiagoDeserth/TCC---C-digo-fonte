from flask import session
from main import usuario_dao  # Importe o DAO correto

def user_context_processor():
    user_id = session.get('usuario_logado')
    if user_id:
        usuario = usuario_dao.busca_por_id(user_id)
        return {'usuario': usuario}
    return {'usuario': None}
