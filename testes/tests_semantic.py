import unittest
import os
import sys

pasta_atual = os.path.dirname(os.path.abspath(__file__))
pasta_raiz = os.path.dirname(pasta_atual)

if pasta_raiz not in sys.path:
    sys.path.insert(0, pasta_raiz)

from src.compilador.lexer import tokenizar
from src.compilador.parser import analisar_sintaxe
from src.compilador.semantic import analisar_semantica
from src.tratamento_erros.errors_semantic import reportar_erro, reportar_aviso


def analisar_codigo(codigo):
    """Executa lexer, parser e analisador semântico para um programa."""
    ast, _ = analisar_sintaxe(tokenizar(codigo))
    return analisar_semantica(ast, parar_no_primeiro_erro=False)


# Erros: identificador esperado -> código de entrada.
ERROS_SEMANTICOS = {
    "ERRO_VAR_NAO_DECLARADA": "PROGRAMA\nESCREVA valor\nFIM_PROGRAMA",
    "ERRO_PARAR": "PROGRAMA\nPARAR\nFIM_PROGRAMA",
    "ERRO_ATRIBUIR_CONSTANTE": (
        "PROGRAMA\nCONSTANTE limite = 10\nlimite = 20\nFIM_PROGRAMA"
    ),
    "ERRO_LER_CONSTANTE": (
        "PROGRAMA\nCONSTANTE limite = 10\nLEIA limite\nFIM_PROGRAMA"
    ),
    "ERRO_DECLARADO_CONSTANTE": (
        "PROGRAMA\nCONSTANTE limite = 10\nCONSTANTE limite = 20\nFIM_PROGRAMA"
    ),
    "ERRO_CONSTANTE_COM_VARIAVEL": (
        "PROGRAMA\nx = 10\nCONSTANTE limite = x\nFIM_PROGRAMA"
    ),
    "ERRO_REPITA_TIPO": (
        'PROGRAMA\nREPITA "texto" VEZES\nESCREVA 1\nFIM_REPITA\nFIM_PROGRAMA'
    ),
    "ERRO_REPITA_NEGATIVO": (
        "PROGRAMA\nREPITA -2 VEZES\nESCREVA 1\nFIM_REPITA\nFIM_PROGRAMA"
    ),
    "ERRO_REPITA_DECIMAL": (
        "PROGRAMA\nREPITA 2.5 VEZES\nESCREVA 1\nFIM_REPITA\nFIM_PROGRAMA"
    ),
    "ERRO_CONDICIONAL_TIPO": (
        "PROGRAMA\nSE 10 ENTAO\nESCREVA 1\nFIM_SE\nFIM_PROGRAMA"
    ),
    "ERRO_CONTA_TEXTO": 'PROGRAMA\nx = "texto" - 2\nFIM_PROGRAMA',
    "ERRO_CONTA_LOGICO": "PROGRAMA\nx = VERDADE + 2\nFIM_PROGRAMA",
    "ERRO_DIVIDIR_ZERO": "PROGRAMA\nx = 10 / 0\nFIM_PROGRAMA",
    "ERRO_RESTO_ZERO": "PROGRAMA\nx = 10 RESTO_DE 0\nFIM_PROGRAMA",
    "ERRO_COMPARAR_LOGICO": (
        "PROGRAMA\nx = VERDADE MAIOR_QUE FALSO\nFIM_PROGRAMA"
    ),
    "ERRO_COMPARAR_TIPO": (
        'PROGRAMA\nx = 10 MAIOR_QUE "dez"\nFIM_PROGRAMA'
    ),
    "ERRO_IGUAL_TIPO": (
        'PROGRAMA\nx = 10 IGUAL_A "10"\nFIM_PROGRAMA'
    ),
    "ERRO_LOGICO_TIPO": "PROGRAMA\nx = 10 E VERDADE\nFIM_PROGRAMA",
    "ERRO_VAR_DECLARADA_BLOCO": (
        "PROGRAMA\nSE VERDADE ENTAO\nx = 10\nFIM_SE\nESCREVA x\nFIM_PROGRAMA"
    ),
}


# Avisos: identificador esperado -> código de entrada.
AVISOS_SEMANTICOS = {
    "AVISO_LOOP_INFINITO": (
        "PROGRAMA\nENQUANTO VERDADE FACA\nESCREVA 1\nFIM_ENQUANTO\nFIM_PROGRAMA"
    ),
    "AVISO_LOOP_INFINITO_B": (
        "PROGRAMA\nx = 1\nENQUANTO x MAIOR_QUE 0 FACA\nESCREVA x\nFIM_ENQUANTO\nFIM_PROGRAMA"
    ),
    "AVISO_BLOCO_VAZIO": (
        "PROGRAMA\nENQUANTO VERDADE FACA\nFIM_ENQUANTO\nFIM_PROGRAMA"
    ),
    "AVISO_NOME_RESERVADO": "PROGRAMA\nprograma = 10\nFIM_PROGRAMA",
    "AVISO_PARAR_DEPOIS": (
        "PROGRAMA\nENQUANTO VERDADE FACA\nPARAR\nESCREVA 1\nFIM_ENQUANTO\nFIM_PROGRAMA"
    ),
}


class TestarSemantico(unittest.TestCase):
    def verificar_erro(self, caso):
        entrada = ERROS_SEMANTICOS[caso]
        if isinstance(entrada, tuple):
            codigo, esperado = entrada
        else:
            codigo, esperado = entrada, caso
        resultado = analisar_codigo(codigo)
        codigos = [erro.codigo for erro in resultado.erros]
        self.assertIn(esperado, codigos, f"Erros encontrados: {codigos}")
        erro = next(item for item in resultado.erros if item.codigo == esperado)
        mensagem = reportar_erro(erro)
        self.assertIn("Erro:", mensagem)
        self.assertTrue(erro.mensagem.strip())

    def verificar_aviso(self, codigo_esperado):
        resultado = analisar_codigo(AVISOS_SEMANTICOS[codigo_esperado])
        codigos = [aviso.codigo for aviso in resultado.avisos]
        self.assertIn(codigo_esperado, codigos, f"Avisos encontrados: {codigos}")
        aviso = next(item for item in resultado.avisos if item.codigo == codigo_esperado)
        mensagem = reportar_aviso(aviso)
        self.assertIn("Aviso:", mensagem)
        self.assertTrue(aviso.mensagem.strip())

    def test_variavel_nao_declarada(self): self.verificar_erro("ERRO_VAR_NAO_DECLARADA")
    def test_parar_fora_laco(self): self.verificar_erro("ERRO_PARAR")
    def test_alterar_constante(self): self.verificar_erro("ERRO_ATRIBUIR_CONSTANTE")
    def test_ler_constante(self): self.verificar_erro("ERRO_LER_CONSTANTE")
    def test_constante_duplicada(self): self.verificar_erro("ERRO_DECLARADO_CONSTANTE")
    def test_constante_com_variavel(self): self.verificar_erro("ERRO_CONSTANTE_COM_VARIAVEL")
    def test_repita_tipo_invalido(self): self.verificar_erro("ERRO_REPITA_TIPO")
    def test_repita_negativo(self): self.verificar_erro("ERRO_REPITA_NEGATIVO")
    def test_repita_decimal(self): self.verificar_erro("ERRO_REPITA_DECIMAL")
    def test_condicao_tipo_invalido(self): self.verificar_erro("ERRO_CONDICIONAL_TIPO")
    def test_conta_com_texto(self): self.verificar_erro("ERRO_CONTA_TEXTO")
    def test_conta_com_logico(self): self.verificar_erro("ERRO_CONTA_LOGICO")
    def test_divisao_por_zero(self): self.verificar_erro("ERRO_DIVIDIR_ZERO")
    def test_resto_por_zero(self): self.verificar_erro("ERRO_RESTO_ZERO")
    def test_comparar_logicos_com_ordem(self): self.verificar_erro("ERRO_COMPARAR_LOGICO")
    def test_comparar_tipos_diferentes_com_ordem(self): self.verificar_erro("ERRO_COMPARAR_TIPO")
    def test_igualdade_tipos_diferentes(self): self.verificar_erro("ERRO_IGUAL_TIPO")
    def test_operacao_logica_tipo_invalido(self): self.verificar_erro("ERRO_LOGICO_TIPO")
    def test_variavel_declarada_em_bloco(self): self.verificar_erro("ERRO_VAR_DECLARADA_BLOCO")
    def test_loop_infinito_literal(self): self.verificar_aviso("AVISO_LOOP_INFINITO")
    def test_loop_infinito_variavel(self): self.verificar_aviso("AVISO_LOOP_INFINITO_B")
    def test_bloco_vazio(self): self.verificar_aviso("AVISO_BLOCO_VAZIO")
    def test_nome_reservado(self): self.verificar_aviso("AVISO_NOME_RESERVADO")
    def test_comando_apos_parar(self): self.verificar_aviso("AVISO_PARAR_DEPOIS")

    def test_programa_sem_erros(self):
        codigo = "PROGRAMA\nx = 10\nESCREVA x\nFIM_PROGRAMA"
        resultado = analisar_codigo(codigo)
        self.assertTrue(resultado.ok)
        self.assertEqual(resultado.erros, [])


if __name__ == "__main__":
    unittest.main()