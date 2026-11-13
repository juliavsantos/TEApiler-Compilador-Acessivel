from dataclasses import dataclass

from ..tratamento_erros.errors_semantic import criar_aviso, criar_erro
from ..estrutura_compilador.symbol_table import Categoria, TabelaSimbolos, DESCONHECIDO, TIPO_NUMERO, TIPO_TEXTO, TIPO_LOGICO
from ..compilador.parser import RESERVADAS_SET


OPS_ORDEM = {"MENOR_QUE", "MAIOR_QUE", "MENOR_OU_IGUAL", "MAIOR_OU_IGUAL"}

# Funções Auxiliares

def conhecido(tipo):
    return tipo != DESCONHECIDO

def nomes_variaveis(no):
    if no.tipo == "Variavel":
        return [no.nome]

    nomes = []

    for campo in ("esq", "dir", "valor"):
        filho = getattr(no, campo, None)

        if hasattr(filho, "tipo"):
            nomes += nomes_variaveis(filho)
    
    return nomes

def nomes_modificados(bloco):
    nomes = set()

    for c in bloco:
        if c.tipo in ("Atribuir", "Leia"):
            nomes.add(c.nome)
        elif c.tipo == "Se":
            nomes |= nomes_modificados(c.entao) | nomes_modificados(c.senao)
        elif c.tipo in ("Enquanto", "Repita"):
            nomes |= nomes_modificados(c.corpo)
    return nomes

def contem_parar(bloco):
    for c in bloco:
        if c.tipo == "Parar":
            return True
        if c.tipo == "Se" and c.senao and termina(c.entao) and termina(c.senao):
            return True
    return False



# Determinando se um bloco termina com PARAR ou não.
def termina(bloco):
    for comando in bloco:
        if comando.tipo == "Parar":
            return True
        if comando.tipo == "Se" and comando.senao and termina(comando.entao) and termina(comando.senao):
            return True
    
    return False

# Funções principais/Analisador Semantico
@dataclass
class ResultadoSemantico:
    ast: object
    tabela: TabelaSimbolos
    avisos: list
    erros: list

    @property
    def ok(self):
        return not self.erros


class AnalisadorSemantico:
    def __init__(self, parar_no_primeiro_erro=True):
        self.parar = parar_no_primeiro_erro
        self.tabela = TabelaSimbolos()
        self.erros = []
        self.avisos = []
        self.nivel_laco = 0
        self.definidas = set()
        self.estruturas = []
        self.origem = {}

    # Entrada analisando AST
    def analisar(self, ast):
        self.visitar(ast)
        return ResultadoSemantico(ast, self.tabela, self.avisos, self.erros)

    # Relatando problemas
    def erro(self, codigo, no, **dados):
        erro = criar_erro(codigo, no, **dados)

        if self.parar:
            raise erro
        self.erros.append(erro)

    def _aviso(self, codigo, no, **dados):
        self.avisos.append(criar_aviso(codigo, no, **dados))



    # Visitar nó da AST e retornar o tipo estático do nó (Anotação da AST)
    def visitar(self, no):
        metodo = getattr(self, f"visitar_{no.tipo}", None)

        if metodo is None:
            raise NotImplementedError(f"Não existe método para visitar o nó do tipo {no.tipo}")

        tipo = metodo(no)

        if tipo is not None:
            no.tipo_estatico = tipo

        return tipo

    # 
    def bloco(self, comandos):
        for comando in comandos:
            self.visitar(comando)

    def visitar_Programa(self, no):
        self.bloco(no.corpo)


    # Resolução de Nomes/IDs

    # Declarando variaveis na tabela de símbolos
    def declarar(self, no, nome, categoria, tipo, constante=None):
        simbolo = self.tabela.declarar(nome, categoria, no.linha, tipo, constante)

        if self.estruturas:
            self.origem[nome] = self.estruturar[-1]

        # Checando se o nome é uma palavra reservada da linguagem em minuscula. 
        if nome != nome.upper() and nome.upper() in RESERVADAS_SET:
            self.aviso("AVISO_NOME_RESERVADO", no, nome=nome, reservada=nome.upper())

        return simbolo

    # Visitando nó de atribuição
    def visitar_Atribuir(self, no):
        # Visitando lado direto da atribuição
        tipo = self.visitar(no.valor)
        existente = self.tabela.buscar(no.nome)
        no.declarado = existente is None

        # Se o ID não existir na tabela, declarando como variável
        if existente is None:
            self.declarar(no, no.nome, Categoria.VARIAVEL, tipo)
        # Se o ID for constante, lançar erro
        elif existente.se_constante:
            self.erro("ERRO_ATRIBUIR_CONSTANTE", no, nome=no.nome, linha=existente.linha)
        # Se o ID existir, mas o tipo for diferente, marcar como desconhecido
        elif existente.tipo != tipo:
            existente.tipo = DESCONHECIDO

        # Adicionando o ID na lista de IDs definidos junto com seu tipo
        self.definidas.add(no.name)
        no.tipo_estatico = tipo

    # Verificando constantes
    def visitar_Constante(self, no):
        tipo = self.visitar(no.valor)
        existente = self.tabela.buscar(no.nome)
        no.declarado = existente is None

        # Verificando se constante já foi declarada
        if existente is not None:
            self.erro("ERRO_DECLARADO_CONSTANTE", no, nome=no.nome, linha=existente.linha)
        
        for nome_var in nomes_variaveis(no.valor):
            simbolo = self.tabela.buscar(nome_var)

            # Verificando se uma variavel está sendo usada para definir uma constante
            if simbolo is not None and not simbolo.se_constante:
                self.erro("ERRO_CONSTANTE_COM_VARIAVEL", no, nome=no.nome)
                break

        if existente is None:
            self.declarar(no, no.nome, Categoria.CONSTANTE, tipo, constante=no.valor)

        self.definidas.add(no.nome)
        no.tipo_estatico = tipo

    # Verificando leitura de variáveis, tipo sempre será desconhecido.
    def visitar_Leia(self, no):
        existente = self.tabela.buscar(no.nome)
        no.declarado = existente is None

        # Se o ID não existir na tabela, declarando como variável
        if existente is None:
            self.declarar(no, no.nome, Categoria.VARIAVEL, DESCONHECIDO)
        # Se o ID for constante, lançar erro
        elif existente.se_constante:
            self.erro("ERRO_LER_CONSTANTE", no, nome=no.nome, linha=existente.linha)
        else:
            existente.tipo = DESCONHECIDO

        self.definidas.add(no.nome)

    def visitar_Escreva(self, no):
        self.visitar(no.valor)


    # Verificando variáveis
    def visitar_Variavel(self, no):
        simbolo = self.tabela.buscar(no.nome)

        # Se o ID não existir na tabela, lançar erro e marcar como desconhecido
        if simbolo is None:
            self.erro("ERRO_VAR_NAO_DECLARADA", no, nome=no.nome)
            no.se_constante = False
            return DESCONHECIDO
        
        # Verificando se a variavel está sendo declarada em um bloco condicional ou repetição
        if no.nome not in self.definidas:
            rotulo, linha = self.origem.get(no.nome, ("programa", simbolo.linha))
            self.erro("ERRO_VAR_DECLARADA_BLOCO", no, nome=no.nome, estrutura=rotulo, linha=linha)

        no.se_constante = simbolo.se_constante
        return simbolo.tipo

    # Verificando se PARAR está sendo usado do jeito certo
    def visitar_Parar(self, no):
        if self.nivel_laco == 0:
            self.erro("ERRO_PARAR", no)

    def checar_condicao(self, tipo):
        if tipo in (TIPO_NUMERO, TIPO_TEXTO):
            self.erro("ERRO_CONDICIONAL_TIPO")


    # Verificando bloco condicional "SE"
    def visitar_Se(self, no):
        tipo = self.visitar(no.condicao)
        self.checar_condicao(tipo)

        self.estruturas.append(("SE", no.linha))
        antes = set(self.definidas)
        self.bloco(no.entao)
        fim_entao = self.definidas
        self.definidas = set(antes)
        self.bloco(no.senao)
        fim_senao = self.definidas
        self.estruturas.pop()

        termina_entao, termina_senao = termina(no.entao), termina(no.senao)

        # Verificando como termina bloco "SE"
        if termina_entao and not termina_senao:
            self.definidas = fim_senao
        elif termina_senao and not termina_entao:
            self.definidas = fim_entao
        else:
            self.definidas = fim_entao & fim_senao

    def avisar_loop_infinito(self, no):
        if contem_parar(no.corpo):
            return

        condicao = no.condicao

        if condicao.tipo == "logico" and condicao.valor is True:
            self.aviso("AVISO_LOOP_INFINITO", no)
            return
        
        variaveis = []

        if variaveis and not (set(variaveis) & nomes_modificados(no.corpo)):
            self.aviso("AVISO_LOOP_INFINITO_B", no, nome=variaveis[0]) 

    def laco(self, no, rotulo, corpo):
        if not corpo:
            self._aviso("AVISO_BLOCO_VAZIO", no)
        self.estruturas.append((rotulo, no.linha))
        self.nivel_laco += 1
        antes = set(self.definidas)
        self._bloco(corpo)
        self.definidas = antes             # o corpo pode não executar nenhuma vez
        self.nivel_laco -= 1
        self.estruturas.pop()

    def visitar_Enquanto(self, no):
        tipo = self.visitar(no.condicao)
        self.checar_condicao(no.condicao, tipo, "ENQUANTO")
        self.avisar_loop_infinito(no)
        self.laco(no, "ENQUANTO", no.corpo)

    def visitar_Repita(self, no):
        tipo = self.visitar(no.vezes)
        if tipo in (TIPO_TEXTO, TIPO_LOGICO):
            self.erro("ERRO_REPITA_TIPO")
        else:
            valor = self._valor_constante(no.vezes)
            if valor is not None and valor < 0:
                self.erro("ERRO_REPITA_NEGATIVO")
            elif valor is not None and not float(valor).is_integer():
                self._erro("ERRO_REPITA_DECIMAL")
        self.laco(no, "REPITA", no.corpo)

    def visitar_Numero(self, no):
        return TIPO_NUMERO
 
    def visitar_Texto(self, no):
        return TIPO_TEXTO
 
    def visitar_Logico(self, no):
        return TIPO_LOGICO
 
    def visitar_Negativo(self, no):
        tipo = self.visitar(no.valor)
        if tipo == TIPO_TEXTO:
            self.erro("ERRO_CONTA_TEXTO", no)
        elif tipo == TIPO_LOGICO:
            self.erro("ERRO_CONTA_LOGICO", no)
        return TIPO_NUMERO


    def visitar_OpAritmetica(self, no):
        esquerda, direita = self.visitar(no.esq), self.visitar(no.dir)

        op = no.op

        if op == "+":
            if TIPO_LOGICO in (esquerda, direita):
                self.erro("ERRO_CONTA_LOGICO", no)
                return DESCONHECIDO
            
            if TIPO_TEXTO in (esquerda, direita):
                return TIPO_TEXTO

            if esquerda == TIPO_NUMERO and direita == TIPO_NUMERO:
                return TIPO_NUMERO
            
            return DESCONHECIDO

        if TIPO_TEXTO in (esquerda, direita):
            self.erro("ERRO_CONTA_TEXTO", no)
        elif TIPO_LOGICO in (esquerda, direita):
            self.erro("ERRO_CONTA_LOGICO", no)
        
        if op in ("/", "RESTO_DE") and self.valor_constante(no.dir) == 0:
            self._erro("ERRO_DIVIDIR_ZERO" if op == "/" else "ERRO_RESTO_ZERO", no)

        return TIPO_NUMERO

    def visitar_OpRelacional(self, no):
        esquerda, direita = self.visitar(no.esq), self.visitar(no.dir)

        diferentes = conhecido(esquerda) and conhecido(direita) and esquerda != direita

        if no.op in OPS_ORDEM:
            if TIPO_LOGICO in (esquerda, direita):
                self.erro("ERRO_COMPARAR_LOGICO", no)
            elif diferentes:
                self.erro("ERRO_COMPARAR_TEXTO", no)
        elif diferentes:
            self.erro("ERRO_IGUAL_TIPO", no)
        
        return TIPO_LOGICO

    def exigir_logico(self, operando, tipo, operador):
        if tipo in (TIPO_NUMERO, TIPO_TEXTO):
            self.erro("ERRO_LOGICO_TIPO")
 
    def visitar_OpLogica(self, no):
        self.exigir_logico(no.esq, self.visitar(no.esq), no.op)
        self.exigir_logico(no.dir, self.visitar(no.dir), no.op)
        return TIPO_LOGICO
 
    def visitar_Nao(self, no):
        self.exigir_logico(no.valor, self.visitar(no.valor), "NAO")
        return TIPO_LOGICO


    def valor_constante(self, no):
        if no.tipo == "Numero":
            return no.valor
        
        if no.tipo == "Negativo":
            valor = self.valor_constante(no.valor)
            return None if valor is None else -valor
        
        if no.tipo == "Variavel":
            simbolo = self.tabela.buscar(no.nome)
            return simbolo.valor_constante if simbolo is not None and simbolo.se_constante else None

        if no.tipo == "OpAritmetica":
            a, b = self.valor_constante(no.esq), self.valor_constante(no.dir)

            if a is None or b is None:
                return None

            if no.op == "+":
                return a + b
                
            if no.op == "-":
                return a - b
            
            if no.op == "*":
                return a * b
            
            if b == 0:
                return None
        
            return a / b if no.op == "/" else a % b


        return None

def analisar_semantica(ast, parar_no_primeiro_erro=True):
    """Ponto de entrada: analisa a AST e devolve um ResultadoSemantico."""
    return AnalisadorSemantico(parar_no_primeiro_erro).analisar(ast)

          