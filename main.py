from src.compilador.lexer import tokenizar, imprimir
from src.compilador.parser import analisar_sintaxe

if __name__ == "__main__":
    programa = 1
    
    exemplos = ["""
                PROGRAMA

                x = 5 

                ESCREVA x

                FIM_PROGRAMA
                """,
                """
                PROGRAMA

                x = 10

                SE x MENOR_QUE 10:
                ESCREVA "menor"

                FIM_PROGRAMA
                """]

    for code in exemplos:
        print(f"Programa {programa}")
        tokens_cod = tokenizar(code)
        imprimir(tokens_cod)

        analisar_sintaxe(tokens_cod)

        programa += 1