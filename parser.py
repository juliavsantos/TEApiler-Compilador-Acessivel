
"""
Análise sintática

Gramática (EBNF) implementada:
  programa   -> PROGRAMA bloco FIM_PROGRAMA
  bloco      -> { comando }
  comando    -> ID "=" expr | CONSTANTE ID "=" expr | ESCREVA expr | LEIA ID | PARAR
              | SE expr ENTAO [":"] bloco [SENAO [":"] bloco] FIM_SE
              | ENQUANTO expr FACA [":"] bloco FIM_ENQUANTO
              | REPITA expr VEZES [":"] bloco FIM_REPITA
  expr       -> neg { E neg } | neg { OU neg }
                (misturar E com OU exige parênteses)
  neg        -> [NAO] comparacao
  comparacao -> soma [ op_rel soma ]
                (sem comparação encadeada)
  soma       -> termo { ("+"|"-") termo }
  termo      -> fator { ("*"|"/"|RESTO_DE) fator }
  fator      -> NUM | TEXTO | VERDADE | FALSO | ID | "(" expr ")" | "-" fator

Uma instrução por linha (QUEBRA_LINHA termina o comando).
"""

from lexer import RESERVADAS
from errors_parser import ErroParser


RESERVADAS_SET = set(RESERVADAS.split("|"))

FIM_BLOCO = {
    "KW_FIM_PROGRAMA",
    "KW_FIM_SE",
    "KW_SENAO",
    "KW_FIM_ENQUANTO",
    "KW_FIM_REPITA",
    "EOF"
}

OPS_REL = {
    "OPR_IGUAL",
    "OPR_N_IGUAL",
    "OPR_MENOR_Q",
    "OPR_MAIOR_Q",
    "OPR_MENOR_IGUAL",
    "OPR_MAIOR_IGUAL"
}


class No:
    """Nó da AST: tipo + posição + campos específicos."""

    def __init__(self, tipo, tok, **campos):
        self.tipo = tipo
        self.linha = tok.linha
        self.coluna = tok.coluna
        self.__dict__.update(campos)

    def para_dict(self):
        def conv(v):
            if isinstance(v, No):
                return v.para_dict()
            if isinstance(v, list):
                return [conv(x) for x in v]
            return v

        d = {"tipo": self.tipo}
        d.update({
            k: conv(v)
            for k, v in self.__dict__.items()
            if k not in ("tipo", "linha", "coluna")
        })

        return d


def descrever(tok):
    if tok.token == "QUEBRA_LINHA":
        return "o fim da linha"

    if tok.token == "EOF":
        return "o fim do programa"

    return f'"{tok.lexema}"'


class Parser:

    def __init__(self, tokens):
        self.t = tokens
        self.i = 0
        self.nos = 0

    @property
    def atual(self):
        return self.t[self.i]

    def e(self, *tipos):
        return self.atual.token in tipos

    def prox(self):
        return self.t[min(self.i + 1, len(self.t) - 1)]

    def erro(self, msg, tok=None):
        """Encaminha o erro sintático para o módulo de tratamento."""
        raise ErroParser(msg, tok or self.atual)

    def avancar(self):
        tok = self.atual

        if tok.token != "EOF":
            self.i += 1

        return tok

    def esperar(self, tipo, texto):
        if not self.e(tipo):
            self.erro(
                f"Eu esperava {texto}, mas encontrei "
                f"{descrever(self.atual)}."
            )

        return self.avancar()

    def no(self, tipo, tok, **c):
        self.nos += 1
        return No(tipo, tok, **c)

    def pular_linhas(self):
        while self.e("QUEBRA_LINHA"):
            self.avancar()

    def fim_linha(self):
        if self.e("QUEBRA_LINHA"):
            self.pular_linhas()

        elif not self.e("EOF"):
            self.erro(
                f"Escreva uma instrução por linha. Depois da instrução, "
                f"comece uma nova linha (encontrei {descrever(self.atual)})."
            )

    def dois_pontos(self):
        if self.e("S_2_PONTOS"):
            self.avancar()

    def fechar(self, tipo, palavra, abre, nome):
        if not self.e(tipo):
            self.erro(
                f"O {nome} da linha {abre.linha} não foi fechado. "
                f"Escreva {palavra} no final do bloco."
            )

        self.avancar()

    # ---- estrutura ----

    def programa(self):
        self.pular_linhas()
        ini = self.atual

        if not self.e("KW_PROGRAMA"):
            self.erro("Todo programa começa com a palavra PROGRAMA.")

        self.avancar()
        self.fim_linha()

        corpo = self.bloco()

        if not self.e("KW_FIM_PROGRAMA"):
            self.erro(
                f"Eu esperava FIM_PROGRAMA para terminar, "
                f"mas encontrei {descrever(self.atual)}."
            )

        self.avancar()
        self.pular_linhas()

        if not self.e("EOF"):
            self.erro("Depois de FIM_PROGRAMA não pode haver mais nada.")

        return self.no("Programa", ini, corpo=corpo)

    def bloco(self):
        lista = []
        self.pular_linhas()

        while not self.e(*FIM_BLOCO):
            lista.append(self.comando())
            self.fim_linha()

        return lista

    def comando(self):
        t = self.atual

        if t.token == "ID":
            if self.prox().token != "OP_ATRIBUIR":
                if t.lexema.upper() in RESERVADAS_SET:
                    self.erro(
                        f'"{t.lexema}" parece a palavra reservada '
                        f'{t.lexema.upper()}. Escreva em letras maiúsculas.'
                    )

                self.erro(
                    f'Depois do nome "{t.lexema}" eu esperava o sinal = '
                    f'(exemplo: {t.lexema} = 5).',
                    self.prox()
                )

            self.avancar()
            self.avancar()

            return self.no(
                "Atribuir",
                t,
                nome=t.lexema,
                valor=self.expr()
            )

        if t.token == "KW_CONST":
            self.avancar()
            nome = self.esperar("ID", "o nome da constante")
            self.esperar("OP_ATRIBUIR", "o sinal =")

            return self.no(
                "Constante",
                t,
                nome=nome.lexema,
                valor=self.expr()
            )

        if t.token == "KW_ESCREVA":
            self.avancar()

            return self.no(
                "Escreva",
                t,
                valor=self.expr()
            )

        if t.token == "KW_LEIA":
            self.avancar()
            nome = self.esperar("ID", "o nome de uma variável")

            return self.no(
                "Leia",
                t,
                nome=nome.lexema
            )

        if t.token == "KW_PARAR":
            self.avancar()
            return self.no("Parar", t)

        if t.token == "KW_SE":
            self.avancar()
            cond = self.expr()

            self.esperar("KW_ENTAO", "a palavra ENTAO")
            self.dois_pontos()
            self.fim_linha()

            entao = self.bloco()
            senao = []

            if self.e("KW_SENAO"):
                self.avancar()
                self.dois_pontos()
                self.fim_linha()
                senao = self.bloco()

            self.fechar("KW_FIM_SE", "FIM_SE", t, "SE")

            return self.no(
                "Se",
                t,
                condicao=cond,
                entao=entao,
                senao=senao
            )

        if t.token == "KW_ENQUANTO":
            self.avancar()
            cond = self.expr()

            self.esperar("KW_FACA", "a palavra FACA")
            self.dois_pontos()
            self.fim_linha()

            corpo = self.bloco()

            self.fechar(
                "KW_FIM_ENQUANTO",
                "FIM_ENQUANTO",
                t,
                "ENQUANTO"
            )

            return self.no(
                "Enquanto",
                t,
                condicao=cond,
                corpo=corpo
            )

        if t.token == "KW_REPITA":
            self.avancar()
            n = self.expr()

            self.esperar("KW_VEZES", "a palavra VEZES")
            self.dois_pontos()
            self.fim_linha()

            corpo = self.bloco()

            self.fechar(
                "KW_FIM_REPITA",
                "FIM_REPITA",
                t,
                "REPITA"
            )

            return self.no(
                "Repita",
                t,
                vezes=n,
                corpo=corpo
            )

        self.erro(
            f"Não entendi {descrever(t)} no começo da linha. "
            "Uma instrução começa com um nome, ESCREVA, LEIA, SE, "
            "ENQUANTO, REPITA, CONSTANTE ou PARAR."
        )

    # ---- expressões (um nível por precedência, sem ambiguidade) ----

    def expr(self):
        a = self.neg()
        op = None

        while self.e("OPL_E", "OPL_OU"):
            t = self.avancar()

            if op and t.token != op:
                self.erro(
                    "Não misture E com OU sem parênteses. "
                    "Exemplo: (a E b) OU c",
                    t
                )

            op = t.token

            a = self.no(
                "OpLogica",
                t,
                op=t.lexema,
                esq=a,
                dir=self.neg()
            )

        return a

    def neg(self):
        if self.e("OPL_N"):
            t = self.avancar()

            return self.no(
                "Nao",
                t,
                valor=self.comparacao()
            )

        return self.comparacao()

    def comparacao(self):
        a = self.soma()

        if self.e(*OPS_REL):
            t = self.avancar()
            b = self.soma()

            if self.e(*OPS_REL):
                self.erro(
                    "Compare dois valores por vez. "
                    "Exemplo: (x MAIOR_QUE 1) E (x MENOR_QUE 9)"
                )

            return self.no(
                "OpRelacional",
                t,
                op=t.lexema,
                esq=a,
                dir=b
            )

        return a

    def soma(self):
        a = self.termo()

        while self.e("OPA_ADI", "OPA_SUB"):
            t = self.avancar()

            a = self.no(
                "OpAritmetica",
                t,
                op=t.lexema,
                esq=a,
                dir=self.termo()
            )

        return a

    def termo(self):
        a = self.fator()

        while self.e("OPA_MUL", "OPA_DIV", "OPA_RESTO"):
            t = self.avancar()

            a = self.no(
                "OpAritmetica",
                t,
                op=t.lexema,
                esq=a,
                dir=self.fator()
            )

        return a

    def fator(self):
        t = self.atual

        if t.token == "L_NUM":
            self.avancar()

            valor = (
                float(t.lexema)
                if "." in t.lexema
                else int(t.lexema)
            )

            return self.no("Numero", t, valor=valor)

        if t.token == "L_TEXTO":
            self.avancar()

            return self.no(
                "Texto",
                t,
                valor=t.lexema[1:-1]
            )

        if t.token in ("L_VERDADEIRO", "L_FALSO"):
            self.avancar()

            return self.no(
                "Logico",
                t,
                valor=t.token == "L_VERDADEIRO"
            )

        if t.token == "ID":
            self.avancar()

            return self.no(
                "Variavel",
                t,
                nome=t.lexema
            )

        if t.token == "S_E_PARENTESE":
            self.avancar()
            e = self.expr()

            self.esperar(
                "S_D_PARENTESE",
                "o parêntese de fechamento )"
            )

            return e

        if t.token == "OPA_SUB":
            self.avancar()

            return self.no(
                "Negativo",
                t,
                valor=self.fator()
            )

        self.erro(
            f"Eu esperava um valor (número, texto, nome ou "
            f"VERDADE/FALSO), mas encontrei {descrever(t)}."
        )


def analisar_sintaxe(tokens):
    """Devolve (AST, número de nós). Levanta ErroParser no primeiro erro."""

    p = Parser(tokens)
    ast = p.programa()

    return ast, p.nos
