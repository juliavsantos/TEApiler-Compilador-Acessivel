# RFC: Proposta de Projeto — Grupo 2

| Campo | Valor |
|---|---|
| **Título** | Compilador para [Nome da Linguagem] — DSL de programação acessível para pessoas com TEA |
| **Trilha** | Projeto novo — linguagem de programação educacional acessível (front-end de compilador) |
| **Equipe** | Grupo 2 |
| **Autores** | Julia Aparecida Venâncio dos Santos, Matheus Akira Saito de Souza, Ronald Alencar do Rosário, William Souza |
| **Status** | Rascunho |
| **Data** | |
| **Sprint de referência** | 1 |

> Este RFC formaliza a criação de uma DSL simples voltada a pessoas com TEA e do seu compilador (análise léxica, sintática e semântica). O produto da disciplina é o **compilador front-end validando corretamente programas**, não um produto educacional completo (isso é trabalho de outra disciplina). Geração de código executável real, IDE e testes de usabilidade com usuários reais **não** entram neste documento.

---

## 1. Resumo (TL;DR)

Propomos desenvolver uma linguagem de programação com sintaxe simples, previsível e de baixa ambiguidade, utilizando como referência características de acessibilidade encontradas na literatura sobre ensino de programação para pessoas neurodivergentes.
A partir dessa linguagem, será desenvolvido um compilador front-end composto por analisador léxico, analisador sintático, árvore sintática abstrata (AST) e análise semântica básica, acompanhado de mensagens de erro claras e específicas.

---

## 2. Contexto e motivação

Pessoas com TEA podem se beneficiar de linguagens de programação com sintaxe previsível, vocabulário consistente, baixa ambiguidade e feedback de erro direto — reduzindo carga cognitiva/sensorial ao aprender lógica de programação. O projeto aplica conceitos centrais da disciplina (expressões regulares, gramáticas livres de contexto, autômatos) ao desenho e à implementação dessa linguagem.

---

## 3. Problema formal e objetivo da linguagem

| Pergunta | Resposta |
|---|---|
| Problema de design que a linguagem resolve | Reduzir barreiras cognitivas/sensoriais na programação para pessoas com TEA |
| Princípios de acessibilidade que orientam a sintaxe | (ex.: uma instrução por linha, palavras-chave em português simples, ausência de símbolos ambíguos, mensagens de erro específicas — **detalhar na Sprint 1**) |
| Escopo funcional mínimo da v1 (viável em 5 semanas) | (ex.: variáveis, atribuição, condicional simples, laço simples, saída de texto — **fechar lista na Sprint 1**) |
| Unidade de compilação | Um programa-fonte = um arquivo da linguagem |

---

## 4. Escopo

| Pergunta | Resposta |
|---|---|
| Dentro do escopo | Especificação léxica (tokens via expressões regulares), gramática (EBNF/BNF), lexer, parser (AST), análise semântica básica (declaração antes do uso, tipos simples), mensagens de erro amigáveis |
| Fora de escopo | Geração de código de máquina/bytecode real, IDE completa, testes de usabilidade formais com usuários TEA reais, otimizações de compilador |

---

## 5. Usuários e decisão apoiada

Pessoa com TEA aprendendo lógica de programação (ou educador que a acompanha) usa o compilador para escrever pequenos programas e obter **feedback claro** sobre erros, decidindo o que corrigir antes de seguir em frente.

---

## 6. Referências de design (em vez de "dados")

| Fonte | O que fornece | Papel no projeto |
|---|---|---|
| Diretrizes de acessibilidade cognitiva (ex.: WCAG cognitive) | Princípios de clareza e previsibilidade | Orientam decisões de sintaxe |
| Literatura sobre TEA e ensino de programação | Boas práticas de design de linguagem | Orientam vocabulário e estrutura de erros |

---

## 7. Custo das decisões de design

| Tipo de erro de design | O que significa | Custo/consequência |
|---|---|---|
| Sintaxe ainda ambígua ou confusa | Usuário se perde ao ler/escrever o programa | Alto — compromete o objetivo central do projeto |
| Sintaxe excessivamente restritiva | Limita o que dá para expressar | Médio — atrapalha, mas é mais fácil de corrigir depois |

A ambiguidade é o erro mais grave e orienta a simplicidade extrema da gramática desde a Sprint 1.

---

## 8. Abordagem proposta (visão de alto nível)

definição de princípios de acessibilidade e lista fechada de features → especificação léxica (tokens, expressões regulares) → especificação sintática (gramática EBNF, testada manualmente contra ambiguidade) → implementação do lexer → implementação do parser (construção da AST) → análise semântica básica (tabela de símbolos, checagem de declaração/tipo) → tratamento de erros com mensagens claras → bateria de programas de teste (válidos e inválidos) → manual rápido da linguagem.

Não há geração de código executável real neste projeto — o entregável é o front-end validado.

---

## 9. Riscos e limitações conhecidas

- Prazo curto para validar acessibilidade de fato (sem testes com usuários reais)
- Ambiguidade gramatical não percebida a tempo
- Escopo da linguagem crescer além do viável (scope creep)
- Mensagens de erro genéricas demais se não houver tempo de refinar

---

## 10. Critérios de sucesso

- Gramática formalizada e sem ambiguidade relevante (ou documentada e resolvida)
- Compilador aceita corretamente todos os programas de teste válidos
- Compilador rejeita os inválidos com mensagens de erro específicas
- Cobertura completa das features definidas no escopo da v1
- Manual da linguagem entregue

---

## 11. Alternativas consideradas *(opcional)*

Outras abordagens de sintaxe (ex.: baseada em blocos visuais tipo Scratch) avaliadas e descartadas por fugirem do escopo de "compilador" da disciplina.

---

## 12. Perguntas em aberto

- Conjunto final de palavras-chave e sua tradução/simplificação (depende de validação informal na Sprint 1)
- Nível de detalhe da análise semântica (depende do tempo restante após a Sprint 3)

---

## 13. Cronograma e contrato entre sprints

| Sprint | Período | Produz (sai) | A próxima sprint é obrigada a usar |
|---|---|---|---|
| 1 | Semana 1 | Princípios de acessibilidade, lista fechada de features da v1, especificação léxica (tabela de tokens + ER), rascunho da gramática EBNF | Essa gramática, já congelada |
| 2 | Semana 2 | Lexer funcional, gramática revisada e testada manualmente (sem ambiguidade), conjunto de programas de exemplo (válidos/inválidos) | Os tokens gerados e a gramática congelada |
| 3 | Semanas 3–4 | Parser (AST), tabela de símbolos, checagem semântica básica, mensagens de erro | A AST e as análises já validadas |
| 4 | Semana 5 | Bateria de testes automatizados, manual da linguagem, ajuste final das mensagens de erro, demo | — (entrega final) |

---

## 14. Histórico de revisões

| Versão | Data | Autor | O que mudou |
|---|---|---|---|
| v0.1 | | | Primeira versão do RFC (Sprint 1) |
| | | | |
