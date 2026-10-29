# Tabela de tokens
import re

# Letras aceitas em identificadores. O documento usa apenas ASCII ("a-zA-Z").
_LETRAS = "a-zA-Z"

# Categorias - token -> regex
_PALAVRAS_RESERVADAS = {
    "KW_PROGRAMA":     r"\bPROGRAMA\b",
    "KW_FIM_PROGRAMA": r"\bFIM_PROGRAMA\b",
    "KW_SE":           r"\bSE\b",
    "KW_ENTAO":        r"\bENTAO\b",
    "KW_SENAO":        r"\bSENAO\b",
    "KW_FIM_SE":       r"\bFIM_SE\b",
    "KW_ENQUANTO":     r"\bENQUANTO\b",
    "KW_FACA":         r"\bFACA\b",
    "KW_FIM_ENQUANTO": r"\bFIM_ENQUANTO\b",
    "KW_REPITA":       r"\bREPITA\b",
    "KW_VEZES":        r"\bVEZES\b",
    "KW_FIM_REPITA":   r"\bFIM_REPITA\b",
    "KW_PARAR":        r"\bPARAR\b",
    "KW_CONST":        r"\bCONSTANTE\b",
    "KW_ESCREVA":      r"\bESCREVA\b",
    "KW_LEIA":         r"\bLEIA\b",
}

_LITERAIS = {
    "L_NUM":        r"[0-9]+(?:\.[0-9]+)?",
    "L_TEXTO":      r'"[^"\r\n]*"',
    "L_VERDADEIRO": r"\bVERDADE\b",
    "L_FALSO":      r"\bFALSO\b",
}

_OP_ARITMETICOS = {
    "OPA_ADI":   r"\+",
    "OPA_SUB":   r"-",
    "OPA_MUL":   r"\*",
    "OPA_DIV":   r"/",
    "OPA_RESTO": r"\bRESTO_DE\b",
}

_OP_RELACIONAIS = {
    "OPR_IGUAL":       r"\bIGUAL_A\b",
    "OPR_N_IGUAL":     r"\bDIFERENTE_DE\b",
    "OPR_MENOR_Q":     r"\bMENOR_QUE\b",
    "OPR_MAIOR_Q":     r"\bMAIOR_QUE\b",
    "OPR_MENOR_IGUAL": r"\bMENOR_OU_IGUAL\b",
    "OPR_MAIOR_IGUAL": r"\bMAIOR_OU_IGUAL\b",
}

_OP_LOGICOS = {
    "OPL_E":  r"\bE\b",
    "OPL_OU": r"\bOU\b",
    "OPL_N":  r"\bNAO\b",
}

_ATRIBUICAO = {
    "OP_ATRIBUIR": r"=",
}

_DELIMITADORES = {
    "S_2_PONTOS":    r":",
    "S_E_PARENTESE": r"\(",
    "S_D_PARENTESE": r"\)",
}

_OUTROS = {
    "COMENTAR":     r"\bANOTA\b[^\r\n]*",
    "QUEBRA_LINHA": r"(?:\r?\n[ \t]*)+",
}

# O regex de ID precisa da lista de palavras reservadas. 
# Ela é montada automaticamente a partir das categorias acima
# todo padrão no formato \bPALAVRA\b é uma palavra reservada.
_PADRAO_PALAVRA_FIXA = re.compile(r"\\b([A-Z_]+)\\b")


def _lexemas_reservados():
    lexemas = {"ANOTA"}  # o regex de COMENTAR tem mais coisa além da palavra
    for categoria in (_PALAVRAS_RESERVADAS, _LITERAIS, _OP_ARITMETICOS,
                      _OP_RELACIONAIS, _OP_LOGICOS):
        for padrao in categoria.values():
            m = _PADRAO_PALAVRA_FIXA.fullmatch(padrao)
            if m:
                lexemas.add(m.group(1))
    return lexemas


RESERVADAS = "|".join(sorted(_lexemas_reservados(), key=len, reverse=True))

_IDENTIFICADOR = {
    "ID": rf"\b(?!(?:{RESERVADAS})\b)[{_LETRAS}_][{_LETRAS}0-9_]*",
}

# Tokens para identificar erros léxicos
# O Regex de ERRO_LETRA_ACENTUADA precisa dos ACENTOS para identificar o erro com letras acentuadas
# Esses erros além de identificarem erros comuns, como um nome de váriavel errado, Possui erros identificando símbolos comuns de outras linguagem de programação
# Assim dando possibilidade de reportar ao aluno qual símbolo correto utilizar
_ACENTOS = "À-ÖØ-öø-ÿ"

_ERROS_LEXICOS = {
    "ERRO_VAR_COM_NUM": rf"[0-9]+(?:\.[0-9]+)?[{_LETRAS}_][{_LETRAS}0-9_]*",
    "ERRO_NUMERO_INCOMPLETO": r"[0-9]+(?:\.[0-9]+){2,}|[0-9]+\.(?![0-9])|\.[0-9]+", 
    "ERRO_DECIMAL_VIRGULA": r"[0-9]+,[0-9]+",
    "ERRO_LETRA_ACENTUADA": rf"(?=[{_LETRAS}0-9_]*[{_ACENTOS}])[{_LETRAS}_{_ACENTOS}][{_LETRAS}0-9_{_ACENTOS}]*",
    "ERRO_TEXTO_ABERTO": r'"[^"\r\n]*', 
    "ERRO_ASPAS_SIMPLES": r"['‘’][^'‘’\r\n]*['‘’]?",
    "ERRO_COMPARADOR_SIMBOLO": r"==|!=|<>|<=|>=|=<|=>|<|>", 
    "ERRO_LOGICO_SIMBOLO": r"&&|\|\||[&|!]",
    "ERRO_RESTO_SIMBOLO": r"%",
    "ERRO_ATRIBUICAO_COMPOSTA": r"\+\+|--|[+\-*/]=",
    "ERRO_FIM_SIMBOLO": r";",
    "ERRO_BLOCO_SIMBOLO": r"[{}]",
    "ERRO_COLCHETES_SIMBOLO": r"[\[\]]",
    "ERRO_COMENTARIO_SIMBOLO": r"#[^\r\n]*|//[^\r\n]*|/\*[^\r\n]*",
    "ERRO": r".",
}


# DICIONÁRIO PRINCIPAL: categoria -> token: regex
TOKENS = {
    "PALAVRAS_RESERVADAS":    _PALAVRAS_RESERVADAS,
    "LITERAIS":               _LITERAIS,
    "IDENTIFICADOR":          _IDENTIFICADOR,
    "OPERADORES_ARITMETICOS": _OP_ARITMETICOS,
    "OPERADORES_RELACIONAIS": _OP_RELACIONAIS,
    "OPERADORES_LOGICOS":     _OP_LOGICOS,
    "ATRIBUICAO":             _ATRIBUICAO,
    "DELIMITADORES":          _DELIMITADORES,
    "OUTROS":                 _OUTROS,
    "ERROS_LEXICOS":          _ERROS_LEXICOS,
}

# token -> categoria para análise sintática
CATEGORIA_DO_TOKEN = {
    nome: categoria for categoria, tokens in TOKENS.items() for nome in tokens
}
