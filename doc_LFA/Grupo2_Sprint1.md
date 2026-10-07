# Diário de Sprint 1 — Definição da linguagem
**Período:** Semana 1
**Grupo / tema:** Grupo 2 — Compilador para DSL acessível para pessoas com TEA
**Integrantes:** Julia Aparecida Venâncio dos Santos, Matheus Akira Saito de Souza, Ronald Alencar do Rosário, William Souza
**Scrum Master do Sprint:** Matheus Akira Saito de Souza
**Repositório GitHub:** https://github.com/juliavsantos/TEApiler-Compilador-Acessivel

> Esta sprint **só define a linguagem no papel**: princípios de acessibilidade, lista fechada de features da v1, especificação léxica e rascunho da gramática. **Não há** implementação de lexer/parser nem código — isso começa na Sprint 2.

### Contrato desta sprint

| | Artefato | Quem usa depois |
|---|---|---|
| **Entra** | Enunciado do projeto (nada de sprint anterior) | — |
| **Sai** | Canvas de kickoff (personas, princípios de acessibilidade, decisão apoiada) | Sprints seguintes |
| **Sai** | Lista fechada de features da v1 | Sprint 2 (lexer/gramática) e 3 (parser) |
| **Sai** | Especificação léxica (tabela de tokens + expressões regulares) | Sprint 2 **é obrigada a usar esta especificação** |
| **Sai** | Rascunho da gramática (EBNF) + exemplos de programas-alvo | Sprint 2 (revisão e implementação) |

**Não sai daqui:** lexer implementado, parser, AST, análise semântica.

---

## 1. Canvas de kickoff

| Pergunta | Resposta |
|---|---|
| Pergunta | Resposta |
|---|---|
| Quem é o público-alvo (persona) e que decisão/tarefa a linguagem apoia? | Pessoas com TEA que estão aprendendo logica de programação. Educadores para acompanhar e orientar o aprendizado do aluno. A linguagem deve permitir a criação de pequenos programas e fornecer feedback claro sobre erros, ajudando o usuário com o que corrigir para continuar. |
| Quais princípios de acessibilidade vão orientar a sintaxe (ex.: uma instrução por linha, palavras-chave simples, baixa ambiguidade)? | Palavras chaves, claras e simples em português (Prioridade: Alta). Redução de uso de simbolos, como {} ou ||, que possam causar confusão, trocar por palavras específicas como INICIO, FIM e OU (Prioridade: Alta). Sintaxe previsivel (Prioridade: Média). Preferencia por uma instrução por linha e comandos curtos (Prioridade: Média). Mensagens de erros claras e imediatas. (Média-Baixa) |
| Qual é o custo de uma sintaxe ainda ambígua vs. uma sintaxe restritiva demais? Qual é mais grave? | Uma sintaxe ambigua possui custo alto, pois dificulta a leitura e escrita do programa e comprometer o principal objetivo do projeto. Uma sintexe restritiva possui custo medio já que limita o que pode ser desenvolvido, porem pode ser ampliada futuramente, por isso em nosso projeto a ambiguidade pode ser considerada o problema mais grave. |
| Justificativa da escolha desses princípios (referências de acessibilidade cognitiva consultadas) | Os principios em nosso projeto foram escolhidos com base em diretrizes de acessibilidade cognitiva, voltadas mais a clareza e previsibilidade, e em literatura sobre TEA e ensino de programação. Essas referencias servem para orientar uma sintaxe simples, com vocabulario consistente e mensagens de erro diretas. |

- [ X ] Persona e decisão apoiada descritas com clareza
- [ X ] Princípios de acessibilidade listados e priorizados (qual erro de design é mais grave)

## 2. Lista fechada de features da v1

- [ X ] Lista de construções da linguagem fechada (ex.: variáveis, atribuição, condicional simples, laço simples, saída de texto)
- [ X ] Cada feature justificada pelo objetivo pedagógico/acessível da linguagem
- [ X ] Features explicitamente fora do escopo da v1 registradas (para não crescer depois)

**Features dentro da v1:** 
1. **Comandos de ação direta:** Palavras-chave em português, sem abreviações e sem símbolos especiais complexos ({}, ;, &&). elimina a objeção/abstração do inglês e a sobrecarga de memorizar símbolos( ex: () ), permite o processo literal e direto de um comando dado pelo usuário. Ex: SE x MAIOR_QUE 5 ENTÃO:.
2. **Linguagem não tipada:** Essa restrição de tipos tem como objetivo reduzir a carga cognitiva e a abstração para a criança com TEA. Assim fazendo com que o aluno apenas declare a variável sem se preocupar com o seu tipo. Em linguagens tradicionais, termos inteiros, decimais (float), números negativos e números gigantes. Para o público-alvo isso gera abstrações desnecessárias que aumentam o risco de erro ou confusão.
3. **Variáveis e atribuição:** As variáveis e atribuição serão declaradas como na linguagem Python, por serem consideradas intuitivas e fáceis de se aplicar no contexto TEA. As variáveis terão a mesma regra de nomeação, onde não podem começar com um número ou terem espaço. O símbolo de atribuição será o símbolo "=".
4. **Estruturas de Controles:** Serão usados laços condicionais e repetição simples para que os alunos sejam expostos a tais conceitos, mas, que ainda mantenha execução e sintaxe simples. Deixando bem claro onde o bloco começa e termina e qual tipo de laço estão utilizando.
- Laço condicional simples: SE condição ENTÃO ... FIM_SE
- Laço repetição não-determinístico simples: ENQUANTO condição FACA ... FIM_ENQUANTO
- Laço repetição determinístico simples: REPITA quantidade VEZES ... FIM_REPITA
5. **Saída e Entrada:** Os comandos de entrada e saída serão curtos, objetivos e intuitivos para o aluno poder interagir e observar os resultados do seu programa. LEIA será usado para o programar capturar o valor de entrada. ESCREVA será usado para o programa escrever resultados de variáveis ou textos no output. 
6. **Mensagens de erro humanizada:** crianças com espectro autista tendem a ter baixa tolerância á frustração causada por erros opacos e ruidosos. O erro direcionado por um alerta amigável e simples pode diminuir e manter o engajamento sem causar ansiedade (overload) e irritação, até perda de interesse.

**Features fora da v1 (adiadas ou descartadas):**
1. **Funções:**
    -*motivo:* Vamos focar na semántica simples, então iremos utilizar apenas um escopo do programa e execução simples.
2. **Tipos de dados avançados (float, string, matrizes):**
    -*motivo:* abstração matemática desnecessária para o conceito inicial de lógica do grid
3. **Funções customizadas com parâmetro:**
    -*motivo:* o conceito de escopo de pilha e retorno de funções é demasiadamente abstrato para a v1.

## 3. Especificação léxica

- [ X ] Tabela de tokens (palavras-chave, identificadores, literais, símbolos) com expressão regular de cada um
- [ X ] Palavras-chave escolhidas alinhadas aos princípios de acessibilidade da seção 1
- [ X ] Casos de ambiguidade léxica verificados (ex.: um token não pode ser prefixo problemático de outro)

**Tabela de tokens:**

| Token | Expressão regular | Exemplo |
|---|---|---|
|KW_PROGRAMA    	(?i)\bprograma\b	        programa
|KW_FIM_PROGRAMA	(?i)\bfim_programa\b	    fim_programa
|KW_CONSTANTE	    (?i)\b(constante|const)\b	constante
|COMENTARIO     	(//.|(?i)nota:.)	        // comentário ou nota: obs
|KW_ESCREVA	        (?i)\bescreva\b	            escreva
|KW_LEIA	        (?i)\bleia\b	            leia
|OP_SOMA_SUB_MULT	[\+\-\*]	                 +, -, *
|KW_DIVIDIDO_POR	(?i)\bdividido_por\b	     dividido_por
|KW_DIV_INTEIRA	    (?i)\bdivisao_inteira\b	     divisao_inteira
|KW_RESTO_DE	    (?i)\bresto_de\b	            resto_de
|KW_JUNTE	        (?i)\bjunte\b	                junte
|KW_IGUAL_A	        (?i)\bigual_a\b	                igual_a
|KW_DIFERENTE_DE	(?i)\bdiferente_de\b	        diferente_de
|KW_MAIOR_QUE	    (?i)\bmaior_que\b	            maior_que
|KW_MENOR_QUE	    (?i)\bmenor_que\b	            menor_que
|KW_MAIOR_IGUAL	    (?i)\bmaior_ou_igual_a\b	    maior_ou_igual_a
|KW_MENOR_IGUAL	    (?i)\bmenor_ou_igual_a\b	    menor_ou_igual_a
|KW_E	            (?i)\be\b	                    e
|KW_OU	            (?i)\bou\b	                    ou
|KW_NAO	            (?i)\bnao\b	                    nao
|KW_SE	            (?i)\bse\b	                    se
|KW_ENTAO	        (?i)\bentao\b	                entao
|KW_SENAO	        (?i)\bsenao\b	                senao
|KW_FIM_SE	        (?i)\bfim_se\b	                fim_se
|KW_ENQUANTO	    (?i)\benquanto\b	            enquanto
|KW_FACA	        (?i)\bfaca\b	                faca
|KW_FIM_ENQUANTO	(?i)\bfim_enquanto\b	        fim_enquanto
|KW_REPITA	        (?i)\brepita\b	                repita
|KW_VEZES	        (?i)\bvezes\b	                vezes
|KW_FIM_REPITA	    (?i)\bfim_repita\b	            fim_repita
|KW_PARAR	        (?i)\bparar\b	                parar
|OP_ATRIBUICAO	     =	                             =
|IDENTIFICADOR	    [a-zA-Z_][a-zA-Z0-9_]*	        idade, total_passos
|ABRE_FECHA_PAREN	[\(\)]	                        (, )
|QUEBRA_LINHA	    \n+	                            \n

## 4. Rascunho da gramática e exemplos-alvo

- [ X ] Gramática em EBNF cobrindo todas as features da lista fechada (seção 2)
- [ X ] Pelo menos 3 programas de exemplo que a linguagem deve conseguir expressar
- [ X ] Derivação manual de pelo menos 1 exemplo, para checar se a gramática realmente gera o programa esperado

**Gramática (EBNF):**
(* ============ PROGRAMA ============ *)
programa      = { comando } ;

comando       = ( atribuicao
                | leitura
                | escrita
                | condicional
                | enquanto
                | repita ) , NOVA_LINHA ;

(* ============ COMANDOS SIMPLES ============ *)
atribuicao    = IDENTIFICADOR , "=" , expressao ;
leitura       = "LEIA" , IDENTIFICADOR ;
escrita       = "ESCREVA" , expressao ;

(* ============ ESTRUTURAS DE CONTROLE ============ *)
condicional   = "SE" , condicao , "ENTAO" , NOVA_LINHA ,
                { comando } ,
                [ "SENAO" , NOVA_LINHA , { comando } ] ,   (* opcional, ver nota 5 *)
                "FIM_SE" ;

enquanto      = "ENQUANTO" , condicao , "FACA" , NOVA_LINHA ,
                { comando } ,
                "FIM_ENQUANTO" ;

repita        = "REPITA" , expressao , "VEZES" , NOVA_LINHA ,
                { comando } ,
                "FIM_REPITA" ;

(* ============ CONDIÇÕES ============ *)
condicao      = termo_logico , { "OU" , termo_logico } ;
termo_logico  = fator_logico , { "E" , fator_logico } ;
fator_logico  = [ "NAO" ] , comparacao ;
comparacao    = expressao , comparador , expressao ;
comparador    = "IGUAL_A"
              | "DIFERENTE_DE"
              | "MAIOR_QUE"
              | "MENOR_QUE"
              | "MAIOR_OU_IGUAL_A"
              | "MENOR_OU_IGUAL_A" ;

(* ============ EXPRESSÕES (sem parênteses) ============ *)
expressao     = termo , { ( "+" | "-" ) , termo } ;
termo         = fator , { ( "*" | "DIVIDIDO_POR" | "RESTO_DE" ) , fator } ;
fator         = [ "-" ] , valor ;
valor         = NUMERO | TEXTO | IDENTIFICADOR ;

(* ============ LÉXICO ============ *)
IDENTIFICADOR = ( letra | "_" ) , { letra | digito | "_" } ;   (* exceto palavras reservadas *)
NUMERO        = digito , { digito } , [ "." , digito , { digito } ] ;
TEXTO         = '"' , { qualquer_caractere_exceto_aspas } , '"' ;
letra         = "a".."z" | "A".."Z" | "á" | "é" | "í" | "ó" | "ú"
              | "â" | "ê" | "ô" | "ã" | "õ" | "ç" ;
digito        = "0".."9" ;
NOVA_LINHA    = "\n" ;

PALAVRAS_RESERVADAS = "SE" | "ENTAO" | "SENAO" | "FIM_SE"
                    | "ENQUANTO" | "FACA" | "FIM_ENQUANTO"
                    | "REPITA" | "VEZES" | "FIM_REPITA"
                    | "LEIA" | "ESCREVA" | "E" | "OU" | "NAO"
                    | "DIFERENTE_DE" | "MAIOR_QUE" | "MENOR_QUE"
                    | "MAIOR_OU_IGUAL_A" | "MENOR_OU_IGUAL_A" | "IGUAL_A";

**Programas de exemplo:**
1. Verificar se número é "grande" ou não
PROGRAMA
ESCREVA "Qual é o seu número?"
LEIA numero
contador = 0
REPITA numero VEZES
    contador = contador + 1
FIM_REPITA
SE contador MAIOR_QUE 5 ENTAO
    ESCREVA "Número grande!"
FIM_SE
FIM_PROGRAMA

2. Verificar se número é par ou não
PROGRAMA
ESCREVA "Digite um número qualquer:"
LEIA numero
SE RESTO_DE numero IGUAL_A 0
    ESCREVA "Seu número é par!"
FIM_SE
FIM_PROGRAMA

3. Somando de dobro de cada numero até 3, desde que o resultado não seja maior que 100
soma = 0
contador = 1
ENQUANTO contador MENOR_OU_IGUAL 3 E NAO soma MAIOR_QUE 100 FACA
    soma = soma + contador * 2
    contador = contador + 1
FIM_ENQUANTO
ESCREVA "Soma: " + soma

Resultado esperado: "Soma: 12"

Teste de Mesa:
1	soma = 0	0	n/d	n/d
2	contador = 1	0	1	n/d
	ENQUANTO, avaliação 1	0	1	1 <= 3 e NAO (0 > 100) → verdadeira
3	soma = soma + contador * 2 → 0 + 1*2	2	1	n/d
4	contador = contador + 1	2	2	n/d
	ENQUANTO, avaliação 2	2	2	2 <= 3 e NAO (2 > 100) → verdadeira
5	soma = 2 + 2*2	6	2	n/d
6	contador = 2 + 1	6	3	n/d
	ENQUANTO, avaliação 3	6	3	3 <= 3 e NAO (6 > 100) → verdadeira
7	soma = 6 + 3*2	12	3	n/d
8	contador = 3 + 1	12	4	n/d
	ENQUANTO, avaliação 4	12	4	4 <= 3 → falsa, sai do laço
9	ESCREVA "Soma: " + soma	12	4	n/d

## 5. Scrum

- [ X ] Papéis definidos (Product Owner = docente; Scrum Master do sprint; Development Team)
- [ X ] Board criado (GitHub Projects ou Trello) com To do / Doing / Done
- [ X ] Backlog inicial com pelo menos 3 user stories

**Papéis:**
- Product Owner: Andrea Ono Sakai
- Scrum Master: Matheus
- Development Team: Julia, Matheus, Ronald e William

**User stories do backlog inicial:**
1. O estudante pode escrever um programa usando a linguagem que será criada.
2. O compilador pode identificar erros no código e mostrar uma mensagem clara sobre o problema.
3. O compilador pode verificar se o código segue as regras da linguagem.

**Link do board:** https://github.com/users/juliavsantos/projects/1

## 6. Diário de bordo (retrospectiva individual)

| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|---|---|---|---|
| Ronald Lopes Alencar do Rosario | Ajudei a definir o pubico alvo, os principios de acessibilidade, a features iniciais da linguagem e participei da pesquisa de refetencia para TEA e ensino de programação | a principal dificuldade foi pensar em uma sintaxe simples sem limitar demais a linguagem. | pretendo manter o foco em clareza e simplicidade e ajustar a linguagem conforme surgirem ambiguidades ou dificuldades nas proximas etapas. |
| Julia Aparecida Venâncio dos Santos | Participei da definição dos princípios da linguagem, da especificação dos tokens e da organização das etapas do projeto. Também ajudei na organização do GitHub e das evidências da Sprint.| Tive dificuldade para definir quais características da linguagem poderiam contribuir para uma sintaxe mais clara e previsível, além de organizar as informações da Sprint.|Manter a organização das tarefas e das evidências. Ajustar a definição da linguagem conforme as decisões do grupo e as referências utilizadas no projeto.|
| William Souza | Editei passo 2 e 3 sendo eles a lista fechada de features da v1, e a tabela de tokens, pesquisei, abordei o tópico e discuti com os demais integrantes do projeto para discernir ideias, foco do projeto e alinhamento de ideias de implementação, avaliação do que estava sendo escrito e comparativos com a premissa do projeto. Realizei pesquisa corrida de conceitos sobre análises léxica, sintática, validação de caracteres, desing de linguagem e propriedades de uma linguagem de programação voltado ao ensino e apoio ao público de destino (TEA), para me introduzir sobre o que seria necessário implementar posteriormente e ter clareza de como a linguagem deve se comportar. Encontrei um pouco de dificuldade em escrever alguns tópicos do passo 2, como o que seria excluido ou deixado de fora da v1, na primeira fase não seria viável, e também na tabela, como tokens e expressão regulares, já que fiquei um pouco perdido e sem saber como estruturar o conjunto, bem como a cadeia de caracteres pertencente ao alfabeto da linguagem que selecionamos. | Irei manter todos neste primeiro modo, já foi discutido e concordado assim.|
| Matheus Akira Saito de Souza | Defini parte da linguagem em grupo, discuti e trouxe problemas de acessibilidade de acordo com os artigos que baseiam o projeto para a definição da linguagem. Editei o passo 4 definindo o rascunho da linguagem no formato EBNF. Revisei os passos 1 e 2.| Entender as necessidades da linguagem para pessoas com TEA, e nas funcionalidades que temos que abstrair para facilitar a linguagem | Organizar tempo e horário para o projeto, Manter e organizar de maneira estrutura as tarefas e obrigações e ajustar a definição da nossa linguagem |

## 7. Evidências gerais

- Link da especificação léxica: https://drive.google.com/drive/folders/1Dg_Qa4gx0Hbu5rMRUk6QghtaZSh6qZ8O?usp=sharing
- Link do rascunho da gramática: https://docs.google.com/document/d/1CFzWWAhGM3eqMH_sSkr1Ym1aUHOH6hIvEOzyJ-lH7Xg/edit?usp=sharing
- Link do board: https://github.com/users/juliavsantos/projects/1

---

## Rubrica de avaliação — Sprint 1 (nota de 0 a 4,0)

| Critério | Peso | O que caracteriza nota máxima | Nota atribuída | Observações |
|---|---|---|---|---|
| Canvas e princípios de acessibilidade | 0,5 | Persona clara; princípios priorizados e justificados | | |
| Lista fechada de features | 0,5 | Escopo v1 claro e justificado; fora de escopo registrado | | |
| Especificação léxica | 1,0 | Tokens completos, expressões regulares corretas, sem ambiguidade óbvia | | |
| Rascunho da gramática e exemplos | 1,5 | Gramática cobre a lista de features; exemplos derivados corretamente | | |
| Scrum + diário de bordo | 0,5 | Papéis, board, backlog e diário reflexivo de todos | | |
| **Nota final da Sprint 1** | **4,0** | | **___ / 4,0** | |
