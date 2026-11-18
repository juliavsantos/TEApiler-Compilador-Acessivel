
import unittest
import os
import sys

pasta_atual = os.path.dirname(os.path.abspath(__file__))
pasta_raiz = os.path.dirname(pasta_atual)

if pasta_raiz not in sys.path:
    sys.path.insert(0, pasta_raiz)

from src.compilador.lexer import tokenizar
from src.estrutura_compilador.tokens_dict import TOKENS


def testar_erro(codigo):
    tokens_cod = tokenizar(codigo)

    for tok in tokens_cod:
        if tok.token in TOKENS["ERROS_LEXICOS"]:
            return tok.token

    return None


# Definindo casos de erros
ERROS_LEXICOS = {
    "ERRO_VAR_COM_NUM": "1x = 10",
    "ERRO_NUMERO_INCOMPLETO": "x = 3.",
    "ERRO_DECIMAL_VIRGULA": "x = 3,14",
    "ERRO_LETRA_ACENTUADA": "SE x ENTÃO:",
    "ERRO_TEXTO_ABERTO": "\"Seu texto aqui",
    "ERRO_ASPAS_SIMPLES": "'Seu texto aqui'",
    "ERRO_COMPARADOR_SIMBOLO": "SE x == 2 ENTAO:",
    "ERRO_LOGICO_SIMBOLO": "SE x && y ENTAO:",
    "ERRO_RESTO_SIMBOLO": "SE x % 2 IGUAL_A 0 ENTAO:",
    "ERRO_ATRIBUICAO_COMPOSTA": "x += 1",
    "ERRO_FIM_SIMBOLO": "x = 10;",
    "ERRO_BLOCO_SIMBOLO": "SE x ENTAO: { ESCREVA x }",
    "ERRO_COLCHETES_SIMBOLO": "x = [10]",
    "ERRO_COMENTARIO_SIMBOLO": "//comentario",
    "ERRO": "x = 10, 20"
}


class TestarLexer(unittest.TestCase):

    def test_var_num(self):
        cod = ERROS_LEXICOS["ERRO_VAR_COM_NUM"]
        self.assertEqual(testar_erro(cod), "ERRO_VAR_COM_NUM")

    def test_numero_incompleto(self):
        cod = ERROS_LEXICOS["ERRO_NUMERO_INCOMPLETO"]
        self.assertEqual(testar_erro(cod), "ERRO_NUMERO_INCOMPLETO")

    def test_decimal_virgula(self):
        cod = ERROS_LEXICOS["ERRO_DECIMAL_VIRGULA"]
        self.assertEqual(testar_erro(cod), "ERRO_DECIMAL_VIRGULA")

    def test_letra_acentuada(self):
        cod = ERROS_LEXICOS["ERRO_LETRA_ACENTUADA"]
        self.assertEqual(testar_erro(cod), "ERRO_LETRA_ACENTUADA")

    def test_texto_aberto(self):
        cod = ERROS_LEXICOS["ERRO_TEXTO_ABERTO"]
        self.assertEqual(testar_erro(cod), "ERRO_TEXTO_ABERTO")

    def test_aspas_simples(self):
        cod = ERROS_LEXICOS["ERRO_ASPAS_SIMPLES"]
        self.assertEqual(testar_erro(cod), "ERRO_ASPAS_SIMPLES")

    def test_comparador_simbolo(self):
        cod = ERROS_LEXICOS["ERRO_COMPARADOR_SIMBOLO"]
        self.assertEqual(testar_erro(cod), "ERRO_COMPARADOR_SIMBOLO")

    def test_logico_simbolo(self):
        cod = ERROS_LEXICOS["ERRO_LOGICO_SIMBOLO"]
        self.assertEqual(testar_erro(cod), "ERRO_LOGICO_SIMBOLO")

    def test_resto_simbolo(self):
        cod = ERROS_LEXICOS["ERRO_RESTO_SIMBOLO"]
        self.assertEqual(testar_erro(cod), "ERRO_RESTO_SIMBOLO")

    def test_atribuicao_composta(self):
        cod = ERROS_LEXICOS["ERRO_ATRIBUICAO_COMPOSTA"]
        self.assertEqual(testar_erro(cod), "ERRO_ATRIBUICAO_COMPOSTA")

    def test_fim_simbolo(self):
        cod = ERROS_LEXICOS["ERRO_FIM_SIMBOLO"]
        self.assertEqual(testar_erro(cod), "ERRO_FIM_SIMBOLO")

    def test_bloco_simbolo(self):
        cod = ERROS_LEXICOS["ERRO_BLOCO_SIMBOLO"]
        self.assertEqual(testar_erro(cod), "ERRO_BLOCO_SIMBOLO")

    def test_colchetes_simbolo(self):
        cod = ERROS_LEXICOS["ERRO_COLCHETES_SIMBOLO"]
        self.assertEqual(testar_erro(cod), "ERRO_COLCHETES_SIMBOLO")

    def test_comentario_simbolo(self):
        cod = ERROS_LEXICOS["ERRO_COMENTARIO_SIMBOLO"]
        self.assertEqual(testar_erro(cod), "ERRO_COMENTARIO_SIMBOLO")

    def test_erro_generico(self):
        cod = ERROS_LEXICOS["ERRO"]
        self.assertEqual(testar_erro(cod), "ERRO")


if __name__ == "__main__":
    unittest.main()
