import re
from typing import NamedTuple
from tokens_dict import TOKENS, CATEGORIA_DO_TOKEN
import errors_lexer


# Analisador léxico mínimo, só para testar a tabela.
# NÃO fazem parte da tabela do documento (adições necessárias para o teste):
#   - espaços e tabs são ignorados
#   - ERRO: qualquer caractere que nenhuma regra reconhece
#   - EOF: fim da entrada
# Regras: maior casamento vence; em empate, vale a ordem do dicionário.

_IGNORAR = re.compile(r"[ \t]+")
_TABELA = [(nome, re.compile(padrao))
           for tokens in TOKENS.values() for nome, padrao in tokens.items()]


class Token(NamedTuple):
    token: str
    categoria: str
    lexema: str
    linha: int


def tokenizar(codigo):
    """
    Devolve a lista de Token do código. 
    Não levanta exceção: erros viram token ERRO.
    """
    pos, linha, saida = 0, 1, []
    while pos < len(codigo):
        # Tratamento para ignorar espaços
        ign = _IGNORAR.match(codigo, pos)
        if ign:
            pos = ign.end()
            continue

        # Verificando se uma palavra é um token existente
        melhor = None  # (nome, fim)
        for nome, rx in _TABELA:
            m = rx.match(codigo, pos)
            if m and m.end() > pos and (melhor is None or m.end() > melhor[1]):
                melhor = (nome, m.end())

        # Caso encontre um erro inesperado, não mapeado nos tokens de erro
        # Associe token a "ERRO" generico e continue a tokenizacao
        if melhor is None:
            nome, fim = "ERRO", pos + 1
        else:
            nome, fim = melhor
        lexema = codigo[pos:fim]

        # Descartando linhas de comentário e quebras de linha
        descartar = (nome == "COMENTAR") or (
            nome == "QUEBRA_LINHA" and saida and saida[-1].token == "QUEBRA_LINHA")
        if not descartar:
            saida.append(Token(nome, CATEGORIA_DO_TOKEN.get(nome, "ERRO"), lexema, linha))

        linha += lexema.count("\n")
        pos = fim

    saida.append(Token("EOF", "FIM", "", linha))
    return saida


def imprimir(tokens):
    print(f"{'LINHA':<6}{'CATEGORIA':<25}{'TOKEN':<25}LEXEMA")
    for t in tokens:
        print(f"{t.linha:<6}{t.categoria:<25}{t.token:<25}{t.lexema!r}")

        if t.token in TOKENS["ERROS_LEXICOS"]:
            print(f"ERRO na linha {t.linha}: {errors_lexer.formatar_mensagem(t)}")