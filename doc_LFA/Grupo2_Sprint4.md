# Diário de Sprint 4 — Testes, refinamento e entrega
**Período:** Semana 5
**Grupo / tema:** Grupo 2 — Compilador para DSL acessível para pessoas com TEA

**Equipe:** Julia Aparecida Venâncio dos Santos; Matheus Akira Saito de Souza; Ronald Lopes Alencar do Rosario; William Souza da Silva
**Scrum Master do Sprint:** Julia e Matheus
**Repositório GitHub:** [https://github.com/juliavsantos/TEApiler-Compilador-Acessivel]

> Parser, AST e análise semântica prontos na Sprint 3. Esta sprint **fecha o projeto**: bateria de testes automatizados, refinamento final e manual da linguagem. **Não há** sprint seguinte — esta é a entrega.

### Contrato desta sprint

| | Artefato | Origem / destino |
|---|---|---|
| **Entra** | Parser + AST + análise semântica | Sprint 3 — **não redesenhar do zero** |
| **Sai** | Bateria de testes automatizados | Entrega final |
| **Sai** | Manual da linguagem | Entrega final |
| **Sai** | Apresentação/demo final | Entrega final / mostra |

**Não há sprint seguinte.**

- [ X ] Confirmei que os testes cobrem todas as features da lista fechada da Sprint 1

---

## 1. Bateria de testes automatizados

- [ X ] Testes cobrindo cada feature da v1 (pelo menos 1 caso válido e 1 inválido por feature)
- [ X ] Testes de erro léxico, sintático e semântico, verificando a mensagem retornada
- [ X ] Todos os testes passando; falhas corrigidas ou documentadas como limitação conhecida

**Cobertura de testes (resumo) e link do repositório:**

Cobrimos todos os erros possíveis e que previmos que poderia acontecer e ser capturados pelo compilador. Focamos em verificar se a mensagem de erro que um código errado na nossa linguagem deve reportar está correta. Separamos em três batidas focando nos erros léxicos, sintáticos e semânticos.

Os três testes podem ser verificados utilizando esse comando:
``` 
> python -m unittest discover -s testes -v 
```

Link Repositório: [https://github.com/juliavsantos/TEApiler-Compilador-Acessivel]

## 2. Refinamento final

- [ X ] Mensagens de erro revisadas mais uma vez com base nos testes desta sprint
- [ X ] Ajustes pontuais na gramática/análise semântica, se necessário, com justificativa registrada
- [ x ] Casos-limite encontrados durante os testes tratados ou documentados como limitação

**Ajustes finais realizados:**

## 3. Manual da linguagem

- [ X ] Sintaxe de cada construção documentada com exemplo comentado
- [ X ] Lista de mensagens de erro possíveis e o que cada uma significa
- [ X ] Escopo da v1 (o que a linguagem faz e não faz) explícito no manual

**Link do manual:** https://drive.google.com/drive/folders/1z2Pm4okSkJNKR15IT540rFdklulEDxOD?usp=sharing

## 4. Apresentação/demo final

- [ X ] Roteiro da apresentação definido (motivação → linguagem → compilador → demo ao vivo → limitações)
- [ X ] Demo preparada com pelo menos 1 programa válido e 1 inválido, mostrando o erro reportado

## 5. Scrum

- [ X ] Atualizações assíncronas semanais registradas
- [ X ] Board refletindo o backlog, em andamento e concluído

## 6. Diário de bordo (retrospectiva individual)

| Integrante | O que fiz nesta Sprint | Dificuldades | O que pretendo manter/ajustar |
|---|---|---|---|
| Julia Aparecida Venâncio dos Santos | Participei da organização e do acompanhamento da revisão dos arquivos do projeto e da verificação do funcionamento da IDE, do parser e da visualização da AST. Também acompanhei os testes e a preparação dos materiais para a entrega final. |  montagem do analisador sintático e a criação da visualização da AST foram desafios, pois era a primeira vez que desenvolvia algo desse tipo. No começo, tive dificuldade para compreender como as etapas deveriam funcionar em conjunto e como representar a estrutura do código por meio da árvore. Com o desenvolvimento e os testes, fui entendendo melhor o funcionamento e conseguindo avançar. | Pretendo continuar aprofundando meus conhecimentos sobre compiladores, principalmente sobre análise sintática e árvores sintáticas abstratas. Também quero manter uma boa comunicação com a equipe e a organização das tarefas. Considero importante realizar testes ao longo do desenvolvimento, facilitando a identificação e a correção de problemas. Além disso, acredito que seria interessante implementar a execução dos programas escritos na linguagem, permitindo que o usuário não apenas escreva códigos e receba avisos de erros, mas também consiga executar suas próprias instruções. Nesta versão, nosso foco ficou mais concentrado na interface do compilador e nas etapas de análise e identificação de erros. |
| Matheus Akira Saito de Souza | Criei batida de testes dos analisadores léxicos, sintáticos e semânticos, testei cada erro na IDE para verificar se está bem integrado com o compilador, gerei, analisei e validei manual da linguagem | Criar o analisador semântico e juntar e testar cada mensagem de erro de cada fase do compilador | Pretendo encontrar outras formas mais efetivas de aplicar a nossa linguagem para o público alvo, talvez através de gamificação e outras ideias. Melhorar minha produtividade e atenção. Estudar os próximos passos do compilador para extender a aplicação para o backend, implementando a execução do código e talvez adição de escopos e funções |
| Ronald Alencar do Rosário | Finalizei a IDE, acompanhei testes finais e certifiquei que estava ocorrendo tudo de acordo com os erros definidos e features da v1. | Certificar que o design do IDE estava de acordo com os estudo e recomendações de acessibilidade indicadas pelos artigos reunidos | Pretendo ajustar a função de zoom, e adicionar mais funções como de recomendação de tokens | 
| William Souza | Ajudei na organização final do projeto, finalizei blog de apresentação do projeto. Acompanhei testes realizados tanto na IDE e no compilador | Implementar simulador léxico no blog e fundamentar analise léxica na apresentação | - | 

---

## Rubrica de avaliação — Sprint 4 (nota de 0 a 4,0)

| Critério | Peso | O que caracteriza nota máxima | Nota atribuída | Observações |
|---|---|---|---|---|
| Bateria de testes automatizados | 1,5 | Cobertura completa da v1; testes de erro em todas as camadas | | |
| Refinamento final | 0,5 | Ajustes justificados; casos-limite tratados ou documentados | | |
| Manual da linguagem | 1,0 | Sintaxe, exemplos e mensagens de erro documentados | | |
| Apresentação final / Scrum + diário | 1,0 | Demo funcional; board e diário atualizados | | |
| **Nota final da Sprint 4** | **4,0** | | **___ / 4,0** | |
