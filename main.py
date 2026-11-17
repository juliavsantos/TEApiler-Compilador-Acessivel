from src.compilador.lexer import tokenizar, imprimir
from src.compilador.parser import analisar_sintaxe
from src.compilador.semantic import analisar_semantica

if __name__ == "__main__":
    programa = 1
    
    exemplos = ["""
                PROGRAMA

                ENQUANTO VERDADE FACA:

                ESCREVA "ola"

                FIM_ENQUANTO

                FIM_PROGRAMA
                """,
                ]   

    for code in exemplos:
        print(f"Programa {programa}")
        tokens_cod = tokenizar(code)

        ast, _ = analisar_sintaxe(tokens_cod)

        ast_anot = analisar_semantica(ast)

        programa += 1