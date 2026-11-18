import unittest
import os
import sys

pasta_atual = os.path.dirname(os.path.abspath(__file__))
pasta_raiz = os.path.dirname(pasta_atual)

if pasta_raiz not in sys.path:
    sys.path.insert(0, pasta_raiz)

from src.compilador.lexer import tokenizar
from src.compilador.parser import analisar_sintaxe
from src.tratamento_erros.errors_parser import ErroParser, reportar_erro_sintatico


def testar_erro(codigo):
    """Retorna a mensagem formatada do primeiro erro sintático."""
    try:
        analisar_sintaxe(tokenizar(codigo))
    except ErroParser as erro:
        return reportar_erro_sintatico(erro)
    return None


# Cada caso associa o problema esperado a um programa que contém esse erro.
ERROS_SINTATICOS = {
    "ERRO_INICIO_PROGRAMA": (
        "ESCREVA 10\nFIM_PROGRAMA",
        "Todo programa começa com a palavra PROGRAMA.",
    ),
    "ERRO_FIM_PROGRAMA": (
        "PROGRAMA\nESCREVA 10",
        "Eu esperava FIM_PROGRAMA para terminar",
    ),
    "ERRO_SEM_FIM_SE": (
        "PROGRAMA\nSE VERDADE ENTAO\nESCREVA 1\nFIM_PROGRAMA",
        "O SE da linha 2 não foi fechado",
    ),
    "ERRO_SEM_FIM_ENQUANTO": (
        "PROGRAMA\nENQUANTO VERDADE FACA\nPARAR\nFIM_PROGRAMA",
        "O ENQUANTO da linha 2 não foi fechado",
    ),
    "ERRO_SEM_FIM_REPITA": (
        "PROGRAMA\nREPITA 2 VEZES\nESCREVA 1\nFIM_PROGRAMA",
        "O REPITA da linha 2 não foi fechado",
    ),
    "ERRO_SEM_ENTAO": (
        "PROGRAMA\nSE VERDADE\nESCREVA 1\nFIM_SE\nFIM_PROGRAMA",
        "Eu esperava a palavra ENTAO",
    ),
    "ERRO_SEM_FACA": (
        "PROGRAMA\nENQUANTO VERDADE\nPARAR\nFIM_ENQUANTO\nFIM_PROGRAMA",
        "Eu esperava a palavra FACA",
    ),
    "ERRO_ATRIBUICAO_SEM_IGUAL": (
        "PROGRAMA\nx 10\nFIM_PROGRAMA",
        'Depois do nome "x" eu esperava o sinal =',
    ),
    "ERRO_VARIAS_INSTRUCOES_NA_LINHA": (
        "PROGRAMA\nx = 1 y = 2\nFIM_PROGRAMA",
        "Escreva uma instrução por linha",
    ),
    "ERRO_COMPARACAO_ENCADEADA": (
        "PROGRAMA\nx = 1 MENOR_QUE 2 MENOR_QUE 3\nFIM_PROGRAMA",
        "Compare dois valores por vez",
    ),
    "ERRO_PROGRAMA_DUPLICADO": (
        "PROGRAMA\nPROGRAMA\nFIM_PROGRAMA",
        "Seu programa já foi iniciado",
    ),
    "ERRO_COMANDO_APOS_FIM": (
        "PROGRAMA\nESCREVA 1\nFIM_PROGRAMA\nESCREVA 2",
        "Não é permitido escrever comandos depois de FIM_PROGRAMA",
    ),
    "ERRO_MISTURA_E_OU": (
        "PROGRAMA\nx = VERDADE E FALSO OU VERDADE\nFIM_PROGRAMA",
        "Não misture E com OU sem parênteses",
    ),
    "ERRO_PARENTESE_NAO_FECHADO": (
        "PROGRAMA\nx = (10 + 2\nFIM_PROGRAMA",
        "Eu esperava o parêntese de fechamento )",
    ),
    "ERRO_EXPRESSAO_INCOMPLETA": (
        "PROGRAMA\nx = 10 +\nFIM_PROGRAMA",
        "Eu esperava um valor",
    ),
}


class TestarParser(unittest.TestCase):
    def verificar_caso(self, nome):
        codigo, mensagem_esperada = ERROS_SINTATICOS[nome]
        mensagem = testar_erro(codigo)
        self.assertIsNotNone(mensagem, f"{nome}: o parser não identificou o erro")
        self.assertIn(mensagem_esperada, mensagem, f"{nome}: mensagem inesperada: {mensagem}")

    def test_inicio_programa(self):
        self.verificar_caso("ERRO_INICIO_PROGRAMA")

    def test_fim_programa(self):
        self.verificar_caso("ERRO_FIM_PROGRAMA")

    def test_sem_fim_se(self):
        self.verificar_caso("ERRO_SEM_FIM_SE")

    def test_sem_fim_enquanto(self):
        self.verificar_caso("ERRO_SEM_FIM_ENQUANTO")

    def test_sem_fim_repita(self):
        self.verificar_caso("ERRO_SEM_FIM_REPITA")

    def test_sem_entao(self):
        self.verificar_caso("ERRO_SEM_ENTAO")

    def test_sem_faca(self):
        self.verificar_caso("ERRO_SEM_FACA")

    def test_atribuicao_sem_igual(self):
        self.verificar_caso("ERRO_ATRIBUICAO_SEM_IGUAL")

    def test_varias_instrucoes_na_linha(self):
        self.verificar_caso("ERRO_VARIAS_INSTRUCOES_NA_LINHA")

    def test_comparacao_encadeada(self):
        self.verificar_caso("ERRO_COMPARACAO_ENCADEADA")

    def test_programa_duplicado(self):
        self.verificar_caso("ERRO_PROGRAMA_DUPLICADO")

    def test_comando_apos_fim(self):
        self.verificar_caso("ERRO_COMANDO_APOS_FIM")

    def test_mistura_e_ou(self):
        self.verificar_caso("ERRO_MISTURA_E_OU")

    def test_parentese_nao_fechado(self):
        self.verificar_caso("ERRO_PARENTESE_NAO_FECHADO")

    def test_expressao_incompleta(self):
        self.verificar_caso("ERRO_EXPRESSAO_INCOMPLETA")

    def test_programa_valido(self):
        codigo = "PROGRAMA\nx = 10\nESCREVA x\nFIM_PROGRAMA"
        ast, quantidade_nos = analisar_sintaxe(tokenizar(codigo))
        self.assertEqual(ast.tipo, "Programa")
        self.assertGreater(quantidade_nos, 0)


if __name__ == "__main__":
    unittest.main()
