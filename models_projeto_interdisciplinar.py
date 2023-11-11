from flask_mysqldb import MySQL

class Alimentos:
    def __init__(self, Descricao, kcal, kJ, Energia, Proteina, Lipideos, Carboidratos, Calcio, Ferro, Retinol, Vitamina_C, Sodio, Cor, Categorias_ID_Categoria, Categoria, ID_Alimento=None):
        self._ID_Alimento = ID_Alimento
        self._Descricao = Descricao
        self._kcal = kcal
        self._kJ = kJ
        self._Energia = Energia
        self._Proteina = Proteina
        self._Lipideos = Lipideos
        self._Carboidratos = Carboidratos
        self._Calcio = Calcio
        self._Ferro = Ferro
        self._Retinol = Retinol
        self._Vitamina_C = Vitamina_C
        self._Sodio = Sodio
        self._Cor = Cor
        self._Categorias_ID_Categoria = Categorias_ID_Categoria
        self._Categoria = Categoria

#ID=usuario
class Usuario:
    def __init__(self, nome, id, senha=None):
        self._nome=nome
        self._id=id
        self._senha=senha

class Evento:
    def __init__(self, Nome_Evento, ID_Eventos=None):
        self._Nome_Evento=Nome_Evento
        self._ID_Eventos=ID_Eventos

class Modalidade_Refeicao:
    def __init__(self, Modalidade, ID_Modalidade_Refeicao=None):
        self._Modalidade=Modalidade
        self._ID_Modalidade_Refeicao=ID_Modalidade_Refeicao

class Ingrediente:
    def __init__(self, Descricao_Ingrediente, Quantidade_Ingrediente, Unidade_Medida_Ingrediente, ID_Ingrediente=None):
        self._ID_Ingrediente=ID_Ingrediente
        self._Descricao_Ingrediente=Descricao_Ingrediente
        self._Quantidade_Ingrediente=Quantidade_Ingrediente
        self._Unidade_Medida_Ingrediente=Unidade_Medida_Ingrediente

    def getIdIngrediente(self):
        return self._ID_Ingrediente

class Local:
    def __init__(self, Nome_RU, Local_RU, ID_Local_RU=None):
        self._ID_Local_RU=ID_Local_RU
        self._Nome_RU=Nome_RU
        self._Local_RU=Local_RU

class Dia:
    def __init__(self, Data, Dia_Semana, Precipitacao, Umidade, Vento, Temperatura, ID_Dia=None):
        self._ID_Dia=ID_Dia
        self._Data=Data
        self._Dia_Semana=Dia_Semana
        self._Precipitacao=Precipitacao
        self._Umidade=Umidade
        self._Vento=Vento
        self._Temperatura=Temperatura

class Categoria:
    def __init__(self, Nome_Categoria, ID_Categoria=None):
        self._ID_Categoria=ID_Categoria
        self._Nome_Categoria=Nome_Categoria

class Cardapio:
    def __init__(self, Quantidade_por_aluno, Modalidade_Refeicao_ID_Modalidade_Refeicao, Dia_ID_Dia, Modalidade_Refeicao, Nome_Alimento, Quantidade_Alimento, Alimento_ID, ID_Cardapio=None):
        self._ID_Cardapio=ID_Cardapio
        self._Quantidade_por_aluno=Quantidade_por_aluno
        self._Modalidade_Refeicao_ID_Modalidade_Refeicao=Modalidade_Refeicao_ID_Modalidade_Refeicao
        self._Dia_ID_Dia = Dia_ID_Dia
        self._Modalidade_Refeicao = Modalidade_Refeicao

        #Listas de alimentos
        self._Nome_Alimento = Nome_Alimento
        self._Quantidade_Alimento = Quantidade_Alimento
        self._Alimento_ID = Alimento_ID

class Alimento_has_Cardapio:
    def __init__(self, Alimento_ID_Alimento, Nome_Alimento, Quantidade_Alimento, Cardapio_ID_Cardapio):
        self._Alimento_ID_Alimento = Alimento_ID_Alimento
        self._Nome_Alimento = Nome_Alimento
        self._Quantidade_Alimento = Quantidade_Alimento
        self._Cardapio_ID_Cardapio = Cardapio_ID_Cardapio

class Refeicao:
    def __init__(self, Quantidade_por_pratos, ID_Refeicao=None):
        self._ID_Refeicao=ID_Refeicao
        self._Quantidade_por_pratos=Quantidade_por_pratos
