# Diário de Sprint 2 — Lexer e gramática validada
**Período:** Semana 2

**Grupo / tema:** Grupo 2 — Compilador para DSL acessível para pessoas com TEA

**Equipe:** Julia Aparecida Venâncio dos Santos, Matheus Akira Saito de Souza, Ronald Alencar do Rosário, William Souza

**Scrum Master do Sprint:** Matheus

**Repositório GitHub:** https://github.com/juliavsantos/TEApiler-Compilador-Acessivel

> A entrega é sobre a especificação léxica e o rascunho de gramática da Sprint 1. Esta sprint **implementa o lexer** e **revisa a gramática até eliminar ambiguidades** — não avança para parser/AST, isso é Sprint 3.

### Contrato desta sprint

| | Artefato | Origem / destino |
|---|---|---|
| **Entra** | Especificação léxica + rascunho da gramática | Sprint 1 — **não redefinir tokens sem justificar** |
| **Entra** | Lista fechada de features da v1 | Sprint 1 |
| **Sai** | Lexer funcional (tokenizador) | Sprint 3 |
| **Sai** | Gramática revisada e sem ambiguidade relevante | Sprint 3 **é obrigada a usar esta gramática** |
| **Sai** | Conjunto de programas de exemplo (válidos e inválidos) | Sprint 3 e 4 (testes) |

**Não sai daqui:** parser, AST, análise semântica. 

- [ X ] Confirmei que os tokens implementados são os da especificação da Sprint 1 (ou revisados com justificativa registrada)

---

## 1. Implementação do lexer

- [ X ] Tokenizador implementado a partir da tabela de tokens da Sprint 1
- [ X ] Tratamento de espaços em branco, comentários (se houver) e quebras de linha
- [ X ] Erros léxicos (caractere/símbolo não reconhecido) tratados com mensagem clara

**Descrição da implementação e estrutura do código:** Implementamos a função tokenizar(codigo), que aceita um código (uma linha ou várias linhas). <br>
Esse mini analisador léxico, devolve os tokens usados, sua categoria, lexema e a linha que se encontra. Aqui o maior casamento de string vence, caso aconteça empate, vai depender da ordem que está no dicionário. <br>
Espaços em branco, comentários e quebras de linha são tratados nesse implementação. além de tratar de forma bem crua e simples erros léxicos com o token "ERRO". <br>
Apenas tokenizamos e validamos os tokens em si com base no dicionário implementado com base na sintaxe estabelecido no sprint 1: <br>
```
def tokenizar(codigo):
    """
    Devolve a lista de Token do código. 
    Não levanta exceção: erros viram token ERRO.
    """
    pos, linha, saida = 0, 1, []
    while pos < len(codigo):
        # Pega a posição de um espaço e ignora
        ign = _IGNORAR.match(codigo, pos)
        if ign:
            pos = ign.end()
            continue

        # Verifica se uma palavra é um token existente
        melhor = None  # (nome, fim)
        for nome, rx in _TABELA:
            m = rx.match(codigo, pos)
            if m and m.end() > pos and (melhor is None or m.end() > melhor[1]):
                melhor = (nome, m.end())

        if melhor is None:
            nome, fim = "ERRO", pos + 1
        else:
            nome, fim = melhor
        lexema = codigo[pos:fim]

        descartar = (nome == "COMENTAR" and not manter_comentarios) or (
            nome == "QUEBRA_LINHA" and saida and saida[-1].token == "QUEBRA_LINHA")
        if not descartar:
            saida.append(Token(nome, CATEGORIA_DO_TOKEN.get(nome, "ERRO"), lexema, linha))

        linha += lexema.count("\n")
        pos = fim

    saida.append(Token("EOF", "FIM", "", linha))
    return saida
```
**Evidências (link do repositório/commit):** https://github.com/juliavsantos/TEApiler-Compilador-Acessivel

## 2. Testes do lexer

- [ ] Casos de teste com tokens válidos de cada categoria (palavra-chave, identificador, literal, símbolo)
- [ ] Casos de teste com entradas inválidas (símbolo desconhecido) e mensagem de erro correspondente
- [ ] Todos os testes passando

**Tabela de casos de teste do lexer:**

| Entrada | Tokens esperados | Resultado obtido | Passou? |
|---|---|---|---|
| "PROGRAMA x = 5 FIM_PROGRAMA" | ID, <br> OP_ATRIBUIR, <br> L_NUM, <br> EOF | 1     IDENTIFICADOR            **ID**                'x'<br>1     ATRIBUICAO               **OP_ATRIBUIR**       '='<br>1     LITERAIS                 **L_NUM**             '5'<br>1     FIM                      **EOF** ''| Sim |
| "CONSTANTE fahrenheit_con = 32 \n celsius = 25 \n converter_fah = ((celsius * 9) / 5) + fahrenheit_con" | KW_CONST, <br> ID, <br> OP_ATRIBUIR, <br> L_NUM, <br> S_E_PARENTESE, <br> S_D_PARENTESE, <br> OPA_MUL, <br> OPA_DIV, <br> OPA_ADI, <br> EOF | 1     PALAVRAS_RESERVADAS      KW_CONST          'CONSTANTE'<br>1     IDENTIFICADOR            ID                'fahrenheit_con'<br>1     ATRIBUICAO               OP_ATRIBUIR       '='<br>1     LITERAIS                 L_NUM             '32'<br>1     OUTROS                   QUEBRA_LINHA      '\n '<br>2     IDENTIFICADOR            ID                'celsius'<br>2     ATRIBUICAO               OP_ATRIBUIR       '='<br>2     LITERAIS                 L_NUM             '25'<br>2     OUTROS                   QUEBRA_LINHA      '\n '<br>3     IDENTIFICADOR            ID                'converter_fah'<br>3     ATRIBUICAO               OP_ATRIBUIR       '='<br>3     DELIMITADORES            S_E_PARENTESE     '('<br>3     DELIMITADORES            S_E_PARENTESE     '('<br>3     IDENTIFICADOR            ID                'celsius'<br>3     OPERADORES_ARITMETICOS   OPA_MUL           '*'<br>3     LITERAIS                 L_NUM             '9'<br>3     DELIMITADORES            S_D_PARENTESE     ')'<br>3     OPERADORES_ARITMETICOS   OPA_DIV           '/'<br>3     LITERAIS                 L_NUM             '5'<br>3     DELIMITADORES            S_D_PARENTESE     ')'<br>3     OPERADORES_ARITMETICOS   OPA_ADI           '+'<br>3     IDENTIFICADOR            ID                'fahrenheit_con'<br>3     FIM                      EOF               ''| Sim |

## 3. Revisão da gramática

- [ ] Derivações manuais de cada programa de exemplo da Sprint 1, conferindo se a gramática realmente os gera
- [ ] Pontos de ambiguidade identificados e resolvidos (reescrita de regras, se necessário)
- [ ] Gramática final documentada em EBNF, versionada

**Ajustes feitos na gramática e por quê:**
**Gramática final (EBNF):**

## 4. Conjunto de programas de exemplo

- [ ] Pelo menos 5 programas válidos, cobrindo todas as features da v1
- [ ] Pelo menos 3 programas inválidos, cada um violando uma regra diferente (léxica, sintática)
- [ ] Cada exemplo inválido com a explicação do que deveria ser rejeitado e por quê

**Lista de programas de exemplo (válidos e inválidos) e link do arquivo:**

## 5. Scrum

- [ ] Atualizações semanais no board
- [ ] Board refletindo o estado real

**Link do board:**

## 6. Diário de bordo (retrospectiva individual)

| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|---|---|---|---|
| | | | |

---

## Rubrica de avaliação — Sprint 2 (nota de 0 a 4,0)

| Critério | Peso | O que caracteriza nota máxima | Nota atribuída | Observações |
|---|---|---|---|---|
| Lexer implementado e testado | 1,5 | Tokenizador funcional, erros léxicos tratados, testes cobrindo categorias e casos inválidos | | |
| Gramática revisada e sem ambiguidade | 1,5 | Derivações conferidas, ambiguidades resolvidas e documentadas | | |
| Programas de exemplo | 0,5 | Conjunto válido/inválido cobrindo a v1, com explicação dos inválidos | | |
| Scrum + diário de bordo | 0,5 | Board com histórico; diário reflexivo de todos | | |
| **Nota final da Sprint 2** | **4,0** | | **___ / 4,0** | |
