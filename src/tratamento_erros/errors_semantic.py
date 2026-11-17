from dataclasses import dataclass

# Mensagens de erros semânticos
_MENSAGENS_ER_SEMANTICOS = {
    "ERRO_VAR_NAO_DECLARADA": "Ainda não foi dado valor a variável \"{nome}\" ... Por favor, dê um valor antes de usá-la | Exemplo: {nome} = 10",
    "ERRO_VAR_DECLARADA_BLOCO": "A variável {nome} só recebe valor dentro de um bloco SE/ENQUANTO/REPITA... Por favor, de um valor inicial a variável antes | Exemplo: {nome} = 10",
    "ERRO_ATRIBUIR_CONSTANTE": "\"{nome}\" é uma CONSTANTE (linha: {linha}) e não pode ser alterada... Por favor, use uma variável com outro nome para armazenar e mudar valores | Exemplo: var = 10",
    "ERRO_LER_CONSTANTE": "Não da para guardar um valor em \"{nome}\" por ser uma CONSTANTE... Use LEIA apenas em variáveis | Exemplo: LEIA var",
    "ERRO_DECLARADO_CONSTANTE": "A variável \"{nome}\" já foi usado como CONSTANTE na linha {linha}... Por favor, use outro nome para a constante",
    "ERRO_CONSTANTE_COM_VARIAVEL": "O valor atribuído a CONSTANTE \"{nome}\" usa uma variável... Por favor, use apenas valores fixos para constantes | Exemplo: CONSTANTE {nome} = 10",
    "ERRO_PARAR": "PARAR apenas funciona dentro de laços de repetição... Como ENQUANTO ou REPITA",
    "ERRO_REPITA_TIPO": "O valor de REPITA precisa ser um número inteiro positivo... Encontrei um valor texto/lógico | Exemplo: REPITA 10 VEZES",
    "ERRO_REPITA_NEGATIVO": "O valor de REPITA precisa ser um número inteiro positivo... Encontrei um valor negativo | Exemplo: REPITA 10 VEZES",
    "ERRO_REPITA_DECIMAL": "O valor de REPITA precisa ser um número inteiro positivo... Encontrei um valor decimal | Exemplo: REPITA 10 VEZES",
    "ERRO_CONDICIONAL_TIPO": "O valor de SE/ENQUANTO precisa ser um valor lógico... Encontrei um valor texto/número | Exemplo: SE var IGUAL_A 10 ENTAO:",
    "ERRO_CONTA_TEXTO": "Não é possível fazer contas com textos como 10 / \"a\"... Utilize apenas números para fazer contas matemáticas ou textos para juntar eles | Exemplo: 10 + 10 ou \"a\" + \"b\"",
    "ERRO_CONTA_LOGICO": "Não é possível fazer contas com valores lógicos como 10 / VERDADE... Utilize apenas números para fazer contas matemáticas ou textos para juntar eles | Exemplo: 10 + 10 ou \"a\" + \"b\"",
    "ERRO_COMPARAR_TEXTO": "Não é possível comparar textos como \"a\" IGUAL_A \"b\" ou \"a\" IGUAL_A 2... Utilize apenas números para fazer comparações | Exemplo: 10 IGUAL_A 10,",
    "ERRO_COMPARAR_LOGICO": "Não é possível comparar valores lógicos como VERDADE MAIOR_QUE FALSO... Utilize apenas os comparadores IGUAL_A ou DIFERENTE_DE para comparar valores lógicos | Exemplo: VERDADE IGUAL_A VERDADE",
    "ERRO_IGUAL_TIPO": "Não é possível comparar valores de tipos diferentes como 10 IGUAL_A \"10\"... Utilize apenas o mesmo tipo de dado para comparar | Exemplo: 10 IGUAL_A 10",
    "ERRO_LOGICO_TIPO": "Não é possível fazer operações lógicas com valores de tipos números e textos sozinhos... Utilize expressões que devolvem respostas de VERDADE ou FALSO | Exemplo: var MAIOR_QUE 0 E var MENOR_QUE 10",
    "ERRO_DIVIDIR_ZERO": "Não é possível dividir um número por 0... Por favor, troque o 0 por outro número | Exemplo: var = 10 / 2",
    "ERRO_RESTO_ZERO": "Não é possível fazer resto de um número por 0... Por favor, troque o 0 por outro número | Exemplo: var = 10 RESTO_DE 2",
}

# Mensagens de avisos semânticos
_MENSAGENS_AV_SEMANTICOS = {
    "AVISO_LOOP_INFINITO": "Cuidado: Este ENQUANTO pode nunca parar... Por favor, verifique se a condição é sempre VERDADE ou use um PARAR no laço",
    "AVISO_LOOP_INFINITO_B": "Cuidado: Este ENQUANTO pode nunca parar... Por favor, verifique se \"{nome}\" muda no bloco ou use um PARAR no laço",
    "AVISO_PARAR_DEPOIS": "Cuidado: Esta {linha} nunca será executada por que vem depois do PARAR",
    "AVISO_BLOCO_VAZIO": "Cuidado: Este bloco de código está vazio... Por favor, verifique se você esqueceu de colocar algum comando dentro do bloco",
    "AVISO_NOME_RESERVADO": "Cuidado: O nome \"{nome}\" é a palavra reservada {reservada} em minúsculas... Por favor, use outro nome para a variável",
}

# Levantamento exceção de erro semântico
class ErroSemantico(Exception):
    def __init__(self, codigo, mensagem, no=None):
        self.codigo = codigo
        self.mensagem = mensagem
        self.no = no
        self.linha = getattr(no, "linha", None)

        super().__init__(mensagem)

# Levantando avisos semânticos. Não deveria interromper a execução.
@dataclass
class Aviso(Exception):
    codigo: str
    mensagem: str
    linha: int = None

# Criando e reportando erro semântico
def criar_erro(codigo, no, **dados):
    return ErroSemantico(codigo, _MENSAGENS_ER_SEMANTICOS[codigo].format(**dados), no)

# Criando e reportando aviso semântico
def criar_aviso(codigo, no, **dados):
    return Aviso(codigo, _MENSAGENS_AV_SEMANTICOS[codigo].format(**dados), getattr(no, "linha", None))

# Checando localização da linha do erro
def checar_linha(linha):
    if linha is not None:
        return f"linha {linha}"
    else:
        return "local desconhecido"

# Reportando erro semântico
def reportar_erro(erro):
    return f"Erro: {checar_linha(erro.linha)}: {erro.mensagem}"

# Reportando aviso semântico
def reportar_aviso(aviso):
    return f"Aviso: {checar_linha(aviso.linha)}: {aviso.mensagem}"