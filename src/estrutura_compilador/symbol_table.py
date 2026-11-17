from dataclasses import dataclass
from enum import Enum

# Tipos estáticos para o analisador
TIPO_NUMERO = "numero"
TIPO_TEXTO = "texto"
TIPO_LOGICO = "logico"
DESCONHECIDO = "desconhecido"

# Anotando categoria de um ID
class Categoria(Enum):
    VARIAVEL = "variavel"
    CONSTANTE = "constante"

# Propriedades de um ID
@dataclass
class Simbolo:
    nome: str
    categoria: Categoria
    linha: int
    tipo: str = DESCONHECIDO
    constante: object = None

    @property
    def se_constante(self):
        return self.categoria is Categoria.CONSTANTE

# Checando se símbolo já está na tabela
class SimboloDeclarado(Exception):
    def __init__(self, existe):
        self.existe = existe

        super().__init__(f"O nome \"{existe.nome}\" ja está na tabela \n foi definido na linha {existe.linha}")

# Tabela de Símbolos (escopo único)
class TabelaSimbolo:
    def __init__(self):
        # iniciando tabela/dicionario de simbolos
        self.simbolos_tab = {}

    # Declarando símbolo na tabela
    def declarar(self, nome, categoria, linha, tipo=DESCONHECIDO, constante=None):
        if nome in self.simbolos_tab:
            raise SimboloDeclarado(self.simbolos_tab[nome])

        simbolo = Simbolo(nome, categoria, linha, tipo, constante)
        self.simbolos_tab[nome] = simbolo

        return simbolo

    # Buscando ID na tabela de símbolos
    # Retorna None se ID não existir
    def buscar(self, nome):
        return self.simbolos_tab.get(nome)

    # Retorna todos os IDs na tabela em uma lista
    def todos_simbolos(self):
        return list(self.simbolos_tab.values())