from lexer import tokenizar, imprimir

if __name__ == "__main__":
    programa = 1
    
    exemplos = ["x = 5", "CONSTANTE fahrenheit_con = 32 \n celsius = 25 \n converter_fah = ((celsius * 9) / 5) + fahrenheit_con"]

    for code in exemplos:
        print(f"Programa {programa}")
        tokens_cod = tokenizar(code)
        imprimir(tokens_cod)

        programa += 1