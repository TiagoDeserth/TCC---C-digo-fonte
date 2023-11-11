from models_projeto_interdisciplinar import Alimentos, Usuario, Modalidade_Refeicao, Evento, Ingrediente, Local, Dia, Categoria, Cardapio, Refeicao, Alimento_has_Cardapio

#Comandos SQL dos Alimentos
SQL_DELETA_ALIMENTO='DELETE from Alimento where ID_Alimento=%s'
SQL_CRIA_ALIMENTO='INSERT INTO Alimento (Descricao, kcal, kJ, Proteina, Lipideos, Carboidratos, Calcio, Ferro, Retinol, Vitamina_C, Sodio, Cor, Categorias_ID_Categoria) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
SQL_ATUALIZA_ALIMENTO='UPDATE Alimento SET Descricao=%s, kcal = %s, kJ = %s, Proteina = %s, Lipideos = %s, Carboidratos = %s, Calcio = %s, Ferro = %s, Retinol = %s, Vitamina_C = %s, Sodio = %s, Cor = %s, Categorias_ID_Categoria=%s where ID_Alimento=%s'
SQL_BUSCA_ALIMENTOS='SELECT A.ID_Alimento, A.Descricao, A.kcal, A.kJ, A.Energia, A.Proteina, A.Lipideos, A.Carboidratos, A.Calcio, A.Ferro, A.Retinol, A.Vitamina_C, A.Sodio, A.Cor, A.Categorias_ID_Categoria, C.Nome_Categoria as categoria_nome FROM Alimento A INNER JOIN Categorias C ON A.Categorias_ID_Categoria=C.ID_Categoria'
SQL_ALIMENTO_POR_ID='SELECT A.ID_Alimento, A.Descricao, A.kcal, A.kJ, A.Energia, A.Proteina, A.Lipideos, A.Carboidratos, A.Calcio, A.Ferro, A.Retinol, A.Vitamina_C, A.Sodio, A.Cor, A.Categorias_ID_Categoria, C.Nome_Categoria as categoria_nome FROM Alimento A INNER JOIN Categorias C ON A.Categorias_ID_Categoria=C.ID_Categoria where A.ID_Alimento=%s'

#Comandos SQL dos Usuários
SQL_DELETA_USUARIO='DELETE from usuario where id=%s'
SQL_ATUALIZA_USUARIO='UPDATE usuario SET nome=%s, senha=%s where id=%s'
SQL_USUARIO_POR_ID='SELECT  id, nome, senha from usuario where id=%s'
SQL_BUSCA_USUARIOS='SELECT id, nome, senha from usuario'
SQL_CRIA_USUARIO='INSERT into usuario (id, nome, senha) values (%s, %s, %s)'

#Comandos SQL dos Eventos
SQL_DELETA_EVENTO='DELETE from Eventos where ID_Eventos=%s'
SQL_CRIA_EVENTO='INSERT into Eventos (Nome_Evento, ID_Eventos) values (%s, %s)'
SQL_ATUALIZA_EVENTO='UPDATE Eventos SET Nome_Evento=%s  where ID_Eventos=%s'
SQL_BUSCA_EVENTOS='SELECT ID_Eventos, Nome_Evento from Eventos'
SQL_EVENTO_POR_ID='SELECT ID_Eventos, Nome_Evento from Eventos where ID_Eventos=%s'

#Comandos SQL das Modalidades das Refeições
SQL_DELETA_MODALIDADE_REFEICAO='DELETE from Modalidade_Refeicao where ID_Modalidade_Refeicao=%s'
SQL_CRIA_MODALIDADE_REFEICAO='INSERT into Modalidade_Refeicao (Modalidade, ID_Modalidade_Refeicao) values (%s, %s)'
SQL_ATUALIZA_MODALIDADE_REFEICAO='UPDATE Modalidade_Refeicao SET Modalidade=%s where ID_Modalidade_Refeicao=%s'
SQL_BUSCA_MODALIDADE_REFEICOES='SELECT ID_Modalidade_Refeicao, Modalidade from Modalidade_Refeicao'
SQL_MODALIDADE_REFEICOES_POR_ID='SELECT ID_Modalidade_Refeicao, Modalidade from Modalidade_Refeicao where ID_Modalidade_Refeicao=%s'

#Comandos SQL dos Ingredientes
SQL_DELETA_INGREDIENTE='DELETE from Ingrediente where ID_Ingrediente=%s'
SQL_CRIA_INGREDIENTE='INSERT into Ingrediente (Descricao_Ingrediente, Quantidade_Ingrediente, Unidade_Medida_Ingrediente) values (%s, %s, %s)'
SQL_ATUALIZA_INGREDIENTE='UPDATE Ingrediente SET Descricao_Ingrediente=%s,  Quantidade_Ingrediente=%s, Unidade_Medida_Ingrediente=%s where ID_Ingrediente=%s'
SQL_BUSCA_INGREDIENTES='SELECT ID_Ingrediente, Descricao_Ingrediente, Quantidade_Ingrediente, Unidade_Medida_Ingrediente from Ingrediente'
SQL_INGREDIENTE_POR_ID='SELECT ID_Ingrediente, Descricao_Ingrediente, Quantidade_Ingrediente, Unidade_Medida_Ingrediente from Ingrediente where ID_Ingrediente=%s'

#Comandos SQL do Local
SQL_DELETA_LOCAL='DELETE from Local_RU where ID_Local_RU=%s'
SQL_CRIA_LOCAL='INSERT into Local_RU (Nome_RU, Local_RU) values (%s, %s)'
SQL_ATUALIZA_LOCAL='UPDATE Local_RU SET Nome_RU=%s, Local_RU=%s where ID_Local_RU=%s'
SQL_BUSCA_LOCAIS='SELECT ID_Local_RU, Nome_RU, Local_RU from Local_RU'
SQL_LOCAL_POR_ID='SELECT ID_Local_RU, Nome_RU, Local_RU from Local_RU where ID_Local_RU=%s'

#Comandos SQL do Dia
SQL_DELETA_DIA='DELETE from Dia where ID_Dia=%s'
SQL_CRIA_DIA='INSERT into Dia (Data, Dia_Semana, Precipitacao, Umidade, Vento, Temperatura) values (%s, %s, %s, %s, %s, %s)'
SQL_ATUALIZA_DIA='UPDATE Dia SET Data=%s, Dia_Semana=%s, Precipitacao=%s, Umidade=%s, Vento=%s, Temperatura=%s where ID_Dia=%s'
SQL_BUSCA_DIAS='SELECT ID_Dia, Data, Dia_Semana, Precipitacao, Umidade, Vento, Temperatura from Dia'
SQL_DIA_POR_ID='SELECT ID_Dia, Data, Dia_Semana, Precipitacao, Umidade, Vento, Temperatura from Dia where ID_Dia=%s'

#Comandos SQL da Categoria
SQL_DELETA_CATEGORIA='DELETE from Categorias where ID_Categoria=%s'
SQL_CRIA_CATEGORIA='INSERT into Categorias (Nome_Categoria, ID_Categoria) values (%s, %s)'
SQL_ATUALIZA_CATEGORIA='UPDATE Categorias SET Nome_Categoria=%s where ID_Categoria=%s'
SQL_BUSCA_CATEGORIAS='SELECT ID_Categoria, Nome_Categoria from Categorias'
SQL_CATEGORIA_POR_ID='SELECT ID_Categoria, Nome_Categoria from Categorias where ID_Categoria=%s'

#Comandos SQL do Cardápio
SQL_DELETA_CARDAPIO='DELETE from Cardapio where ID_Cardapio=%s'
SQL_CRIA_CARDAPIO='INSERT into Cardapio (Quantidade_por_aluno, Modalidade_Refeicao_ID_Modalidade_Refeicao, Dia_ID_Dia) values (%s, %s, %s)'
SQL_ATUALIZA_CARDAPIO='UPDATE Cardapio SET Quantidade_por_aluno=%s, Modalidade_Refeicao_ID_Modalidade_Refeicao=%s, Dia_ID_Dia=%s where ID_Cardapio=%s'
SQL_BUSCA_CARDAPIOS='SELECT C.ID_Cardapio, C.Quantidade_por_aluno, C.Dia_ID_Dia, C.Modalidade_Refeicao_ID_Modalidade_Refeicao, D.Data as data_nome, D.Dia_Semana, M.Modalidade as modalidade_nome FROM Cardapio C INNER JOIN Dia D ON C.Dia_ID_Dia=D.ID_Dia INNER JOIN Modalidade_Refeicao M ON C.Modalidade_Refeicao_ID_Modalidade_Refeicao = M.ID_Modalidade_Refeicao'
SQL_CARDAPIO_POR_ID='SELECT C.ID_Cardapio, C.Quantidade_por_aluno, C.Dia_ID_Dia, C.Modalidade_Refeicao_ID_Modalidade_Refeicao, D.Data as data_nome, D.Dia_Semana, M.Modalidade as modalidade_nome FROM Cardapio C INNER JOIN Dia D ON C.Dia_ID_Dia=D.ID_Dia INNER JOIN Modalidade_Refeicao M ON C.Modalidade_Refeicao_ID_Modalidade_Refeicao = M.ID_Modalidade_Refeicao WHERE C.ID_Cardapio = %s'

#Comando SQL do Alimento_has_Cardapio
SQL_CRIA_ALIMENTO_HAS_CARDAPIO = "Insert into Alimento_has_Cardapio (Alimento_ID_Alimento, Quantidade_Alimento, Cardapio_ID_Cardapio) values (%s, %s, %s)"
SQL_DELETA_ALIMENTO_HAS_CARDAPIO_ID_CARDAPIO = "DELETE from Alimento_has_Cardapio where Cardapio_ID_Cardapio=%s"
SQL_BUSCA_ALIMENTO_HAS_CARDAPIO = "SELECT AC.Alimento_ID_Alimento, A.Descricao AS Nome_Alimento, AC.Quantidade_Alimento, AC.Cardapio_ID_Cardapio FROM Alimento_has_Cardapio AS AC INNER JOIN Alimento AS A ON AC.Alimento_ID_Alimento = A.ID_Alimento"
SQL_ALIMENTO_HAS_CARDAPIO_POR_ID = "SELECT AC.Alimento_ID_Alimento, A.Descricao AS Nome_Alimento, AC.Quantidade_Alimento, AC.Cardapio_ID_Cardapio FROM Alimento_has_Cardapio AS AC INNER JOIN Alimento AS A ON AC.Alimento_ID_Alimento = A.ID_Alimento WHERE AC.Cardapio_ID_Cardapio=%s"

class AlimentoDao:
    def __init__(self, db):
       self.__db=db

    def salvar(self, alimento):
        cursor=self.__db.connection.cursor()

        if(alimento._ID_Alimento):
            cursor.execute(SQL_ATUALIZA_ALIMENTO, (alimento._Descricao, alimento._kcal, alimento._kJ, alimento._Proteina, alimento._Lipideos, alimento._Carboidratos, alimento._Calcio, alimento._Ferro, alimento._Retinol, alimento._Vitamina_C, alimento._Sodio, alimento._Cor, alimento._Categorias_ID_Categoria, alimento._ID_Alimento))
        else:
            cursor.execute(SQL_CRIA_ALIMENTO, (alimento._Descricao, alimento._kcal, alimento._kJ, alimento._Proteina, alimento._Lipideos, alimento._Carboidratos, alimento._Calcio, alimento._Ferro, alimento._Retinol, alimento._Vitamina_C, alimento._Sodio, alimento._Cor, alimento._Categorias_ID_Categoria))
            cursor._id=cursor.lastrowid

        self.__db.connection.commit()
        return alimento

    def listar(self):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_ALIMENTOS)
        alimentos=traduz_alimentos(cursor.fetchall())
        return alimentos

    def busca_por_id(self, ID_Alimento):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_ALIMENTO_POR_ID, (ID_Alimento,))
        tupla=cursor.fetchone()
        return Alimentos(tupla[1], 
                         tupla[2], 
                         tupla[3], 
                         tupla[4], 
                         tupla[5], 
                         tupla[6], 
                         tupla[7], 
                         tupla[8], 
                         tupla[9], 
                         tupla[10], 
                         tupla[11], 
                         tupla[12], 
                         tupla[13],
                         tupla[14],
                         tupla[15],  
                         ID_Alimento=tupla[0])

    def deletar(self, ID_Alimento):
        self.__db.connection.cursor().execute(SQL_DELETA_ALIMENTO, (ID_Alimento,))
        self.__db.connection.commit()

class UsuarioDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, usuario):
        cursor=self.__db.connection.cursor()

        if(usuario._id):
            cursor.execute(SQL_ATUALIZA_USUARIO, (usuario._id, usuario._nome, usuario._senha))
        else:
            cursor.execute(SQL_CRIA_USUARIO, (usuario._id, usuario._nome, usuario._senha))
            cursor._id=cursor.lastrowid
        self.__db.connection.commit()
        return usuario

    def busca_por_id(self, id):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados=cursor.fetchone()
        usuario=traduz_usuario_login(dados) if dados else None
        return usuario

    def listar(self):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_USUARIOS)
        usuarios=traduz_usuario(cursor.fetchall())
        return usuarios

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_USUARIO, (id,))
        self.__db.connection.commit()

class EventoDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, evento):
        cursor=self.__db.connection.cursor()

        if(evento._ID_Eventos):
            cursor.execute(SQL_ATUALIZA_EVENTO, (evento._Nome_Evento, evento._ID_Eventos))
        else:
            cursor.execute(SQL_CRIA_EVENTO, (evento._Nome_Evento, evento._ID_Eventos))
            cursor._id=cursor.lastrowid
        self.__db.connection.commit()
        return evento

    def listar(self):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_EVENTOS)
        eventos=traduz_eventos(cursor.fetchall())
        return eventos

    def busca_por_id(self, ID_Eventos):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_EVENTO_POR_ID, (ID_Eventos,))
        tupla=cursor.fetchone()
        return Evento(tupla[1], ID_Eventos=tupla[0])

    def deletar(self, ID_Eventos):
        self.__db.connection.cursor().execute(SQL_DELETA_EVENTO, (ID_Eventos,))
        self.__db.connection.commit()

class Modalidade_RefeicaoDao():
    def __init__(self, db):
        self.__db=db

    def salvar(self, modalidade):
        cursor=self.__db.connection.cursor()

        if(modalidade._ID_Modalidade_Refeicao):
            cursor.execute(SQL_ATUALIZA_MODALIDADE_REFEICAO, (modalidade._Modalidade, modalidade._ID_Modalidade_Refeicao))
        else:
            cursor.execute(SQL_CRIA_MODALIDADE_REFEICAO, (modalidade._Modalidade, modalidade._ID_Modalidade_Refeicao))
            cursor._id = cursor.lastrowid
        self.__db.connection.commit()
        return modalidade

    def listar(self):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_MODALIDADE_REFEICOES)
        modalidades=traduz_modalidades_refeicoes(cursor.fetchall())
        return modalidades

    def busca_por_id(self, ID_Modalidade_Refeicao):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_MODALIDADE_REFEICOES_POR_ID, (ID_Modalidade_Refeicao,))
        tupla=cursor.fetchone()
        return Modalidade_Refeicao(tupla[1], ID_Modalidade_Refeicao=tupla[0])

    def deletar(self, ID_Modalidade_Refeicao):
        self.__db.connection.cursor().execute(SQL_DELETA_MODALIDADE_REFEICAO, (ID_Modalidade_Refeicao,))
        self.__db.connection.commit()

class IngredienteDao:
    def __init__(self, db):
       self.__db=db

    def salvar(self, ingrediente):
        cursor=self.__db.connection.cursor()

        if(ingrediente._ID_Ingrediente):
            cursor.execute(SQL_ATUALIZA_INGREDIENTE, (ingrediente._Descricao_Ingrediente, ingrediente._Quantidade_Ingrediente, ingrediente._Unidade_Medida_Ingrediente, ingrediente._ID_Ingrediente))
        else:
            cursor.execute(SQL_CRIA_INGREDIENTE, (ingrediente._Descricao_Ingrediente, ingrediente._Quantidade_Ingrediente, ingrediente._Unidade_Medida_Ingrediente))
            cursor._id=cursor.lastrowid
        self.__db.connection.commit()
        return ingrediente

    def listar(self):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_INGREDIENTES)
        ingredientes=traduz_ingredientes(cursor.fetchall())
        return ingredientes

    def busca_por_id(self, ID_Ingrediente):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_INGREDIENTE_POR_ID, (ID_Ingrediente,))
        tupla=cursor.fetchone()
        return Ingrediente(tupla[1], tupla[2], tupla[3], ID_Ingrediente=tupla[0])

    def deletar(self, ID_Ingrediente):
        self.__db.connection.cursor().execute(SQL_DELETA_INGREDIENTE, (ID_Ingrediente,))
        self.__db.connection.commit()


class LocalDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, local):
        cursor=self.__db.connection.cursor()

        if(local._ID_Local_RU):
            cursor.execute(SQL_ATUALIZA_LOCAL, (local._Nome_RU, local._Local_RU, local._ID_Local_RU))
        else:
            cursor.execute(SQL_CRIA_LOCAL, (local._Nome_RU, local._Local_RU))
            cursor._id=cursor.lastrowid
        self.__db.connection.commit()
        return local

    def listar(self):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_LOCAIS)
        locais=traduz_locais(cursor.fetchall())
        return locais

    def busca_por_id(self, ID_Local_RU):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_LOCAL_POR_ID, (ID_Local_RU,))
        tupla=cursor.fetchone()
        return Local(tupla[1], tupla[2], ID_Local_RU=tupla[0])

    def deletar(self, ID_Local_RU):
        self.__db.connection.cursor().execute(SQL_DELETA_LOCAL, (ID_Local_RU,))
        self.__db.connection.commit()

class DiaDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, dia):
        cursor=self.__db.connection.cursor()

        if(dia._ID_Dia):
            cursor.execute(SQL_ATUALIZA_DIA, (dia._Data, dia._Dia_Semana, dia._Precipitacao, dia._Umidade, dia._Vento, dia._Temperatura, dia._ID_Dia))
        else:
            cursor.execute(SQL_CRIA_DIA, (dia._Data, dia._Dia_Semana, dia._Precipitacao, dia._Umidade, dia._Vento, dia._Temperatura))
            cursor._id=cursor.lastrowid
        self.__db.connection.commit()
        return dia

    def listar(self):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_DIAS)
        dias=traduz_dias(cursor.fetchall())
        return dias

    def busca_por_id(self, ID_Dia):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_DIA_POR_ID, (ID_Dia,))
        tupla=cursor.fetchone()
        return Dia(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], ID_Dia=tupla[0])

    def deletar(self, ID_Dia):
        self.__db.connection.cursor().execute(SQL_DELETA_DIA, (ID_Dia,))
        self.__db.connection.commit()

class CategoriaDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, categoria):
        cursor=self.__db.connection.cursor()

        if(categoria._ID_Categoria):
            cursor.execute(SQL_ATUALIZA_CATEGORIA, (categoria._Nome_Categoria, categoria._ID_Categoria))
        else:
            cursor.execute(SQL_CRIA_CATEGORIA, (categoria._Nome_Categoria, categoria._ID_Categoria))
            cursor._id=cursor.lastrowid
        self.__db.connection.commit()
        return categoria

    def listar(self):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CATEGORIAS)
        categorias=traduz_categorias(cursor.fetchall())
        return categorias

    def busca_por_id(self, ID_Categoria):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_CATEGORIA_POR_ID, (ID_Categoria,))
        tupla=cursor.fetchone()
        return Categoria(tupla[1], ID_Categoria=tupla[0])

    def deletar(self, ID_Categoria):
        self.__db.connection.cursor().execute(SQL_DELETA_CATEGORIA, (ID_Categoria,))
        self.__db.connection.commit()

class CardapioDao:
    def __init__(self, db):
        self.__db=db

    print("teste")

    def salvar(self, cardapio):
        cursor=self.__db.connection.cursor()

        print("TETAS")

        if(cardapio._ID_Cardapio):
            cursor.execute(SQL_ATUALIZA_CARDAPIO, (cardapio._Quantidade_por_aluno, cardapio._Modalidade_Refeicao_ID_Modalidade_Refeicao, cardapio._Dia_ID_Dia, cardapio._ID_Cardapio))
            cursor._id=cardapio._ID_Cardapio
            print("cardapio._ID_Cardapio (TESTE - ATUALIZAR):", cardapio._ID_Cardapio)
        else:
            #For com um tanto de execute

            print("Quantidade por aluno (DAO): ", cardapio._Quantidade_por_aluno)
            print("Dia_ID_Dia (DAO): ", cardapio._Dia_ID_Dia)
            print("Modalidade_Refeicao_ID_Modalidade (DAO): ", cardapio._Modalidade_Refeicao_ID_Modalidade_Refeicao)

            cursor.execute(SQL_CRIA_CARDAPIO, (cardapio._Quantidade_por_aluno, cardapio._Modalidade_Refeicao_ID_Modalidade_Refeicao, cardapio._Dia_ID_Dia))

            cursor._id=cursor.lastrowid

        print("CURSOR - TESTE (DAO): ", cursor)

        cursor.execute(SQL_DELETA_ALIMENTO_HAS_CARDAPIO_ID_CARDAPIO, (cursor._id,))

        for i in range(len(cardapio._Alimento_ID)):
            alimento_has_cardapio = Alimento_has_Cardapio(cardapio._Alimento_ID[i], None, cardapio._Quantidade_Alimento[i], cursor._id)
            print("Alimento_ID ", cardapio._Alimento_ID[i])
            print("cardapio._Quantidade_Alimento", cardapio._Quantidade_Alimento[i])
            print("ID_Cardapio", cursor._id)
            #print("Quantidade alimento", alimento_has_cardapio._Quantidade_Alimento)
            cursor.execute(SQL_CRIA_ALIMENTO_HAS_CARDAPIO, (alimento_has_cardapio._Alimento_ID_Alimento, 
                                                            alimento_has_cardapio._Quantidade_Alimento, 
                                                            alimento_has_cardapio._Cardapio_ID_Cardapio))
        self.__db.connection.commit()
        return cardapio

    def listar(self):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_CARDAPIOS)
        cardapios=traduz_cardapios(cursor.fetchall())
        return cardapios

    def busca_por_id(self, ID_Cardapio):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_CARDAPIO_POR_ID, (ID_Cardapio,))
        tupla=cursor.fetchone()
        return Cardapio(tupla[1], tupla[2], tupla[3], tupla[4], None, None, None, ID_Cardapio=tupla[0])

    def deletar(self, ID_Cardapio):
        self.__db.connection.cursor().execute(SQL_DELETA_CARDAPIO, (ID_Cardapio,))
        self.__db.connection.commit()

class Alimento_has_CardapioDao:
    def __init__(self, db):
        self.__db=db

    def salvar(self, alimento_has_cardapio):
        cursor = self.__db.connection.cursor()
        sql = "INSERT INTO Alimento_has_Cardapio (Alimento_ID_Alimento, Cardapio_ID_Cardapio, Quantidade_Alimento) VALUES (%s, %s, %s)"
        values = (alimento_has_cardapio._Alimento_ID_Alimento, alimento_has_cardapio._Cardapio_ID_Cardapio, alimento_has_cardapio._Quantidade_Alimento)
        cursor.execute(sql, values)
        self.__db.connection.commit()
        return alimento_has_cardapio
    
    def listar(self):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_ALIMENTO_HAS_CARDAPIO)
        alimento_has_cardapio=traduz_alimentos_has_cardapios(cursor.fetchall())
        aux = len(alimento_has_cardapio)
        print("Quantidade de alimentos nos cardápios:", aux)
        return alimento_has_cardapio
    
    def busca_alimentos_cardapio_por_id_cardapio(self, ID_Cardapio):
        cursor=self.__db.connection.cursor()
        cursor.execute(SQL_ALIMENTO_HAS_CARDAPIO_POR_ID, (ID_Cardapio,))
        alimento_has_cardapio=traduz_alimentos_has_cardapios(cursor.fetchall())
        return alimento_has_cardapio

def traduz_alimentos(alimentos):
    def cria_alimento_com_tupla(tupla):
        return Alimentos(tupla[1], 
                        tupla[2], 
                        tupla[3], 
                        tupla[4], 
                        tupla[5], 
                        tupla[6], 
                        tupla[7], 
                        tupla[8], 
                        tupla[9], 
                        tupla[10], 
                        tupla[11], 
                        tupla[12], 
                        tupla[13], 
                        tupla[14],
                        tupla[15], 
                        ID_Alimento=tupla[0])
    return list(map(cria_alimento_com_tupla, alimentos))

def traduz_usuario(usuarios):
    def cria_usuario_com_tupla(tupla):
        return Usuario(tupla[0], tupla[1], tupla[2])
    return list(map(cria_usuario_com_tupla, usuarios))

def traduz_usuario_login(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])

def traduz_eventos(eventos):
    def cria_evento_com_tupla(tupla):
        return Evento(tupla[1], ID_Eventos=tupla[0])
    return list(map(cria_evento_com_tupla, eventos))

def traduz_modalidades_refeicoes(modalidades):
    def criar_modalidade_refeicoes_com_tupla(tupla):
        return Modalidade_Refeicao(tupla[1], ID_Modalidade_Refeicao=tupla[0])
    return list(map(criar_modalidade_refeicoes_com_tupla, modalidades))

def traduz_ingredientes(ingredientes):
    def cria_ingrediente_com_tupla(tupla):
        return Ingrediente(tupla[1], tupla[2], tupla[3], ID_Ingrediente=tupla[0])
    return list(map(cria_ingrediente_com_tupla, ingredientes))

def traduz_locais(locais):
    def cria_local_com_tupla(tupla):
        return Local(tupla[1], tupla[2], ID_Local_RU=tupla[0])
    return list(map(cria_local_com_tupla, locais))

def traduz_dias(dias):
    def cria_dia_com_tupla(tupla):
        return Dia(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], ID_Dia=tupla[0])
    return list(map(cria_dia_com_tupla, dias))

def traduz_categorias(categorias):
    def cria_categoria_com_tupla(tupla):
        return Categoria(tupla[1], ID_Categoria=tupla[0])
    return list(map(cria_categoria_com_tupla, categorias))

def traduz_cardapios(cardapios):
    def cria_cardapio_com_tupla(tupla):
        return Cardapio(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], None, None, ID_Cardapio=tupla[0])
    return list(map(cria_cardapio_com_tupla, cardapios))

def traduz_alimentos_has_cardapios(alimento_has_cardapio):
    def cria_alimento_has_cardapio_com_tupla(tupla):
        print("Tupla 0", tupla[0])
        print("Tupla 1", tupla[1])
        print("Tupla 2", tupla[2])
        print("Tupla 3", tupla[3])
        return Alimento_has_Cardapio(tupla[0], tupla[1], tupla[2], tupla[3])
    return list(map(cria_alimento_has_cardapio_com_tupla, alimento_has_cardapio))

