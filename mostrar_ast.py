"""Mostra a AST de um programa como árvore de texto (para o diário da Sprint 3).
Salve na raiz do repositório (ao lado de parser.py e lexer.py).
Uso:
    python3 mostrar_ast.py                # mostra dois exemplos prontos
    python3 mostrar_ast.py programa.txt   # mostra a AST do seu arquivo
"""
import sys
from src.compilador.lexer import tokenizar
from src.compilador.parser import analisar_sintaxe
from src.tratamento_erros.errors_parser import ErroParser, reportar_erro_sintatico

EXEMPLOS = {
    "Exemplo 1": 'PROGRAMA\n  x = 2 * (3 + 1)\nFIM_PROGRAMA',
    "Exemplo 2": 'PROGRAMA\n  idade = 20\n  SE idade MAIOR_OU_IGUAL 18 ENTAO\n    ESCREVA "Maior de idade"\n  SENAO\n    ESCREVA "Menor de idade"\n  FIM_SE\nFIM_PROGRAMA',
}


def arvore(d, prefixo="", ultimo=True, rotulo="", raiz=False):
    extras = {k: v for k, v in d.items() if k != "tipo" and not isinstance(v, (dict, list))}
    nome = d["tipo"] + "".join(f" {k}={v!r}" for k, v in extras.items())
    if raiz:
        linhas, pref_f = [nome], ""
    else:
        linhas = [prefixo + ("└─ " if ultimo else "├─ ") + (rotulo + ": " if rotulo else "") + nome]
        pref_f = prefixo + ("   " if ultimo else "│  ")
    filhos = [(k, v) for k, v in d.items() if isinstance(v, dict) or (isinstance(v, list) and v)]
    for i, (k, v) in enumerate(filhos):
        fim = i == len(filhos) - 1
        if isinstance(v, dict):
            linhas += arvore(v, pref_f, fim, k)
        else:
            for j, item in enumerate(v):
                linhas += arvore(item, pref_f, fim and j == len(v) - 1, k if j == 0 else "")
    return linhas


def mostrar(titulo, codigo):
    try:
        ast, nos = analisar_sintaxe(tokenizar(codigo.strip()))
    except ErroParser as e:
        print(f"### {titulo}\n{reportar_erro_sintatico(e)}\n")
        return
    print(f"### {titulo} ({nos} nós)")
    print("\n".join(arvore(ast.para_dict(), raiz=True)))
    print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        mostrar(sys.argv[1], open(sys.argv[1], encoding="utf-8").read())
    else:
        for t, c in EXEMPLOS.items():
            mostrar(t, c)
