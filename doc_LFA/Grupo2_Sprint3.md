# Diário de Sprint 3 — Parser, AST e análise semântica
**Período:** Semanas 3–4
**Grupo / tema:** Grupo 2 — Compilador para DSL acessível para pessoas com TEA

**Equipe:** Julia Aparecida Venâncio dos Santos; Matheus Akira Saito de Souza; Ronald Lopes Alencar do Rosario; William Souza da Silva
**Scrum Master do Sprint:**
**Repositório GitHub:** [https://github.com/juliavsantos/TEApiler-Compilador-Acessivel]

> Lexer funcional e gramática validada na Sprint 2. Esta sprint constrói o **parser**, a **AST** e a **análise semântica básica**, com mensagens de erro pensadas para o público da linguagem (princípios de acessibilidade da Sprint 1). **Não** reabre a gramática sem justificar.

### Contrato desta sprint

| | Artefato | Origem / destino |
|---|---|---|
| **Entra** | Lexer funcional + gramática congelada | Sprint 2 — **mesma gramática, salvo ajuste justificado** |
| **Entra** | Programas de exemplo (válidos/inválidos) | Sprint 2 |
| **Sai** | Parser gerando AST | Sprint 4 (testes finais) |
| **Sai** | Análise semântica básica (tabela de símbolos, checagem de declaração/tipo) | Sprint 4 |
| **Sai** | Mensagens de erro específicas e claras | Sprint 4 (refinamento final) |

**Não sai daqui:** bateria de testes automatizados completa, manual da linguagem, geração de código.

- [x] Confirmei que o parser usa a gramática congelada da Sprint 2

---

## 1. Implementação do parser

- [x] Estratégia de parsing definida (recursivo descendente ou tabela LL(1)) e justificada
- [x] Parser cobre todas as regras da gramática congelada
- [x] Erros sintáticos tratados com mensagem indicando onde e o que era esperado

**Estratégia escolhida e justificativa:**
Escolhemos o parser descendente recursivo, com um token de olhada à frente (LL(1)). Na prática, cada regra da gramática virou uma função, e o parser decide o caminho olhando só o token atual, sem voltar atrás. Isso deixou o código parecido com a gramática, o que ajudou muito a entender, testar e arrumar.
Também resolvemos a precedência dos operadores com níveis de regras (comparação, soma, termo e fator), sem precisar de tabela extra. Também estabelecemos que a combinação dos operadores lógicos E e OU na mesma expressão exige o uso de parênteses. Essa decisão evita ambiguidades e torna a interpretação das expressões mais previsível.
O principal motivo da escolha foi o controle das mensagens de erro. Por ser uma implementação própria, conseguimos dizer exatamente onde o problema está, o que esperávamos ver e o que apareceu no lugar. Ele para no primeiro erro, para não encher a tela de mensagens em cascata, que só confundiriam quem está aprendendo.
**Evidências (link do repositório/commit):** [https://github.com/juliavsantos/TEApiler-Compilador-Acessivel/blob/main/src/compilador/parser.py]

## 2. Construção da AST

- [x] Estrutura de nós da AST definida para cada construção da linguagem (variável, atribuição, condicional, laço, saída)
- [x] Parser gera a AST corretamente para os programas de exemplo válidos da Sprint 2
- [x] AST impressa/visualizada para pelo menos 2 exemplos, para conferência manual

**Estrutura da AST (resumo) e exemplos gerados:**

A estrutura da AST foi definida por meio da classe `No`, responsável por representar os elementos do programa. Cada nó possui um tipo, informações de localização no código (linha e coluna) e campos específicos de acordo com a construção representada.

Foram implementados nós para representar programas, variáveis, atribuições, constantes, operações aritméticas, relacionais e lógicas, valores numéricos, textos e lógicos, comandos de entrada e saída, estruturas condicionais e estruturas de repetição.

A construção da AST ocorre durante a análise sintática, organizando os elementos do código em uma estrutura hierárquica que facilita as próximas etapas do compilador, especialmente a análise semântica.

### Exemplo 1 (7 nós)
```
Programa
└─ corpo: Atribuir nome='x'
   └─ valor: OpAritmetica op='*'
      ├─ esq: Numero valor=2
      └─ dir: OpAritmetica op='+'
         ├─ esq: Numero valor=3
         └─ dir: Numero valor=1
```

### Exemplo 2 (11 nós)
```
Programa
├─ corpo: Atribuir nome='idade'
│  └─ valor: Numero valor=20
└─ Se
   ├─ condicao: OpRelacional op='MAIOR_OU_IGUAL'
   │  ├─ esq: Variavel nome='idade'
   │  └─ dir: Numero valor=18
   ├─ entao: Escreva
   │  └─ valor: Texto valor='Maior de idade'
   └─ senao: Escreva
      └─ valor: Texto valor='Menor de idade'
```

## 3. Análise semântica básica

- [ X ] Tabela de símbolos implementada (nome, tipo, escopo)
- [ X ] Checagem de declaração antes do uso
- [ X ] Checagem de tipos simples (conforme as features da v1)
- [ X ] Cada regra semântica testada com pelo menos 1 caso que a viola

**Regras semânticas implementadas e como foram testadas:**

- 1 - **Declaração de Variáveis:** Variáveis não podem ser usadas, como em escrita ou uma condição, antes de serem declaradas. O mesmo vale para variáveis que foram declaradas dentro de blocos condicionais/repetição. Ambos devem ser tratados como erros e parar execução do programa

Exemplos:
```
ANOTA: Permitido

x = 10

ESCREVA x
```

```
ANOTA: Não Permitido

ESCREVA x
ANOTA: x nunca foi declarado nesse programa
```
```
ANOTA: Permitido

x = 5 
y = 0

SE x MENOR_IGUAL 5 ENTAO:
  y = y + x
FIM_SE

ESCREVA y
```
```
ANOTA: Não Permitido

x = 5 

SE x MENOR_IGUAL 5 ENTAO:
  y = y + x
FIM_SE

ESCREVA y
ANOTA: y foi declarado em um bloco condicional, y precisa ser declarado antes
```

- 2 - **Alteração de constantes**: Constantes podem ser apenas atribuidas um valor na primeira vez que são declaradas, e não podem ser alteradas no decorrer do programa. Caso isso aconteça deve ser tratado como erro e parar a execução do programa

Exemplos:
```
ANOTA: Permitido

CONSTANTE x = 10
```
```
ANOTA: Não Permitido

CONSTANTE x = 10

CONSTANTE x = 5
ANOTA: x é uma constante e não pode ser alterado
```

- 2.1 - **Leitura em constantes**: Leitura em constantes não deve ser permitida, apenas valores fixos devem ser atribuidos a constantes. Caso isso aconteça deve ser tratado como erro e parar a execução do programa
Exemplos:
```
ANOTA: Permitido

CONSTANTE x = 10
```
```
ANOTA: Não Permitido

CONSTANTE x

LEIA x
ANOTA: x é uma constante e não pode ser lida
```

- 2.2 - **Variáveis não devem ter o mesmo nome que constantes**: Se uma constante for declarada com um certo nome, uma variável não pode utilizar o mesmo nome que a constante. Caso isso aconteça deve ser tratado como erro e parar a execução do programa
```
ANOTA: Permitido

CONSTANTE x = 10

y = 5
```
```
ANOTA: Não Permitido

CONSTANTE x = 10

x = 5
ANOTA: x já é uma constante, não é permitido usar o mesmo nome
```

- 2.3 - **Variáveis não podem ser utilizados para declarar um valor a uma constante**: É proibido utilizar variáveis na atribuição de constante por não garantir valores fixos. Caso isso aconteça deve ser tratado como erro e parar a execução do programa.
```
ANOTA: Permitido

y = 5

CONSTANTE x = 10

y = y + x
```
```
ANOTA: Não Permitido

y = 5

CONSTANTE x = 10 + y

ANOTA: x é uma constante, e não pode usar variáveis em sua declaração
```

- 3 - **PARAR funciona apenas em laços de repetição**: O palavra chave PARAR pode apenas ser usada em laços como ENQUANTO ou REPETIR. Caso isso aconteça deve ser tratado como erro e parar a execução do programa.
```
ANOTA: Permitido

ENQUANTO x MENOR_QUE 10 FACA:
  x = x + 1
  PARAR
FIM_ENQUANTO
  
```
```
ANOTA: Não Permitido

SE x IGUAL_A 5 ENTAO:
  ESCREVA "igual"
SENAO:
  ESCREVA "diferente"
  PARAR
FIM_SE

ANOTA: PARAR só é permitido dentro de laços de repetição
```

- 4 - **O valor de condição de repita precisa ser um número**: O laço REPITA não pode ter outro tipo de dado além de número em sua condicional. Caso isso aconteça deve ser tratado como erro e parar a execução do programa.
```
ANOTA: Permitido

REPITA 3 VEZES:
  ESCREVA "Ola Mundo"
FIM_REPITA
  
```
```
ANOTA: Não Permitido


REPITA "tres" VEZES:
  ESCREVA "Ola Mundo"
FIM_REPITA

ANOTA: REPITA só pode usar números em sua condição
```

- 4.1 - **O valor de condição de repita não pode ser negativo**: O laço REPITA não pode ter um número negativo em sua condicional. Caso isso aconteça deve ser tratado como erro e parar a execução do programa.
```
ANOTA: Permitido

REPITA 3 VEZES:
  ESCREVA "Ola Mundo"
FIM_REPITA
  
```
```
ANOTA: Não Permitido


REPITA -3 VEZES:
  ESCREVA "Ola Mundo"
FIM_REPITA

ANOTA: REPITA não pode usar números negativos
```

- 4.2 - **O valor de condição de repita não pode ser um valor decimal**: O laço REPITA não pode ter um número decimal em sua condicional. Caso isso aconteça deve ser tratado como erro e parar a execução do programa.
```
ANOTA: Permitido

REPITA 3 VEZES:
  ESCREVA "Ola Mundo"
FIM_REPITA
  
```
```
ANOTA: Não Permitido


REPITA 3.14 VEZES:
  ESCREVA "Ola Mundo"
FIM_REPITA

ANOTA: REPITA não pode usar números decimais
```

- 4.3 - **O valor de condicionais precisa ser lógico**: O laço ENQUANTO e a condicional SE precisa ter um valor lógico em suas condições. Caso isso aconteça deve ser tratado como erro e parar a execução do programa.
```
ANOTA: Permitido

SE x MAIOR_QUE 2 ENTAO:
  ESCREVA "maior"
  
```
```
ANOTA: Não Permitido

SE "x maior que 2" ENTAO:
  ESCREVA "maior"

ANOTA: Condicionais só podem usar valores lógicos em suas condições
```

- 5 - **Contas aritméticas permitem apenas números**: Não é permitido utilizar textos ou valores lógicos em contas aritméticas. Caso isso aconteça deve ser tratado como erro e parar a execução do programa.
```
ANOTA: Permitido

x = 10 + 2
  
```
```
ANOTA: Não Permitido

x = 10 + "dois"

y = 15 + VERDADE

ANOTA: Contas aritméticas só são permitidos números
```

- 6 - **Comparação de tipos diferentes**: Não é permitido comparar textos com números, utilize tipos iguais para comparar. Caso isso aconteça deve ser tratado como erro e parar a execução do programa.
```
ANOTA: Permitido

10 IGUAL_A 10

"a" IGUAL_A "a"
  
```
```
ANOTA: Não Permitido

"10" MAIOR_QUE 10

ANOTA: Não é possível fazer comparação de textos
``` 

- 6.1 - **Comparação de lógicos**: Não é permitido fazer certas comparações com valores lógicos, apenas IGUAL_A e DIFERENTE_DE. Caso isso aconteça deve ser tratado como erro e parar a execução do programa.
```
ANOTA: Permitido

VERDADE DIFERENTE_DE FALSO
  
```
```
ANOTA: Não Permitido

VERDADE MAIOR_QUE FALSO

ANOTA: Certas operações não são permitidas com valores lógicos.
``` 

- 7 - **Igualdade de tipos diferentes**: Não é permitido fazer certas comparações de igualdade com tipo diferentes, apenas do mesmo tipo. Caso isso aconteça deve ser tratado como erro e parar a execução do programa.
```
ANOTA: Permitido

10 IGUAL_A 10
  
```
```
ANOTA: Não Permitido

10 IGUAL_A "10"

ANOTA: Comparações de IGUAL_A só são permitidas com tipos de dados iguais.
```

- 8 - **Operações lógicas com tipos não lógicos**: Não possível fazer operações lógicas (E/OU/NAO) com tipos de dados como apenas números ou textos, as operações precisam responder se é verdade ou falso. Caso isso aconteça deve ser tratado como erro e parar a execução do programa.
```
ANOTA: Permitido

var MAIOR_QUE 0 E var MENOR_QUE 10
  
```
```
ANOTA: Não Permitido

NAO 5

5 E 10

ANOTA: Operações lógicas desse tipo devem retornar uma resposta com VERDADE ou FALSO.
```

- 9 - **Divisão por zero**: Operações de divisão (/) e RESTO_DE não podem utilizar o número zero na expressão. Caso isso aconteça deve ser tratado como erro e parar a execução do programa.
```
ANOTA: Permitido

x = 10 / 5

y = 10 RESTO_DE 2
  
```
```
ANOTA: Não Permitido

x = 10 / 0

y = 10 RESTO_DE 0

ANOTA: Operações de divisão não podem ser dividias por zero.
```

- 10 - **Laços que não terminam**: O laço de repetição ENQUANTO pode nunca terminar. Caso isso aconteça o analisador deve avisar ao aluno do problema, mas não parar a execução do programa.
```
ANOTA: Permitido

ENQUANTO VERDADE FACA:
  PARAR
FIM_ENQUANTO 
  
```
```
ANOTA: Permitido com Ressalvas 

ENQUANTO VERDADE FACA:
  ESCREVA "infinito"
FIM_ENQUANTO

ANOTA: A condição é sempre verdade e nunca termina

ENQUANTO x MENOR_QUE 5 FACA:
  ESCREVA x
FIM_ENQUANTO

ANOTA: A condição tem um fim, mas x nunca muda para, então a laço também nunca termina
```

- 11 - **Código depois de uma PARAR**: Todo código depois de um PARAR não é executado. Caso isso aconteça o analisador deve avisar ao aluno do problema, mas não parar a execução do programa.
```
ANOTA: Permitido

ENQUANTO VERDADE FACA:
  ESCREVA "Ola Mundo"
  PARAR
FIM_ENQUANTO 
  
```
```
ANOTA: Permitido com Ressalvas 

ENQUANTO VERDADE FACA:
  ESCREVA "Ola Mundo"
  PARAR
  ESCREVA "Boa noite mundo"
FIM_ENQUANTO

ANOTA: ESCREVA "Boa noite mundo" nunca é executado por conta do PARAR
```

- 11 - **Bloco Vazio**: Laços de repetição e condicional podem ter seu bloco de execução vazio. Caso isso aconteça o analisador deve avisar ao aluno do problema, mas não parar a execução do programa.
```
ANOTA: Permitido

x = 10
y = 5

SE x MAIOR_QUE y ENTAO:
  ESCREVA "maior"
FIM_SE 
  
```
```
ANOTA: Permitido com Ressalvas

x = 10
y = 5

SE x MAIOR_QUE y ENTAO:

FIM_SE 

ANOTA: Bloco está vazio
```

- 11 - **Nome reservado minúsculo**: Nomes reservados na linguagem são em maisculo, o que permite que variáveis tenham o mesmo nome só que minúsculo. Caso isso aconteça o analisador deve avisar ao aluno do problema, mas não parar a execução do programa.
```
ANOTA: Permitido

mensagem = "Ola Mundo"

ESCREVA mensagem
  
```
```
ANOTA: Permitido com Ressalvas

escreva = "Ola Mundo"

ESCREVA escreva

ANOTA: O nome da variável é a palavra reservada ESCREVA só que minúsculo, o que é permitido mas com cuidado.
```

## 4. Mensagens de erro acessíveis

- [ ] Mensagens de erro léxico, sintático e semântico revisadas conforme os princípios de acessibilidade da Sprint 1 (claras, específicas, sem jargão desnecessário)
- [ ] Cada mensagem indica o que está errado e, quando possível, uma sugestão de correção

**Exemplos de mensagens de erro (antes/depois da revisão):**

### Exemplo Erro Léxico

Antes
```
X == 2

Símbolo de comparador não compátivel com a linguagem
```

Depois
```
X == 2

• Linha 1: Opa! O comparador == está usando um símbolo de outra linguagem...Você quis dizer IGUAL_A?
```

### Exemplo Erro Sintático

Antes
```
SE x DIFERENTE_DE 2
  ESCREVA x
FIM_SE

Erro Sintático: O bloco de código não está correto, por favor verifique a sintaxe
```

Depois
```
SE x DIFERENTE_DE 2
  ESCREVA x
FIM_SE

Erro sintático [Linha 1]: Eu esperava a palavra ENTAO, mas encontrei o fim da linha.
```

### Exemplo Erro Semântico

Antes
```
ESCREVA x
 
Ainda não foi dado valor a variável, por favor inicie a variável antes de usar
```

Depois
```
ESCREVA x

Erro: linha 1: Ainda não foi dado valor a variável "x" ... Por favor, dê um valor antes de usá-la | Exemplo: x = 10
```

## 5. Sprint Review — checkpoint intermediário

**Incremento demonstrado ao PO (docente):**
**Feedback recebido:**

## 6. Scrum

- [ X ] Atualizações assíncronas semanais registradas
- [ X ] Board refletindo o estado real da Sprint

## 7. Diário de bordo (retrospectiva individual)

| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|---|---|---|---|
| Julia | Implementou o analisador sintático e o tratamento de erros sintático, testou IDE e mensagens de erros sintáticos, corrigiu erros relacionados ao imports da IDE, implementou visualizador_ast e mostrar_ast para falicitar visualização da AST gerada pelo analisador | Testar analisador sintático e implementar recursos extras para a AST | Pretendo ajustar a análise sintática para se ajustar a detalhes da gramática EBNF |
| Matheus | Implementou o analisador semântico, tabela de símbolos e o tratamento de erros semântico, implementou analisador semântico na IDE e corrigiu erros relacionados, testou IDE e mensagens de erros semânticos | Estudar e implementar o analisador semântico, corrigir erros e avisos semânticos | Pretendo manter a maneira que os erros são reportados e ajusta-los com mais detalhes sobre estrutura, condição, etc. |
| Ronald | Implementou IDE com o analisador léxico, recursos de acessibilidade e opções limitadas e diretas com base nos recomendações das pesquisas e artigos, testou analisador léxico e erros léxicos | Conectar o analisador léxico ao IDE e certificar que IDE está de acordo com as recomendações dos nosso estudos | - |
| William | Implementou IDE, responsável pela implementação/design do blog, juntou as pesquisas para fundamentar o blog, testou IDE, analisador léxico e seus erros, implementou mini simulador léxico para melhor visualização do processo de tokenização do blog | Estruturar e atualizar o blog, estar de acordo com as recomendações dos estudar, estruturar apresentação | Pretendo ajustar o blog para que seja possível visualizar um exemplo fixo de AST |

---

## Rubrica de avaliação — Sprint 3 (nota de 0 a 4,0)

| Critério | Peso | O que caracteriza nota máxima | Nota atribuída | Observações |
|---|---|---|---|---|
| Parser e AST | 1,5 | Parser cobre a gramática congelada; AST correta nos exemplos válidos | | |
| Análise semântica | 1,0 | Tabela de símbolos, declaração/uso e tipos checados e testados | | |
| Mensagens de erro acessíveis | 1,0 | Mensagens claras e específicas, alinhadas aos princípios da Sprint 1 | | |
| Sprint Review / Scrum + diário | 0,5 | Incremento demonstrado; board e diário atualizados | | |
| **Nota final da Sprint 3** | **4,0** | | **___ / 4,0** | |
