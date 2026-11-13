# Módulo responsável pelo tratamento e formatação

class ErroParser(Exception):
    """Exceção personalizada para erros sintáticos."""

    def __init__(self, mensagem, token=None):
        self.mensagem = mensagem
        self.token = token

        # Obtém as informações de localização do token.
        self.linha = getattr(token, "linha", None)
        self.coluna = getattr(token, "coluna", None)

        super().__init__(mensagem)


def reportar_erro_sintatico(erro):
    """
    Formata uma mensagem de erro sintático
    utilizando as informações do token problemático.
    """

    # Identifica a localização do erro.
    if erro.linha is not None and erro.coluna is not None:
        local = f"Linha {erro.linha}, coluna {erro.coluna}"
    elif erro.linha is not None:
        local = f"Linha {erro.linha}"
    else:
        local = "Localização desconhecida"

    # Obtém o lexema do token que causou o erro.
    lexema = getattr(erro.token, "lexema", "")

    mensagem = f"Erro sintático [{local}]: {erro.mensagem}"

    if lexema:
        mensagem += f" (Próximo de '{lexema}')"

    return mensagem
