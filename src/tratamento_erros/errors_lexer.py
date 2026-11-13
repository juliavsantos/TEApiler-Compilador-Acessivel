# Mensagens de erros léxicos
_MENSAGENS_ERROS = {
    "ERRO_VAR_COM_NUM": "Opa! O nome da sua variável \"{lexema}\" não pode começar com números ou símbolos... Por favor, reescreva o nome da sua variável | Exemplo: \"var\"",
    "ERRO_NUMERO_INCOMPLETO": "Opa! Seu número decimal {lexema} está incompleto... Por favor, verifique se seu número decimal tem um número antes e depois do \".\" | Exemplo: 3.14",
    "ERRO_DECIMAL_VIRGULA": "Opa! Seu número decimal {lexema} está usando \",\" invés de \".\"... Por favor, verifique se seu número decimal tem um número antes e depois do \".\" | Exemplo: 3.14",
    "ERRO_LETRA_ACENTUADA": "Opa! A sua palavra ou variável {lexema} está usando acentos... Por favor, não use acentos em palavras reservadas ou váriaveis | Exemplo: ENTAO",
    "ERRO_TEXTO_ABERTO": "Opa! Seu texto {lexema} não está com as aspas fechadas... Por favor, tenha certeza que todo texto esteja em volta de \" e \" | Exemplo: \"Seu texto aqui\"",
    "ERRO_ASPAS_SIMPLES": "Opa! Seu texto {lexema} não está usando aspas duplas... Por favor, tenha certeza que todo texto esteja em volta de \" e \" e não ' e ' | Exemplo: \"Seu texto aqui\"",
    "ERRO_COMPARADOR_SIMBOLO": "Opa! O comparador {lexema} está usando um símbolo de outra linguagem...",
    "ERRO_LOGICO_SIMBOLO": "Opa! O símbolo lógico {lexema} está usando um símbolo de outra linguagem...",
    "ERRO_RESTO_SIMBOLO": "Opa! O símbolo de resto {lexema} está usando um símbolo de outra linguagem...",
    "ERRO_ATRIBUICAO_COMPOSTA": "Opa! Esse símbolo de atribuição {lexema} não existe nessa linguagem... Para atribuir um valor a uma variável use \"=\" | Exemplo: soma = soma + 1 ou soma = soma + var",
    "ERRO_FIM_SIMBOLO": "Opa! Esse símbolo de conclusão {lexema} não existe nessa linguagem... Não precisa digitar nada quando terminar um comando, apenas em estruturas condicionais e repetição com \":\" | Exemplo: ENTAO: ou VEZES:",
    "ERRO_BLOCO_SIMBOLO": "Opa! Esse símbolo de bloco {lexema} não existe nessa linguagem... Apenas use espaços quando entrar em uma estrutura condicional ou de repetição",
    "ERRO_COLCHETES_SIMBOLO": "Opa! Colchetes {lexema} não existe nessa linguagem",
    "ERRO_COMENTARIO_SIMBOLO": "Opa! Esse símbolo de comentário {lexema} não existe nessa linguagem... Use sempre \"ANOTA:\" quando for comentar algo no código. | Exemplo: ANOTA: Isso é um comentário",
    "ERRO": "Opa! Esse símbolo {lexema} não existe nessa linguagem"
}

# Sugestões válidas para a linguagem
_SUGESTOES = {
    "==": "IGUAL_A",
    "!=": "DIFERENTE_DE",
    "<>": "DIFERENTE_DE",
    "<":  "MENOR_QUE",
    ">":  "MAIOR_QUE",
    "<=": "MENOR_OU_IGUAL",
    ">=": "MAIOR_OU_IGUAL",
    "=<": "MENOR_OU_IGUAL",
    "=>": "MAIOR_OU_IGUAL",
    "&&": "E",   "&": "E",
    "||": "OU",  "|": "OU",
    "!":  "NAO",
    "%":  "RESTO_DE",
}

def sugerir_sintaxe(lexema):
    sugestao = _SUGESTOES.get(lexema)

    if sugestao:
        return f"Você quis dizer {sugestao}?"

    return ""
    

def formatar_mensagem(token):
    mensagem = _MENSAGENS_ERROS.get(token.token, _MENSAGENS_ERROS["ERRO"])

    mensagem += sugerir_sintaxe(token.lexema)

    return mensagem.format(lexema=token.lexema)