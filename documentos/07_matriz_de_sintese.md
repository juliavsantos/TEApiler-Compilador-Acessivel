# Etapa 7 Matriz de síntese e organização da revisão

## Solicitação

Compare os artigos e organize a revisão por temas ou eixos. Não produza apenas uma sequência de resumos.

## Eixos da revisão

1. Requisitos de acessibilidade e estratégias pedagógicas para o ensino de programação a pessoas com TEA
2. Design de sintaxe e redução da complexidade sintática para iniciantes
3. Algoritmos de análise léxica e sintática e sua complexidade

## Matriz de síntese

| Eixo | Artigos relacionados | Convergências | Divergências | Limitações | Lacunas |
|---|---|---|---|---|---|
| 1. Acessibilidade e estratégias pedagógicas para TEA | Zubair et al. (2023); Topaloglou et al. (2026); Elshahawy et al. (2020) | Apoio visual e multimodal e estruturação das tarefas em etapas (scaffolding) aparecem nos três estudos. Zubair e Elshahawy destacam objetivos claros; Zubair e Topaloglou destacam personalização e ritmo individual. | Zubair e Elshahawy derivam recomendações de especialistas (entrevistas e grupos focais); Topaloglou sintetiza intervenções já publicadas. Topaloglou conclui que a ferramenta sozinha não garante acessibilidade e que a integração pedagógica pesa; Zubair e Elshahawy focam no design da ferramenta. Elshahawy associa TEA e deficiência intelectual de forma generalizada, enquanto Zubair e Topaloglou destacam a variação de necessidades entre os estudantes. | Amostras pequenas (4 crianças em Elshahawy; 7 especialistas e 3 na validação em Zubair; Topaloglou aponta amostras pequenas e intervenções curtas nos estudos que revisa). Recomendações de Zubair sem avaliação prática. Elshahawy sem grupo de comparação nem medida de aprendizagem. Predomínio de crianças e adolescentes e de países de alta renda. | Falta de avaliação de longo prazo e de estudos que testem ferramentas construídas a partir das recomendações. Nos artigos analisados, nenhum trata de linguagens textuais nem do processador da linguagem (compilador). |
| 2. Design de sintaxe para iniciantes | Stefik e Siebert (2013); Zubair et al. (2023); Topaloglou et al. (2026) | Todos apontam a simplificação da sintaxe como caminho para reduzir a carga cognitiva: blocos reduzem a necessidade de sintaxe textual (Topaloglou), conjuntos gerenciáveis de elementos de programação (Zubair) e palavras comuns do inglês com menos símbolos conflitantes (Stefik). | Stefik estuda iniciantes em geral, sem TEA, e sintaxe textual; os demais tratam de ferramentas visuais com foco em TEA. No Estudo 4 de Stefik, Ruby e Python tiveram médias maiores que o Quorum, sem diferença significativa, mas os autores recomendam a sintaxe do Quorum. | Amostras pequenas nos experimentos (6 por grupo no Estudo 3; 11 a 13 no Estudo 4), tarefas curtas, população universitária e autores criadores de uma das linguagens comparadas. | Nenhum estudo testou escolhas de sintaxe textual com pessoas com TEA. Nenhum discute o efeito dessas escolhas sobre o custo do parser. |
| 3. Algoritmos de análise léxica e sintática e complexidade | M e Panda (2024); Reddy et al. (2025) | Ambos comparam técnicas descendentes e ascendentes de modo qualitativo e consideram tratamento de erros e restrições da gramática. Ambos mostram o compromisso entre simplicidade e abrangência. | M e Panda descrevem o LL(1) como simples, com tabelas menores, tratamento de erros mais fácil e desempenho melhor que os métodos ascendentes. Reddy classifica LL e LR como restritos a gramáticas simples e descendente recursivo e precedência de operadores como mais flexíveis. M e Panda restringem-se a LL(1), LR(0), SLR e LALR; Reddy inclui outras técnicas e aplicações. | Ambos qualitativos, sem análise assintótica formal e sem medições. M e Panda não declaram limitações e têm uma inconsistência sobre a direção de leitura em LR (pp. 5 e 6). Reddy é uma revisão introdutória e foi publicado em repositório de preprints (confirmar revisão por pares). | Falta comparação assintótica formal de tempo e espaço entre parsers. Nenhum estudo relaciona a escolha do parser a requisitos de acessibilidade, nem avalia mensagens de erro para público com TEA. |
| Relação entre os eixos | Todos os seis estudos | Requisitos de acessibilidade (previsibilidade, feedback imediato, simplicidade) e características de parsers (tratamento de erros, restrições da gramática) tocam temas próximos. Essa aproximação é **interpretação do grupo**, e não afirmação dos artigos. | Não há, porque nenhum artigo trata dos dois eixos juntos. | Poucos estudos por eixo (2 a 3). | Ausência de estudos que liguem acessibilidade ao custo computacional dos processadores de linguagem. Esta é a principal lacuna encontrada. |

## Roteiro da revisão da literatura

### Eixo 1

- Ideia principal: A literatura converge para apoio visual, estruturação de tarefas, personalização e objetivos claros no ensino de programação para pessoas com TEA, mas com evidências frágeis.
- Evidências que serão usadas: as 19 recomendações validadas por especialistas (Zubair et al., 2023); os requisitos de design do jogo CodaRoutine (Elshahawy et al., 2020); as estratégias que deram resultado na revisão de escopo (Topaloglou et al., 2026).
- Comparação entre estudos: origem das evidências (especialistas × intervenções publicadas), foco na ferramenta × foco na integração pedagógica, e tratamento da variação de necessidades.
- Ligação com o problema: responde à parte do problema sobre os requisitos de acessibilidade.

### Eixo 2

- Ideia principal: Simplificar a sintaxe é recomendação comum, mas as evidências sobre sintaxe textual vêm de iniciantes sem TEA.
- Evidências que serão usadas: preferência por palavras comuns e símbolos sem conflito de sentido (Stefik e Siebert, 2013); redução da sintaxe textual em blocos (Topaloglou et al., 2026); conjuntos gerenciáveis de elementos (Zubair et al., 2023).
- Comparação entre estudos: público (iniciantes × TEA), tipo de sintaxe (textual × blocos) e qualidade da evidência (experimento × recomendações de especialistas).
- Ligação com o problema: conecta acessibilidade ao design da linguagem, que é o elo com o processador.

### Eixo 3

- Ideia principal: As técnicas de análise léxica e sintática são comparadas de forma qualitativa, e a literatura lida traz pouca análise assintótica.
- Evidências que serão usadas: comparação entre LL(1), LR(0), SLR e LALR por tabela, tratamento de erros e conflitos (M e Panda, 2024); critérios de comparação e menções a tempo linear ou próximo do linear (Reddy et al., 2025).
- Comparação entre estudos: LL como simples e rápido (M e Panda) × LL e LR como restritos (Reddy); abrangência das técnicas e dos critérios.
- Ligação com o problema: responde à parte do problema sobre a complexidade dos algoritmos e mostra o limite das fontes.

## Síntese crítica provisória

Os estudos sobre TEA convergem em recomendar apoio visual, estruturação em etapas, personalização e simplicidade, e os estudos sobre sintaxe reforçam a redução da complexidade sintática, mas as evidências vêm de amostras pequenas, majoritariamente de crianças, e muitas recomendações ainda não foram avaliadas na prática. Os estudos sobre parsers descrevem LL(1) e LR por critérios qualitativos e divergem quanto a quais técnicas são mais restritas ou flexíveis, sem apresentar análise assintótica formal. A principal lacuna, sustentada pelas seis leituras, é que nenhum estudo relaciona os requisitos de acessibilidade ao custo computacional ou às características dos processadores de linguagem. Qualquer vínculo entre os dois eixos, como o do tratamento de erros com o feedback ao estudante, permanece como hipótese para pesquisas futuras.

## Checklist

- [x] Os artigos foram agrupados por ideias.
- [x] Há comparações entre estudos.
- [x] As divergências foram registradas.
- [x] As lacunas são específicas e sustentadas pelas leituras.
