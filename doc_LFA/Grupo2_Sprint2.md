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
**Evidências (link do repositório/commit):** https://github.com/juliavsantos/TEApiler-Compilador-Acessivel/commit/cd02ee9d052e98acc3806a99db4ce370fa580c67

## 2. Testes do lexer

- [ X ] Casos de teste com tokens válidos de cada categoria (palavra-chave, identificador, literal, símbolo)
- [ X ] Casos de teste com entradas inválidas (símbolo desconhecido) e mensagem de erro correspondente
- [ X ] Todos os testes passando

**Tabela de casos de teste do lexer:**

| Entrada | Tokens esperados | Resultado obtido | Passou? |
|---|---|---|---|
| "x = 5" | ID, <br> OP_ATRIBUIR, <br> L_NUM, <br> EOF | 1     IDENTIFICADOR            **ID**                'x'<br>1     ATRIBUICAO               **OP_ATRIBUIR**       '='<br>1     LITERAIS                 **L_NUM**             '5'<br>1     FIM                      **EOF** ''| Sim |
| CONSTANTE fahrenheit_con = 32 <br> celsius = 25 <br> converter_fah = ((celsius * 9) / 5) + fahrenheit_con | KW_CONST, <br> ID, <br> OP_ATRIBUIR, <br> L_NUM, <br> QUEBRA_LINHA, <br> S_E_PARENTESE, <br> S_D_PARENTESE, <br> OPA_MUL, <br> OPA_DIV, <br> OPA_ADI, <br> EOF | 1     PALAVRAS_RESERVADAS      **KW_CONST**         'CONSTANTE'<br>1     IDENTIFICADOR            **ID**                'fahrenheit_con'<br>1     ATRIBUICAO               **OP_ATRIBUIR**       '='<br>1     LITERAIS                 **L_NUM**             '32'<br>1     OUTROS                   **QUEBRA_LINHA**      '\n '<br>2     IDENTIFICADOR            **ID**                'celsius'<br>2     ATRIBUICAO               **OP_ATRIBUIR**       '='<br>2     LITERAIS                 **L_NUM**             '25'<br>2     OUTROS                   **QUEBRA_LINHA**      '\n '<br>3     IDENTIFICADOR            **ID**                'converter_fah'<br>3     ATRIBUICAO               **OP_ATRIBUIR**       '='<br>3     DELIMITADORES            **S_E_PARENTESE**     '('<br>3     DELIMITADORES            **S_E_PARENTESE**     '('<br>3     IDENTIFICADOR            **ID**                'celsius'<br>3     OPERADORES_ARITMETICOS   **OPA_MUL**           '*'<br>3     LITERAIS                 **L_NUM**             '9'<br>3     DELIMITADORES            **S_D_PARENTESE**     ')'<br>3     OPERADORES_ARITMETICOS   **OPA_DIV**           '/'<br>3     LITERAIS                 **L_NUM**             '5'<br>3     DELIMITADORES            **S_D_PARENTESE**     ')'<br>3     OPERADORES_ARITMETICOS   **OPA_ADI**           '+'<br>3     IDENTIFICADOR            **ID**                'fahrenheit_con'<br>3     FIM                      **EOF**               ''| Sim |
| PROGRAMA <br> lim = 10 <br> soma = 0 <br> ANOTA: Repetir instrucoes 10 vezes <br> REPITA lim VEZES: <br> soma = soma + 2 <br> ANOTA: Caso a soma ultrapasse 10, pare a repeticao <br> SE soma MAIOR_OU_IGUAL 10 ENTAO: <br> PARAR <br> FIM_SE <br> FIM_REPITA<br> ESCREVA "Soma: " + soma <br> FIM_PROGRAMA | KW_PROGRAMA, <br>ID,<br> OP_ATRIBUIR,<br>L_NUM, <br> KW_REPITA, <br> KW_VEZES, <br> S_2_PONTOS, <br> OPA_ADI, <br> KW_SE, <br> OPR_MAIOR_OU_IGUAL, <br> KW_ENTAO, <br> KW_PARAR, <br> KW_FIM_SE, <br> KW_FIM_REPITA, <br> KW_ESCREVA, <br> L_TEXTO, <br> KW_FIM_PROGRAMA, <br> EOF|1     OUTROS                   **QUEBRA_LINHA**      '\n                '<br>2     PALAVRAS_RESERVADAS      **KW_PROGRAMA**       'PROGRAMA'<br>2     OUTROS                   **QUEBRA_LINHA**      '\n\n                '<br>4     IDENTIFICADOR            **ID**                'lim'<br>4     ATRIBUICAO               **OP_ATRIBUIR**       '='<br>4     LITERAIS                 **L_NUM**             '10'<br>4     OUTROS                   **QUEBRA_LINHA**      '\n                '<br>5     IDENTIFICADOR            **ID**                'soma'<br>5     ATRIBUICAO               **OP_ATRIBUIR**       '='<br>5     LITERAIS                 **L_NUM**             '0'<br>5     OUTROS                   **QUEBRA_LINHA**      '\n\n                '<br>8     PALAVRAS_RESERVADAS      **KW_REPITA**         'REPITA'<br>8     IDENTIFICADOR            **ID**                'lim'<br>8     PALAVRAS_RESERVADAS      **KW_VEZES**          'VEZES'<br>8     DELIMITADORES            **S_2_PONTOS**        ':'<br>8     OUTROS                   **QUEBRA_LINHA**      '\n\n                '<br>10    IDENTIFICADOR            **ID**                'soma'<br>10    ATRIBUICAO               **OP_ATRIBUIR**       '='<br>10    IDENTIFICADOR            **ID**                'soma'<br>10    OPERADORES_ARITMETICOS   **OPA_ADI**           '+'<br>10    LITERAIS                 **L_NUM**             '2'<br>10    OUTROS                   **QUEBRA_LINHA**      '\n\n                '<br>13    PALAVRAS_RESERVADAS      **KW_SE**             'SE'<br>13    IDENTIFICADOR            **ID**                'soma'<br>13    OPERADORES_RELACIONAIS   **OPR_MAIOR_IGUAL**   'MAIOR_OU_IGUAL'<br>13    LITERAIS                 **L_NUM**             '10'<br>13    PALAVRAS_RESERVADAS      **KW_ENTAO**          'ENTAO'<br>13    DELIMITADORES            **S_2_PONTOS**        ':'<br>13    OUTROS                   **QUEBRA_LINHA**      '\n                '<br>14    PALAVRAS_RESERVADAS      **KW_PARAR**          'PARAR'<br>14    OUTROS                   **QUEBRA_LINHA**      '\n                '<br>15    PALAVRAS_RESERVADAS      **KW_FIM_SE**         'FIM_SE'<br>15    OUTROS                   **QUEBRA_LINHA**      '\n\n                '<br>17    PALAVRAS_RESERVADAS      **KW_FIM_REPITA**     'FIM_REPITA'<br>17    OUTROS                   **QUEBRA_LINHA**      '\n\n                '<br>19    PALAVRAS_RESERVADAS      **KW_ESCREVA**        'ESCREVA'<br>19    LITERAIS                 **L_TEXTO**           '"Soma: "'<br>19    OPERADORES_ARITMETICOS   **OPA_ADI**           '+'<br>19    IDENTIFICADOR            ID                'soma'<br>19    OUTROS                   **QUEBRA_LINHA**      '\n                '<br>20    PALAVRAS_RESERVADAS      **KW_FIM_PROGRAMA**   'FIM_PROGRAMA'<br>20    OUTROS                   **QUEBRA_LINHA**      '\n                '<br>21    FIM                      **EOF**               ''| Sim |
| 1_acento = 30 | ERRO_VAR_COM_NUM, <br> OP_ATRIBUIR, <br> L_NUM, <br> EOF | 1     ERROS_LEXICOS            **ERRO_VAR_COM_NUM**         '1_acento' <br>ERRO na linha 1: Opa! O nome da sua variável "1_acento" não pode começar com números ou símbolos... Por favor, reescreva o nome da sua variável - Exemplo: "var" <br> 1     ATRIBUICAO               **OP_ATRIBUIR**              '=' <br> 1     LITERAIS                 **L_NUM**                    '30' <br> 1     FIM                      EOF                      '' | SIM |
| ENQUANTO x MENOR_QUE 10 FAÇA:<br>x++ | KW_ENQUANTO,<br> ID, <br> OPR_MENOR_Q, <br> L_NUM, <br> ERRO_LETRA_ACENTUADA, <br> S_2_PONTOS, <br> ERRO_ATRIBUICAO_COMPOSTA, <br> EOF | 1     OUTROS                   **QUEBRA_LINHA**             '\n                '<br>2     PALAVRAS_RESERVADAS      **KW_ENQUANTO**              'ENQUANTO'<br>2     IDENTIFICADOR            **ID**                       'x'<br>2     OPERADORES_RELACIONAIS   **OPR_MENOR_Q**              'MENOR_QUE'<br>2     LITERAIS                 **L_NUM**                    '10'<br>2     ERROS_LEXICOS            **ERRO_LETRA_ACENTUADA**     'FAÇA'<br>ERRO na linha 2: Opa! A sua palavra ou variável FAÇA está usando acentos... Por favor, não use acentos em palavras reservadas ou váriaveis - Exemplo: ENTAO<br>2     DELIMITADORES            **S_2_PONTOS**               ':'<br>2     OUTROS                   **QUEBRA_LINHA**             '\n                '<br>3     IDENTIFICADOR            **ID**                       'x'<br>3     ERROS_LEXICOS            **ERRO_ATRIBUICAO_COMPOSTA** '++' <br> ERRO na linha 3: Opa! Esse símbolo de atribuição ++ não existe nessa linguagem... Para atribuir um valor a uma variável use "=" - Exemplo: soma = soma + 1 ou soma = soma + var <br> 3     OUTROS                   **QUEBRA_LINHA**             '\n                ' <br> 4     FIM                      **EOF**                      ''| SIM |
| SE x % 2 == 0 ENTAO: | KW_SE, <br> ID, <br> ERRO_RESTO_SIMBOLO, <br> L_NUM, <br> ERRO_COMPARADOR_SIMBOLO, <br> KW_ENTAO, <br> S_2_PONTOS, <br> EOF | 1     PALAVRAS_RESERVADAS  **KW_SE**                    'SE' <br> 1     IDENTIFICADOR            **ID**                        'x' <br> 1     ERROS_LEXICOS            **ERRO_RESTO_SIMBOLO**        '%' <br> ERRO na linha 1: Opa! O símbolo de resto % está usando um símbolo de outra linguagem...Você quis dizer RESTO_DE? <br> 1     LITERAIS                **L_NUM**                    '2' <br> 1     ERROS_LEXICOS            **ERRO_COMPARADOR_SIMBOLO**   '==' <br> ERRO na linha 1: Opa! O comparador == está usando um símbolo de outra linguagem...Você quis dizer IGUAL_A? <br> 1     LITERAIS                 **L_NUM**                     '0'<br>1     <br> PALAVRAS_RESERVADAS      **KW_ENTAO**                  'ENTAO' <br> 1     DELIMITADORES            **S_2_PONTOS**                ':' <br> 1     FIM                      **EOF**                       '' | SIM |

## 3. Revisão da gramática

- [ X ] Derivações manuais de cada programa de exemplo da Sprint 1, conferindo se a gramática realmente os gera
- [ X ] Pontos de ambiguidade identificados e resolvidos (reescrita de regras, se necessário)
- [ X ] Gramática final documentada em EBNF, versionada

**Ajustes feitos na gramática e por quê:**
- Mudamos a sintaxe da gramática para se ajustar ao estilo comum e mais aceito na comunidade, para facilitar leitura. Se baseando na gramática EBNF utilizado pelo manual da Linguagem LUA (https://www.lua.org/manual/5.4/manual.html#9)

- Mudamos o nome de NOVA_LINHA para QUEBRA_LINHA, se ajustando a nova tabela de tokens

- Comandos novos foram adicionados sendo eles "declaracao_const" e "parar", para se ajustar com a nova tabela de tokens

- Adicionado e formalizado o uso do delimitador ":" para demarcar a entrada das estruturas de controle (ENTAO:, SENAO:, FACA:, VEZES:)

- Valores passaram a ser NUMERO, TEXTO e IDENTIFICADOR para L_NUM, L_TEXTO, ID, VERDADE, FALSO e ('expressao'). Para se ajustar com a nova tabela de tokens e especificar valores literais.

- Adicionamos os tokens para os parenteses para contas matemáticas

- A regra de comparação foi mudado para expressao [ comparador expressao ], para permitir comparações com uma expressão só. (Exemplo: SE x ENTAO:) 

- Seções de Léxico e Palavras Reservadas foram retirados e deixamos exclusivamente para a tabela de tokens e analisador léxico
**Gramática final (EBNF):**
```
programa = [ QUEBRA_LINHA ] PROGRAMA QUEBRA_LINHA bloco FIM_PROGRAMA [ QUEBRA_LINHA ]
bloco = { comando }
comando = instrucao QUEBRA_LINHA
instrucao = atribuicao | declaracao_const | leitura | escrita |
            parar | condicional | enquanto | repita

(* COMANDOS SIMPLES *)
atribuicao = ID '=' expressao
declaracao_const = CONSTANTE ID '=' expressao
leitura = LEIA ID
escrita = ESCREVA expressao
parar = PARAR

(* ESTRUTURAS DE CONTROLE *)
condicional = SE condicao ENTAO ':' QUEBRA_LINHA bloco
              [ SENAO ':' QUEBRA_LINHA bloco ]
              FIM_SE
enquanto = ENQUANTO condicao FACA ':' QUEBRA_LINHA bloco FIM_ENQUANTO
repita = REPITA expressao VEZES ':' QUEBRA_LINHA bloco FIM_REPITA

(* CONDIÇÕES *)
condicao = termo_logico { OU termo_logico }
termo_logico = fator_logico { E fator_logico }
fator_logico = [ NAO ] comparacao
comparacao = expressao [ comparador expressao ]
comparador = IGUAL_A | DIFERENTE_DE | MENOR_QUE | MAIOR_QUE |
             MENOR_OU_IGUAL | MAIOR_OU_IGUAL

(* EXPRESSÕES *)
expressao = termo { operador_soma termo }
termo = fator { operador_mult fator }
fator = [ '-' ] primario
primario = L_NUM | L_TEXTO | VERDADE | FALSO | ID | '(' expressao ')'
operador_soma = '+' | '-'
operador_mult = '*' | '/' | RESTO_DE
```

## 4. Conjunto de programas de exemplo

- [ X ] Pelo menos 5 programas válidos, cobrindo todas as features da v1
- [ X ] Pelo menos 3 programas inválidos, cada um violando uma regra diferente (léxica, sintática)
- [ X ] Cada exemplo inválido com a explicação do que deveria ser rejeitado e por quê

**Lista de programas de exemplo (válidos e inválidos) e link do arquivo:**
### Programas Válidos
Olá mundo:
```
PROGRAMA

ESCREVA "Olá mundo!"

FIM_PROGRAMA
```
Trocar Valores:
```
PROGRAMA

valor_1 = 10
valor_2 = 20
auxiliar = 0

ESCREVA valor_1 + " " + valor_2

auxiliar = valor_1
valor_1 = valor_2
valor_2 = auxiliar

ESCREVA valor_1 + " " + valor_2

FIM_PROGRAMA
```
Calcular média nota:
```
PROGRAMA

fisica = 9
quimica = 6
biologia = 10

total = fisica + quimica + biologia

media = total / 3

ESCREVA "A sua media é: " + media

SE media MAIOR_OU_IGUAL 7 ENTAO:
ESCREVA "Passou de ano!"
SENAO:
ESCREVA "Reprovado…"
FIM_SE

FIM_PROGRAMA
```
Calcular área:
```
PROGRAMA

ESCREVA "Digite o tamanho da largura: "
LEIA lar

ESCREVA "Digite o tamanho: "
LEIA tam

area = lar * tam
ESCREVA "Area total: " + area

FIM_PROGRAMA
```
Contagem regressiva:
```
PROGRAMA

LEIA inicio

ESCREVA "Terminando contagem em: "

ENQUANTO inicio MAIOR_OU_IGUAL 0 FACA:
ESCREVA inicio

inicio = inicio - 1
FIM_ENQUANTO

FIM_PROGRAMA
```

### Programas Inválidos
Par ou ímpar:
```
PROGRAMA 

LEIA num

SE num RESTO_DE 2 == 0 ENTAO
ESCREVA "Par"
SENAO
ESCREVA Impar

FIM_PROGRAMA
```
Erros Léxicos: O símbolo "==" não existe dentro da linguagem. <br>
Erros Sintáticos: O delimitador ":" não está no final de ENTAO ou SENAO. Falta FIM_SE no final na estrutura condicional SE. <br>
Erro Semântico: O texto Impar está sem parenteses, o analisador léxico identifica Impar como ID. <br>
<br>

Calcular desconto:
```
PROGRAMA

frango = 20
10_desconto = 10

desconto frango * 10_desconto = / 100

ESCREVA desconto

FIM_PROGRAMA
```
Erros Léxicos: 10_desconto é uma variável que começa com número, o que é proibido. <br>
Erros Sintáticos: O calculo e atribuição de desconto está na ordem errada. Deveria ser "desconto = frango * 10_desconto / 100" <br>
<br>
Somador:
```
PROGRAMA

LEIA

x = 0

REPITA lim:
x += 1

ESCREVA x
FIM

FIM_PROGRAMA
```
Erros Léxicos: O símbolo "+=" não existe nessa linguagem. <br>
Erros Sintáticos: LEIA está sem uma variável. A estrutura de repetição REPITA estão sem VEZES. O fechamento da estrutura de repetição está errado, deveria ser FIM_REPITA <br>
Erro Semântico: lim nunca recebeu valor.

## 5. Scrum

- [ - ] Atualizações semanais no board
- [ X ] Board refletindo o estado real

**Link do board:** https://github.com/users/juliavsantos/projects/1

## 6. Diário de bordo (retrospectiva individual)

| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|---|---|---|---|
| Julia | Definiu os tokens e glossário inicial, com base em outras linguagens de programação como C, Python e principalmente Portugol. Garantiu que a gramática atualizada estava livre de ambiguidades e de acordo com as features inicias | Identificar ambiguidades na linguagem e decidir o que era necessário ou não na linguagem | - |
| Matheus | Implementou o dicionário de tokens, analisador léxico básico e tratador de erros léxicos para geração de erros humanizados. Realizou testes do analisador. Definiu gramática final e escreveu os programas válidos e inválidos | Entender e testar analisador léxico base. Implementar erros e escrever mensagens de erros adequadas para o público alvo | Manter a gramática e tokens como está. Ajustar tratamento de erros para mensagens mais adequadas e generalizar para tratamentos não só léxicos, como sintático e talvez semântico. |
| Ronald | Implementou o dicionário de tokens, analisador léxico básico; Realizou testes bases para o analisador léxico | Testar o analisador léxico; Verificar se os tokens estão corretos e gramática sem ambiguidades | Pretendo manter os tokens e a gramática como estão; |
| William | Ajudou na implementação e no embasamento teórico do analisador léxico com base nos tokens definidos. | Entender e direcionar como implementar a base do analisador léxico | - |

---

## Rubrica de avaliação — Sprint 2 (nota de 0 a 4,0)

| Critério | Peso | O que caracteriza nota máxima | Nota atribuída | Observações |
|---|---|---|---|---|
| Lexer implementado e testado | 1,5 | Tokenizador funcional, erros léxicos tratados, testes cobrindo categorias e casos inválidos | | |
| Gramática revisada e sem ambiguidade | 1,5 | Derivações conferidas, ambiguidades resolvidas e documentadas | | |
| Programas de exemplo | 0,5 | Conjunto válido/inválido cobrindo a v1, com explicação dos inválidos | | |
| Scrum + diário de bordo | 0,5 | Board com histórico; diário reflexivo de todos | | |
| **Nota final da Sprint 2** | **4,0** | | **___ / 4,0** | |
