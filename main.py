from lexer import tokenizar, imprimir

if __name__ == "__main__":
    programa = 1
    
    exemplos = ["x = 5", 
                "CONSTANTE fahrenheit_con = 32 \n celsius = 25 \n converter_fah = ((celsius * 9) / 5) + fahrenheit_con",
                """
                PROGRAMA

                lim = 10
                soma = 0

                ANOTA: Repetir instrucoes 10 vezes
                REPITA lim VEZES:

                soma = soma + 2

                ANOTA: Caso a soma ultrapasse 10, pare a repeticao
                SE soma MAIOR_OU_IGUAL 10 ENTAO:
                PARAR
                FIM_SE

                FIM_REPITA

                ESCREVA "Soma: " + soma
                FIM_PROGRAMA
                """,
                "1_acento = 30",
                """
                ENQUANTO x MENOR_QUE 10 FAÇA:
                x++ 
                """,
                "SE x % 2 == 0 ENTAO:"]

    for code in exemplos:
        print(f"Programa {programa}")
        tokens_cod = tokenizar(code)
        imprimir(tokens_cod)

        programa += 1