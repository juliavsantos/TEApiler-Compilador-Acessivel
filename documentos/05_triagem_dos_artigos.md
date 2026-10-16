# Etapa 5 Busca e triagem dos artigos

## Solicitação

Registre as buscas realizadas e justifique a inclusão ou exclusão de cada artigo.

## Registro das buscas

| Base | String usada | Data | Filtros | Resultados encontrados | Responsável |
|---|---|---|---|---:|---|
| SpringerLink | ("visual programming") AND (autism AND accessibility) | 19/09/2026 | Nenhum | 5 | Julia |
| Education. Innovation. Diversity (EID) | ("autism spectrum disorder" OR "ASD") AND ("programming education" OR "visual programming") | 19/09/2026 | Nenhum | 1 | Julia |
| ACM Digital Library | "LLLR" AND "syntax-directed translation” | 21/09/2026 | Nenhum | 1 | Julia |
| Association for Computational Linguistics (ACL)  | ("parsing" OR "parser") AND ("complexity" OR "asymptotic analysis" OR "runtime") AND ("context-free grammar" OR "CFG") | 22/09/2026 | Nenhum | 5 | Julia |
| Association for Computational Linguistics (ACL) | ("context-free parsing" OR "syntactic parsing" OR "parser") AND ("algorithm" OR "parsing algorithm") AND ("complexity" OR "asymptotic analysis" OR "time complexity") | 23/09/2026 | Nenhum | 3 | Julia |
| SBC OpenLib (SOL) | ("autismo" OR "transtorno do espectro autista") AND ("programação OR "coding") AND ("Scratch" OR "programação por blocos") | 21/09/2026 | Nenhum | 1 | Ronald |
| National Center for Biotechnology Information (NCBI) | ("autism" OR "spectrum disorder autism") AND ("programming" OR "coding") AND ("education" OR "learning") | 22/09/2026 | Nenhum | 1 | Ronald |
| National Center for Biotechnology Information (NCBI) | ("autism" OR "spectrum disorder autism") AND ("software" OR "application") AND ("education" OR "learning") | 22/09/2026 | Nenhum | 1 | Ronald |
| IEEE Xplore | “Block-based programming” AND “TEA” | 22/09/2026 | Nenhum | 2 | William |
| SBC OpenLib (SOL)  | "Acessibilidade digital” AND “Transtorno do Espectro Autista” AND (“Interfaces personalizáveis” OR “Sobrecarga sensorial” OR “Design inclusivo") | 24/09/2026 | Nenhum | 1 | William |
| IEEE Xplore e ACM Digital Library | “programming languages” AND “ASD” AND “education” | 23/09/2026 | Nenhum | 4 | Matheus |
| IEEE Xplore, ACM Digital Library e Google Acadêmico | (“compilers” OR “programming languagues”) AND (“asymptotic analysis” OR “algorithm complexity”) AND (“scanner” OR “parser”) | 23/09/2026  | Nenhum | 5 | Matheus |
| IEEE Xplore, ACM Digital Library e Google Acadêmico | ("accessible programming" OR "language design") AND ("autism" OR "neurodiversity") AND ("compiler" OR "complexity") | 24/09/2026 | Nenhum | 3 | Matheus |


## Resumo da triagem

- Total de resultados encontrados: 33
- Duplicatas removidas: 0
- Artigos avaliados por título e resumo: 28
- Artigos selecionados para leitura completa: 13
- Artigos incluídos no conjunto final: 6

## Decisões

| Artigo | Título e resumo | Texto completo | Motivo da exclusão ou inclusão |
|---|---|---|---|
| ZUBAIR, Misbahu S. et al. Designing accessible visual programming tools for children with autism spectrum condition. | Incluir | Aprovar | Escolhemos esse artigo por analisar, propor e validar recomendações para a acessibilidade e engajamento de ferramentas de programação visual, como Scratch e Pocket Code, focando em crianças diagnosticadas com TEA, especialmente aquelas com dificuldade no aprendizado. Deixando claro o que já funciona e o que pode ser melhorado. |
| TOPALOGLOU, Anastasios et al. Programming Education for Students with Autism: A Scoping Review of Pedagogical Strategies and Tools Between 2017–2025. | Incluir | Aprovar | Esse artigo se alinha bastante com que iremos abordar no nosso artigo. Uma análise de artigos e estudos dos últimos anos de como programação foi ensinado e implementado para crianças e adolescentes no espectro autista. |
| SLIVNIK, Boštjan. LLLR parsing. | Incluir | Excluir | Excluimos esse artigo do conjunto final por termos dois artigos que já analisam diversos algoritmos de análise sintática |
| OPEDAL, Andreas et al. Efficient Semiring-Weighted Earley Parsing. | Incluir | Excluir  | Demonstrou otimizações possíveis e detalhes de como implementar eficientemente um algoritmo sintático baseado no clássico algoritmo de Earley. Porém, o algoritmo de Earley é recomendado para linguagens naturais e ambíguas, tanto que artigos anteriores diz que algoritmos como de Earley são menos eficientes em lidar com analisadores sintáticos práticos para linguagens de programação.   |
| KIPPS, James R.; ARPA, Rand-Unix. Analysis of Tomita's algorithm for general context - free parsing. | Incluir | Excluir | Fora do tempo da margem de tempo estabelecido. O artigo apresenta modificações eficientes para algoritmo de Tomita, chegando a complexidade comparável a outros métodos como LR(k). Mas assim como o de Earley, o algoritmo é indicado para processamento de linguagem natural e linguagens ambíguas. O próprio artigo cita que sua implementação poderia prejudicar analisadores sintáticos práticos e que os benefícios de criação de tabelas não balanceariam o custo de overhead.  |
| GKIOLNTA, Eleni; ZYGOPOULOU, Maria; SYRIOPOULOU-DELLI, Christine K. Robot programming for a child with autism spectrum disorder: a pilot study | Incluir | Excluir | Mesmo oferencendo outra perspectiva de ensino de programação para alunos com TEA, escolhermos excluir no momento para utilizarmos em pesquisas futuras. |
| FIORI, Sara; STRONG, Glenn; DUKES, Jonathan. How Are We Teaching Programming to Students with Intellectual Disabilities? A Systematic Review of the Literature. | Incluir | Excluir | O estudo fazendo uma clara distinção entre TEA e deficiência intelectual, mesmo que o estudo admite que muitas vezes ambos as condições são estudadas juntas, e achamos importante apenas entender métodos e estratégias aplicadas a alunos diagnosticados com TEA | 
| SOLA ÖZGÜÇ, Canan; ALTIN, Damla. Teaching Block-Based Coding to a Student with Autism Spectrum Disorder.  | Incluir | Excluir | Este artigo foi excluido por já termos vários exemplos e artigos que apontam os benefícios de programação baseados em blocos no aprendizado de alunos com TEA. |
| MOLLIK, Rubel Hassan; ALJEDAANI, Wajdi; LUDI, Stephanie. Understanding design and accessibility issues in block-based programming for people with disabilities: a literature review. | Incluir | Excluir | Este artigo apresenta pontos de acessibilidade que faltam em programação baseado em blocos para alunos com deficiência. Mesmo sendo interessante, o estudo foca principalmente em deficiências visuais e motoras. Mesmo citando recomendações importantes para deficiências cognitivas, não foi o suficiente para levarmos ao fichamento. |
| M, Asmitha; PANDA, Niharika. Exploring Different Methods of Scanners and Parsers. | Incluir | Aprovar | Escolhemos este estudo por focar em compiladores para linguagens de programação, apresentando diversas técnicas e métodos para a fase léxica e principalmente a sintática. |
| REDDY, Nitin; P, Sai Teja; BELWAL, Meena. A Survey on Top Down and Bottom Up Parsing. | Incluir | Aprovar | Escolhemos este estudo por introduzir e analisar os principais algoritmos das principais metodologias, analisando suas aplicações, complexidade e aplicações. |
| STEFIK, Andreas; SIEBERT, Susanna. An Empirical Investigation into Programming Language Syntax. | Incluir | Aprovar | Mesmo não focando em grupos com TEA ou problemas cognitivos, escolhemos esse estudo por estudar como a sintaxe de diversas linguagens de programação, pode afetar no aprendizado de principiantes e aponta o que pode ser melhorado para facilitar o entendimento de certos conceitos da programação. Utilizamos esse estudo para simplificar nossa linguagem.  |
| ELSHAHAWY, Menna; ABOELNAGA, Khaled; SHARAF, Nada. CodaRoutine: A Serious Game for Introducing Sequential Programming Concepts to Children with Autism. | Incluir | Aprovar | Escolhemos esse artigo por apresentar mais um método de ensinar programação e resolução de problemas, através de um Jogo Educativo / Sério. Que se mostrou muito eficiente para alunos com TEA junto com programação visual (blocos) e programação robótica. |

## Produto da etapa

Conjunto definitivo de artigos e registro das decisões.

## Checklist

- [ X ] Todas as buscas possuem data e string.
- [ X ] As duplicatas foram removidas.
- [ X ] Os critérios foram aplicados igualmente.
- [ X ] Toda exclusão possui justificativa.
- [ X ] Os artigos finais estão diretamente ligados ao problema.
