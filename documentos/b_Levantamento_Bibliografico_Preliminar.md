# Etapa (b) — Levantamento Bibliográfico

> **Como preencher:** este documento deve ser preenchido **em conjunto pelo grupo**, mas com registro individualizado da contribuição de cada integrante em cada passo. Substitua os campos entre `[ ]` pelas informações do seu grupo. Não apague as instruções em itálico — elas ajudam na avaliação do orientador.

---

## 1. Identificação do Grupo

| Campo | Informação |
|---|---|
| Curso / Disciplina | Ciência da Computação |
| Projeto de Pesquisa / IC | Revisão da literatura das linguagens acessíveis voltados ao ensino TEA e sua complexidade |
| Orientador(a) | Andrea Ono Sakai |
| Data de entrega desta etapa | 24/09/2026 |
| Integrantes do grupo | Julia Aparecida Venâncio dos Santos, Matheus Akira Saito de Souza, Ronald Alencar do Rosário, William Souza |
| Tema (da etapa "a") | Desenvolvimento e análise da complexidade de um compilador para uma linguagem de programação acessível, projetada para apoiar o ensino de programação a pessoas com Transtorno do Espectro Autista (TEA) |

---

## FASE 1 — Planejamento da Busca

### Passo 1 — Pergunta de pesquisa e palavras-chave

**1.1 Problema/pergunta de pesquisa (versão de trabalho)**
*Ainda não precisa ser a versão final (isso vem na etapa "c"), mas deve orientar a busca desta fase.*

> Como a literatura aborda linguagens de programação acessíveis para alunos com TEA? E como isso afeta a complexidade da linguagem e compilador?

**1.2 Conceitos-chave e sinônimos**
*Liste os conceitos centrais da pergunta e seus sinônimos, em português e inglês.*

| Conceito-chave | Sinônimos / termos relacionados (PT) | Sinônimos / termos relacionados (EN) |
|---|---|---|
| TEA | Autismo, Neurodivergente | Autism, Neurodivergent, ASD |
| Design de Linguagem | Linguagem de Programação | Programming Languages, Language Design |
| Compiladores | Processadores de Linguagem | Language Processors |
| Análise Léxica | Scanner | Lexical Analysis, scanner |
| Análise Sintática | Parser | Syntatic Analysis, parser |
| Complexidade de Algoritmos | Análise Assintótica | Asymptotic Analysis |
| Educação | Ensino, Didática | Teaching, Didatics |

*Responsável por este passo: Julia, Ronald, Matheus

---

### Passo 2 — Strings de busca

*Combine os termos do passo 1 com operadores booleanos (`AND`, `OR`, `NOT`). Use aspas para termos compostos e truncamento (`*`) quando a base permitir.*

| Nº | String de busca | Base(s) em que será usada | Elaborada por |
|---|---|---|---|
| 1 | ("visual programming") AND (autism AND accessibility) | SpringerLink | Julia |
| 2 | ("autism spectrum disorder" OR "ASD") AND ("programming education" OR "visual programming") | Education. Innovation. Diversity (EID) | Julia |
| 3 | "LLLR" AND "syntax-directed translation” | ACM Digital Library | Julia |
| 4 | ("parsing" OR "parser") AND ("complexity" OR "asymptotic analysis" OR "runtime") AND ("context-free grammar" OR "CFG") | Association for Computational Linguistics (ACL) | Julia |
| 5 | ("context-free parsing" OR "syntactic parsing" OR "parser") AND ("algorithm" OR "parsing algorithm") AND ("complexity" OR "asymptotic analysis" OR "time complexity") | ACL | Julia |
| 6 | ("autismo" OR "transtorno do espectro autista") AND ("programação OR "coding") AND ("Scratch" OR "programação por blocos") | SBC OpenLib (SOL) | Ronald |
| 7 | ("autism" OR "spectrum disorder autism") AND ("programming" OR "coding") AND ("education" OR "learning") | National Center for Biotechnology Information (NCBI) | Ronald |
| 8 | ("autism" OR "spectrum disorder autism") AND ("software" OR "application") AND ("education" OR "learning") | National Center for Biotechnology Information (NCBI) | Ronald |
| 9 | “Block-based programming” AND “TEA” | IEEE Xplore | William |
| 10 | "Acessibilidade digital” AND “Transtorno do Espectro Autista” AND “Interfaces personalizáveis” OR “Sobrecarga sensorial” OR “Design inclusivo" | SBC OpenLib (SOL) | William |
| 11 | “programming languages” AND “ASD” AND “education” | IEEE Xplore e ACM Digital Library | Matheus |
| 12 | ("accessible programming" OR "language design") AND ("autism" OR "neurodiversity") AND ("compiler" OR "complexity") | IEEE Xplore, ACM Digital Library e Google Acadêmico | Matheus |
| 13 | (“compilers” OR “programming languagues”) AND (“asymptotic analysis” OR “algorithm complexity”) AND (“scanner” OR “parser”) | IEEE Xplore, ACM Digital Library e Google Acadêmico | Matheus |

---

### Passo 3 — Bases de dados escolhidas

*Selecione de 2 a 4 bases relevantes ao tema. Registre a justificativa — isso vai para a seção de metodologia do artigo/relatório de IC.*

| Base de dados | Por que foi escolhida | Responsável pela busca nesta base |
|---|---|---|
| SpringerLink | Grande variedade de artigos de qualidade de diversas áreas de pesquisa | Julia |
| Education. Innovation. Diversity (EID) | Banco de dados relevante para área de educação e diversidade que é um dos focos da nossa linguagem | Julia |
| ACM Digital Library | Artigos de relevância de Ciência da Computação, tanto históricos quanto atuais, onde a maioria são de Livre Acesso | Julia, Matheus |
| Association for Computational Linguistics (ACL) | Principal banco de dados sobre o tema de Processamento de Linguagem Natural e Linguagem Baseado em Computador | Julia |
| SBC OpenLib (SOL) | Mais reconhecido entre pesquisadores brasileiros de Computação, fontes confiáveis de livre acesso | Ronald, William |
| National Center for Biotechnology Information (NCBI) | Banco de dados confiável sobre biotecnologia, usado para pesquisar relacionar tecnologia com TEA | Ronald |
| IEEE Xplore | Principal banco de dados de artigos na área de Tecnologia e Ciência da Computação, garantindo artigos de qualidade | Matheus, William |
| Google Acadêmico | Grande diversidade de Artigos, a maioria de livre e fácil acesso. Utilizado como último recurso caso não seja encontrado artigos relevantes ou de livre acesso nos bancos citados acima | Matheus |

---

### Passo 4 — Critérios de inclusão e exclusão

**Critérios de inclusão:**
- Artigos publicados nos últimos 15 anos
- Português/Inglês
- Revisado por Pares

**Critérios de exclusão:**
- Resumos sem texto completo
- Não revisados por pares
- Artigos pagos

*Definidos em conjunto por: Julia, Matheus

---

## FASE 2 — Execução da Busca e Triagem

### Passo 5 — Execução das buscas e registro dos resultados

*Anote quantos resultados cada string trouxe em cada base (útil para o fluxograma tipo PRISMA, se o projeto exigir). Exporte as referências (BibTeX, RIS, CSV) para um gerenciador de referências.*

| Base | String usada (nº) | Data da busca | Nº de resultados | Executada por |
|---|---|---|---|---|
| SpringerLink | 1 | 19/09/2026 | 5 | Julia |
| Education. Innovation. Diversity (EID) | 2 | 19/09/2026 | 1 | Julia |
| ACM Digital Library | 3 | 21/09/2026 | 1 | Julia |
| Association for Computational Linguistics (ACL) | 4 | 22/09/2026 | 5 | Julia |
| Association for Computational Linguistics (ACL) | 5 | 23/09/2026 | 3 | Julia |
| SBC OpenLib (SOL) | 6 | 21/09/2026 | 1 | Ronald |
| National Center for Biotechnology Information (NCBI) | 7 | 22/09/2026 | 1 | Ronald |
| National Center for Biotechnology Information (NCBI) | 8 | 22/09/2026 | 1 | Ronald |
| IEEE Xplore | 9 | 22/09/2026 | 2 | William |
| SBC OpenLib (SOL) | 10 | 24/09/2026 | 1 | William |
| IEEE Xplore e ACM Digital Library | 11 | 23/09/2026 | 4 | Matheus |
| IEEE Xplore, ACM Digital Library e Google Acadêmico | 12 | 24/09/2026 | 3 | Matheus |
| IEEE Xplore, ACM Digital Library e Google Acadêmico | 13 | 23/09/2026 | 5 | Matheus |

**Total de resultados brutos (soma de todas as buscas):** `[ 33 ]`

**Gerenciador de referências utilizado:** Zotero
**Formato de exportação:** BibteX`

---

### Passo 6 — Triagem por título e resumo (1ª filtragem)

*Leia apenas título e resumo de cada resultado. Classifique: incluir / excluir / dúvida. Remova duplicatas entre bases.*

| Item de controle | Quantidade |
|---|---|
| Total de resultados antes da triagem | 33 |
| Duplicatas removidas | 0 |
| Classificados como "Incluir" | 28 |
| Classificados como "Excluir" | 5 |
| Classificados como "Dúvida" | 0 | 

*A triagem detalhada, artigo por artigo, deve ser registrada na planilha de controle do projeto (aba "Triagem de Artigos"). Aqui, registre apenas o resumo quantitativo.*

**Como as dúvidas foram resolvidas?** *(ex.: discussão em grupo, consulta ao orientador)*
 Discussão em Grupo
  
*Responsável(is) por esta triagem: Julia, Ronald, Matheus, William

---

### Passo 7 — Triagem por leitura completa (2ª filtragem)

*Para os artigos que passaram na primeira filtragem, leia introdução e conclusão. Aplique os critérios de inclusão/exclusão (passo 4) de forma mais rigorosa.*

| Item de controle | Quantidade |
|---|---|
| Total de artigos que entraram nesta filtragem | 28 |
| Aprovados (conjunto definitivo para fichamento) | 13 |
| Excluídos nesta etapa | 15 |

**Principais motivos de exclusão nesta filtragem:**
- Fora do escopo
- Artigos com temas e pesquisas muito parecidas

*Responsável(is) por esta triagem: Julia, Ronald, Matheus, William

---

## 3. Lista Final de Artigos Selecionados (Conjunto Definitivo)

*Liste aqui os artigos que passaram por todas as filtragens e seguirão para o fichamento (etapa "j"). Referência completa no formato ABNT/APA definido pelo projeto.*

1. ZUBAIR, Misbahu S. et al. Designing accessible visual programming tools for children with autism spectrum condition. Universal Access in the Information Society, v. 22, n. 2, p. 277–296, jun. 2023. 
2. TOPALOGLOU, Anastasios et al. Programming Education for Students with Autism: A Scoping Review of Pedagogical Strategies and Tools Between 2017–2025. Education. Innovation. Diversity, v. 1, n. 12, p. 74–98, 17 jul. 2026. 
3. SLIVNIK, Boštjan. LLLR parsing. In: SAC ’13: SAC ’13. Proceedings of the 28th Annual ACM Symposium on Applied Computing. Coimbra Portugal: ACM, 18 mar. 2013. Disponível em: <https://dl.acm.org/doi/10.1145/2480362.2480682>. Acesso em: 25 set. 2026
4. OPEDAL, Andreas et al. Efficient Semiring-Weighted Earley Parsing. arXiv, , 2023. Disponível em: <https://arxiv.org/abs/2307.02982>. Acesso em: 25 set. 2026
5. KIPPS, James R.; ARPA, Rand-Unix. Analysis of Tomita's algorithm for general context - free parsing. [S.d.]. 
6. GKIOLNTA, Eleni; ZYGOPOULOU, Maria; SYRIOPOULOU-DELLI, Christine K. Robot programming for a child with autism spectrum disorder: a pilot study. International Journal of Developmental Disabilities, v. 69, n. 3, p. 424–431, 4 maio 2023. 
7. FIORI, Sara; STRONG, Glenn; DUKES, Jonathan. How Are We Teaching Programming to Students with Intellectual Disabilities? A Systematic Review of the Literature. In: KOLI CALLING ’25: 25TH KOLI CALLING INTERNATIONAL CONFERENCE ON COMPUTING EDUCATION RESEARCH. Proceedings of the 25th Koli Calling International Conference on Computing Education Research. Koli Finland: ACM, 11 nov. 2025. Disponível em: <https://dl.acm.org/doi/10.1145/3769994.3770013>. Acesso em: 25 set. 2026
8. SOLA ÖZGÜÇ, Canan; ALTIN, Damla. Teaching Block-Based Coding to a Student with Autism Spectrum Disorder. Ankara Üniversitesi Eğitim Bilimleri Fakültesi Özel Eğitim Dergisi, v. 23, n. 3, p. 565–594, 1 set. 2022. 
9. MOLLIK, Rubel Hassan; ALJEDAANI, Wajdi; LUDI, Stephanie. Understanding design and accessibility issues in block-based programming for people with disabilities: a literature review. Universal Access in the Information Society, v. 25, n. 3, p. 94, ago. 2026. 
10. M, Asmitha; PANDA, Niharika. Exploring Different Methods of Scanners and Parsers. In: 2024 INTERNATIONAL CONFERENCE ON ADVANCES IN MODERN AGE TECHNOLOGIES FOR HEALTH AND ENGINEERING SCIENCE (AMATHE). 2024 International Conference on Advances in Modern Age Technologies for Health and Engineering Science (AMATHE). Shivamogga, India: IEEE, 16 maio 2024. Disponível em: <https://ieeexplore.ieee.org/document/10582089/>. Acesso em: 25 set. 2026
11. REDDY, Nitin; P, Sai Teja; BELWAL, Meena. A Survey on Top Down and Bottom Up Parsing. SSRN, , 2025. Disponível em: <https://www.ssrn.com/abstract=5065432>. Acesso em: 25 set. 2026
12. STEFIK, Andreas; SIEBERT, Susanna. An Empirical Investigation into Programming Language Syntax. ACM Transactions on Computing Education, v. 13, n. 4, p. 1–40, nov. 2013. 
13. ELSHAHAWY, Menna; ABOELNAGA, Khaled; SHARAF, Nada. CodaRoutine: A Serious Game for Introducing Sequential Programming Concepts to Children with Autism. In: 2020 IEEE GLOBAL ENGINEERING EDUCATION CONFERENCE (EDUCON). 2020 IEEE Global Engineering Education Conference (EDUCON). Porto, Portugal: IEEE, abr. 2020. Disponível em: <https://ieeexplore.ieee.org/document/9125196/>. Acesso em: 25 set. 2026
  
*(Adicione quantas linhas forem necessárias.)*

---

## 4. Contribuição Individual dos Integrantes

> **Importante:** cada integrante deve descrever, com suas próprias palavras, o que efetivamente fez em cada passo desta etapa. Contribuições genéricas como "ajudei em tudo" não serão aceitas. Use verbos de ação e seja específico (ex.: "executei a busca no IEEE Xplore com a string 2 e obtive 84 resultados; fiz a triagem por título/resumo de 40 desses").
### Integrante 1 — Julia Aparecida Venâncio dos Santos
- **Passo(s) em que atuou:** Passos 2, 3, 5 e 6
- **O que fez em cada passo:** *Passo 2:* Participei da definição e organização das strings de busca, principalmente das relacionadas a TEA, acessibilidade, ensino de programação, linguagens de programação, compiladores, análise léxica, análise sintática e complexidade de algoritmos. Também realizei buscas nas bases atribuídas ao grupo. *Passo 3:* Participei da definição das bases de pesquisa utilizadas e da organização das justificativas para a escolha de cada base. *Passo 5:* Executei buscas nas bases atribuídas, registrando as strings utilizadas, as datas das pesquisas e os resultados encontrados. Também organizei e compartilhei com o grupo os artigos considerados relevantes para a pesquisa. *Passo 6:* Participei da triagem dos resultados por título e resumo, analisando a pertinência dos trabalhos em relação ao tema e discutindo com os demais integrantes quais artigos deveriam ser incluídos ou excluídos.
- **Tempo dedicado (aprox.):** 5h
- **Evidência da contribuição**: [Pasta de Evidências no Google Drive (Prints das buscas e triagens)](https://drive.google.com/drive/folders/1co5CgIK6frz5DYu1lTV1LSHuENYdWhly?usp=sharing) 
 1. SANTOS, Felipe Lopes dos; VIEIRA, Geciane Oliveira; SANTOS, Jovenilson Ribeiro dos; SANTOS, Wilker José Caminha dos; CONTE, Thiago Nicolau Magalhães de Souza. INCODE: plataforma de apoio à programação para mentes neurodivergentes. Revista Aracê, São José dos Pinhais, v. 7, n. 4, p. 19434-19450, 2025. DOI: 10.56238/arev7n4-219. Disponível em: https://www.researchgate.net/publication/391044465_INCODE_PLATAFORMA_DE_APOIO_A_PROGRAMACAO_PARA_MENTES_NEURODIVERGENTES. Acesso em: 22 ago. 2026.
 2. LOUZADA, Alexandre Neves; SILVA, Mônica Ferreira da; FRANÇA, Tiago Cruz de; ROCHA, Leonardo Pereira. Revisão sistemática de literatura como base para a construção de um catálogo de apoio terapêutico e educacional para pessoas com Transtorno do Espectro Autista (TEA). H2D | Revista de Humanidades Digitais, v. 7, n. 1, e6465, 2025. DOI: 10.21814/h2d.6465. Disponível em:  https://revistas.uminho.pt/index.php/h2d/article/view/6465. Acesso em: 22 ago. 2026.
 3. MORAES, Maria Simone Mônica Costa de. Sistemas e aplicações para autistas: uma revisão sistemática sobre soluções para pessoas atípicas. 2023. 40 f. Trabalho de Conclusão de Curso (Bacharelado em Sistemas de Informação) – Instituto de Computação, Universidade Federal de Alagoas, Maceió, 2023. Disponível em: https://www.repositorio.ufal.br/handle/123456789/12473. Acesso em: 22 ago. 2026.
 4. ASSUNÇÃO, Pedro Henrique Silva; PEREIRA, Pedro Lucas Fernandes; LOPES, Alba Sandyra Bezerra; CÂMARA, Sandra Cristinne Xavier da. Tecnologias digitais na educação para a inclusão de pessoas com Transtorno do Espectro Autista: uma revisão bibliográfica. In: ENCONTRO NACIONAL DE COMPUTAÇÃO DOS INSTITUTOS FEDERAIS (ENCOMPIF), 11., 2024, Brasília, DF. Anais [...]. Porto Alegre: Sociedade Brasileira de Computação, 2024. p. 66-73. DOI: 10.5753/encompif.2024.2511. Disponível em: https://sol.sbc.org.br/index.php/encompif/article/view/29288. Acesso em: 24 ago. 2026.
 5. SILVA, Fernanda Carvalho Caldas da. Aplicativo educacional para autistas baseado em gamificação. 2023. Dissertação (Mestrado Profissional Interdisciplinar em Inovação Tecnológica) – Universidade Federal de São Paulo, São José dos Campos, 2023. Disponível em: https://repositorio.unifesp.br/items/ca0e5910-f516-440b-90d1-6492ad13adb1. Acesso em: 24 ago. 2026.
 6. PAETZOLD, Gustavo Henrique; SCHEMBERGER, Elder Elisandro. EXTLex: um analisador léxico extensível capaz de detectar erros lexicais. Revista Eletrônica Científica Inovação e Tecnologia, Medianeira, v. 5, n. 12, p. 26-36, 2014. DOI: 10.3895/recit.v5.n12.4312. Disponível em: https://periodicos.utfpr.edu.br/recit/article/view/4312. Acesso em:  31 ago. 2026.
 7. GRACIANO JUNIOR, Wagner; GROSSERT, Iara Tavares da Silva; BRANCO NETO, Wilson Castello; AVILA, Alex Junior. Ferramenta interativa para o ensino de compiladores. In: SIMPÓSIO BRASILEIRO DE EDUCAÇÃO EM COMPUTAÇÃO (EDUCOMP), 2., 2022. Anais do II Simpósio Brasileiro de Educação em Computação. Porto Alegre: Sociedade Brasileira de Computação, 2022. DOI: https://doi.org/10.5753/educomp.2022.19217. Disponível em: https://sol.sbc.org.br/index.php/educomp/article/view/19217. Acesso em:  31 ago. 2026.
 8. ZUBAIR, Misbahu S.; BROWN, David J.; HUGHES-ROBERTS, Thomas; BATES, Matthew. Designing accessible visual programming tools for children with autism spectrum condition. *Universal Access in the Information Society*, v. 22, p. 277–296, 2023. DOI: 10.1007/s10209-021-00842-y. Disponível em: https://link.springer.com/article/10.1007/s10209-021-00842-y. Acesso em: 19 set. 2026.
 9. TOPALOGLU, Anastasios; TSIOMI, Evaggelia; NANOU, Andromachi; KARAMPATZAKIS, Dimitris. Programming education for students with autism: a scoping review of pedagogical strategies and tools between 2017–2025. Education. Innovation. Diversity, v. 1, n. 12, p. 74–98, 2026. DOI: 10.17770/eid2026.1.107. Disponível em: https://eid-journals.rtu.lv/eid/article/view/eid2026.1.107. Acesso em: 24 set. 2026.
10. SLIVNIK, Boštjan. LLLR parsing: a combination of LL and LR parsing. In: SYMPOSIUM ON LANGUAGES, APPLICATIONS AND TECHNOLOGIES (SLATE), 5., 2016. Proceedings.... Dagstuhl: Schloss Dagstuhl – Leibniz-Zentrum für Informatik, 2016. p. 5:1–5:13. DOI: 10.4230/OASIcs.SLATE.2016.5. Disponível em: https://drops.dagstuhl.de/entities/document/10.4230/OASIcs.SLATE.2016.5. Acesso em: 21 set. 2026.
11. KIPPS, James R. Analysis of Tomita’s algorithm for general context-free parsing. In: INTERNATIONAL WORKSHOP ON PARSING TECHNOLOGIES, 1., 1989. Proceedings of the First International Workshop on Parsing Technologies. Pittsburgh: Carnegie Mellon University, 1989. p. 193–202. Disponível em: https://aclanthology.org/W89-0220/. Acesso em: 23 set. 2026.
12. OPEDAL, Andreas; ZMIGROD, Ran; VIEIRA, Tim; COTTERELL, Ryan; EISNER, Jason. Efficient semiring-weighted Earley parsing. In: ANNUAL MEETING OF THE ASSOCIATION FOR COMPUTATIONAL LINGUISTICS, 61., 2023. Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). Toronto: Association for Computational Linguistics, 2023. p. 3687–3713. DOI: 10.18653/v1/2023.acl-long.204. Disponível em: https://aclanthology.org/2023.acl-long.204/. Acesso em: 22 set. 2026.

### Integrante 2 — Ronald Lopes Alencar do Rosario
Passo(s) em que atuou: Passos 1, 2, 3, 5 e 7
O que fez em cada passo: Passo 1: participei da definição dos principais conceitos da pesquisa, com foco em compiladores, design de linguagem, IHC e acessibilidade para pessoas com TEA. Passo 2: elaborei uma string de busca relacionada a Design de Linguagem, Análise Léxica e Análise Sintática. Passo 3: realizei pesquisas no Google Acadêmico e na SBC OpenLib (SOL), buscando artigos relacionados ao tema do projeto. Passo 5: executei buscas por trabalhos sobre linguagens de programação simplificadas, compiladores, ensino de programação, mensagens de erro e interfaces acessíveis, selecionando artigos relacionados ao desenvolvimento da proposta. Passo 7: realizei a leitura e o resumo dos artigos selecionados, analisando principalmente como linguagens simplificadas, compiladores, feedback de erros e princípios de IHC podem contribuir para uma linguagem de programação voltada ao ensino de pessoas com TEA.]
Tempo dedicado (aprox.): 5h
Evidência da contribuição: Pesquisas realizadas no Google Acadêmico e SBC OpenLib (SOL), além da leitura e resumo de artigos como PortuCol: uma pseudolinguagem inspirada em C ANSI para o Ensino de Lógica de Programação e Algoritmos; Python Enhanced Error Feedback: Uma IDE Online de Apoio ao Processo de Ensino-Aprendizagem em Programação; e Ferramenta interativa para o ensino de compiladores.

### Integrante 3 — William Souza da Silva
- **Passo(s) em que atuou:** Passos 2, 3, 5, 6 e 7
- **O que fez em cada passo:** 
Passo 2: executei a busca por artigos relacionados á interface e design da linguagem, bem como pesquisas com base na complexidade de criação da linguagem de programação e a acessibilidade do mesmo, além do suporte ao ensino e barreiras. a consulta foram feitas no SBC Openlib SOL, ACM Digital Library, IEEE Xplore e SciElO e Google Academico; 
Passo 3: Busca realizada atráves do google academico e SBC e IEEE Xplorer por datasets conhecidos e estando relacionados ao objetivo do projeto e co-relacionando com as disciplinas, além das discussões á respeito dos artigos encontrado e strings utilizadas para busca.
Passo 5: Enviei todos artigos encontrados e de maior coerência e contexto com as informações necessárias para visualização. 
Passo 6: Foram realizadas exposições dos itens encontrados, assim como o sanar de dúvidas á respeito do abstract/resumo, levando em consideração á estrutura de pesquisa do projeto.
Passo 7: Utilizei de ferramentas para anotação de informações bases encontradas nos artigos publicados dentro dos anos mais recentes, como foi encontrado uma divulgação 2026, realizei a leitura dos abstracts
**Tempo dedicado (aprox.):** 3h25
- **Evidência da contribuição:** https://sol.sbc.org.br/index.php/wie/article/view/26297, https://sol.sbc.org.br/index.php/sbie/article/view/38477/38251, https://dl.acm.org/doi/10.1145/3772318.3791853, https://dl.acm.org/doi/10.1145/3772318.3791853....

### Integrante 4 — Matheus Akira Saito de Souza
- *Passo(s) em que atuou:* Passos 1, 2, 3, 4, 5, 6 e 7
- *O que fez em cada passo:* 
 Passo 1: Defini o problema e os conceitos chaves relacionados a Análise Léxica, Sintática e Complexidade de Algoritmos. 
 Passo 2: Utilizei dos conceitos chaves definidos pare montar strings de busca relacionados a métodos para ensino de programação envolvendo linguagens de programação acessíveis. E algoritmos de análise léxica e sintática.
 Passo 3: Escolhi a base de dados IEEE Xplore e ACM Digital Library por sua credibilidade e artigos de alta qualidade na área de ciência da computação. Google Acadêmico foi escolhido como última opção, caso não encontrasse artigos livres ou relevantes para nossa pesquisa
 Passo 4: Definimos em sala de aula todos os critérios de inclusão e exclusão e preenchi no md.
 Passo 5: Executei as strings 11, 12 e 13 no IEEE Xplore, ACM Digital Library e Google Acadêmico. Essa pesquisa resultou em 12 artigos. Utilizei o programa Zotero para agrupar os artigos encontrados nesse passo e as exportei no formato Bibtex.
 Passo 6: Lemos os resumos dos 33 artigos e esclarecemos as dúvidas em discussão em sala e no grupo do Whatsapp.
 Passo 7: Promovi uma discussão no grupo para resolver as questões de alguns artigos que não foram discutidos. Realizei a leitura e avalição de Introdução e Conclusão de aproximadamente 10 artigos. Relacionei os motivos de exclusão para esse passo.
- *Tempo dedicado (aprox.):* 5h
- *Evidência da contribuição*: Evidência de Buscas: https://drive.google.com/drive/folders/1ShXh3pHOML-yNEssLXeVTk39nXj4h-6n?usp=sharing
 [Artigos Finais Exportados](Artigos_Exportados.bib)

*(Copie o bloco acima para cada integrante adicional do grupo.)*

### 4.1 Quadro-resumo de participação por passo

| Passo | Responsável(is) | % estimado de participação de cada um |
|---|---|---|
| 1. Pergunta e palavras-chave | Julia, Ronald, Matheus, William | Todos: 25% |
| 2. Strings de busca | Julia, Ronald, Matheus, William | Julia: ~38%, Ronald: ~23%, Matheus: ~23%, William: ~15% |
| 3. Bases de dados | Julia, Ronald, Matheus, William | Todos: 25% |
| 4. Critérios de inclusão/exclusão | Julia e Matheus | Julia: 50%, Matheus: 50% |
| 5. Execução das buscas | Julia, Ronald, Matheus, William | Todos: 25% |
| 6. Triagem título/resumo | Julia, Ronald, Matheus, William | Todos: 25% |
| 7. Triagem texto completo | Julia, Ronald, Matheus, William | Todos: 25% |

### 4.2 Quadro-resumo geral de participação na etapa

| Integrante | % estimado de participação total nesta etapa |
|---|---|
| Julia | 25% |
| Ronald | 25% |
| Matheus | 25% |
| William | 25% |

*A soma das porcentagens deve ser igual a 100%. Divergências de percepção sobre a participação devem ser discutidas em grupo antes do envio — o orientador pode solicitar esclarecimentos individuais em caso de disparidade relevante.*

---

## 5. Checklist Final da Etapa

**Fase 1 — Planejamento**
- [ X ] Pergunta de pesquisa de trabalho definida
- [ X ] Conceitos-chave e sinônimos (PT/EN) listados
- [ X ] Strings de busca elaboradas com operadores booleanos
- [ X ] Bases de dados escolhidas e justificadas
- [ X ] Critérios de inclusão e exclusão definidos

**Fase 2 — Execução e triagem**
- [ X ] Buscas executadas e resultados registrados por base/string
- [ X ] Referências exportadas para o gerenciador de referências
- [ X ] Triagem por título/resumo concluída (com duplicatas removidas)
- [ X ] Triagem por texto completo (introdução/conclusão) concluída
- [ X ] Conjunto definitivo de artigos para fichamento compilado

**Documentação**
- [ X ] Contribuição individual de cada integrante registrada por passo
- [ X ] Quadro-resumo de participação preenchido (soma = 100%)

---


