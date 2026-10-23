# Etapa 8 Redação do artigo

## Solicitação

Escreva a primeira versão completa do artigo seguindo a estrutura abaixo.

---

# Mini artigo do grupo (texto original, sem alterações)

**Acessibilidade e Diagnósticos de Erro no aprendizado de programação para pessoas com Transtorno do Espectro Autista: uma revisão bibliográfica narrativa**

Andréa Ono Sakai, Doutorado em Engenharia Biomédica[^0]

Julia Aparecida Venâncio dos Santos[^1]

Matheus Akira Saito de Souza[^2]

Ronald Lopes Alencar do Rosario[^3]

William Souza da Silva[^4]

**RESUMO**

O ensino de programação e o desenvolvimento do pensamento computacional são fundamentais para promover a autonomia de estudantes com Transtorno do Espectro Autista (TEA) (SOLA-ÖZGÜÇ; ALTIN, 2022). Estudantes diagnosticados com esse espectro podem ser beneficiados por meio da tecnologia, por oferecer um ambiente controlado, com respostas imediatas e sem surpresas (ELSHAHAWY et al., 2020). Embora ambientes visuais em blocos mitiguem a complexidade sintática inicial (TOPALOGLOU et al., 2026; ZUBAIR et al., 2023), a transição para linguagens textuais impõe severas barreiras cognitivas, causadas pela opacidade sintática e por mensagens de erro excessivamente abstratas em compiladores tradicionais (HOOBERGS; SCHRIJVERS, 2025). Essa limitação gera frustração e sobrecarga sensorial, evidenciando uma lacuna teórica na articulação entre a teoria de compiladores e a neurodiversidade. Assim, justifica-se a integração de estratégias pedagógicas estruturadas, como *scaffolding* e suporte multimodal, a recursos de compilação previsíveis, a exemplo da análise determinística LL(1) (REDDY et al., 2025) e do paradigma de *Explicit Source Prose* (ESP) (HOOBERGS; SCHRIJVERS, 2025). Diante desse cenário, este artigo tem como objetivo sintetizar as estratégias pedagógicas, os requisitos de design sintático e as abordagens de compilação aplicadas ao ensino inclusivo de programação para alunos com TEA, fundamentando o desenvolvimento de ambientes previsíveis e acessíveis (TOPALOGLOU et al., 2026). A pesquisa adotou uma revisão bibliográfica narrativa, com buscas realizadas nas bases SpringerLink, Education Innovation Diversity, ACM Digital Library, Association for Computational Linguistics, SBC OpenLib, IEEE Xplore e Google Acadêmico. Os critérios de inclusão contemplaram os artigos a partir de 2020, em português e inglês, com texto completo e alinhados à temática do estudo. O estudo delineia-se por meio de uma revisão bibliográfica narrativa destinada a identificar as estratégias pedagógicas vigentes, analisar diretrizes de design sintático acessível e avaliar o papel dos algoritmos de análise léxica e sintática na criação de ambientes educacionais adaptados ao público com TEA. O ensino de programação para alunos com TEA demanda intervenções pedagógicas estruturadas e inclusivas (TOPALOGLOU et al., 2026; ZUBAIR et al., 2023). Nesse sentido, destaca-se a instrução explícita, como estruturada em modelagem, prática guiada e execução independente, associada ao *scaffolding* e à decomposição de tarefas em etapas sequenciais e previsíveis, o que atenua a sobrecarga cognitiva. Os autores ressaltam ainda a eficácia de suportes visuais e abordagens multimodais (como ícones e símbolos) alinhados ao processamento visual desse público, complementados pela flexibilização do ritmo de aprendizagem e pela incorporação de interesses pessoais para sustentar o engajamento e a autonomia. Para favorecer a compreensão e a escrita de código por estudantes com TEA, o design sintático deve focar na redução da complexidade e da abstração (TOPALOGLOU et al., 2026; ZUBAIR et al., 2023). Nesse sentido, o emprego de ambientes visuais em blocos aliado ao uso de sintaxes explícitas, que aproximam as instruções da linguagem natural e eliminam regras implícitas, mitiga a sobrecarga cognitiva e confere previsibilidade aos diagnósticos de erro (HOOBERGS; SCHRIJVERS, 2025; SOLA-ÖZGÜÇ; ALTIN, 2022). Complementarmente, a literatura recomenda substituir blocos densos de texto por ícones e representações gráficas de alto nível, além de restringir as instruções a subconjuntos sintáticos gerenciáveis, garantindo padrões estáveis que facilitam a apreensão semântica e fortalecem a autonomia do aprendiz (TOPALOGLOU et al., 2026; ZUBAIR et al., 2023). A análise léxica e sintática desempenha um papel fundamental na construção de ambientes inclusivos de programação para alunos com TEA. Na fase de compilação, a escolha de algoritmos de *parsing* determinísticos de complexidade temporal previsível e linear (DIEKMANN; TRATT, 2020; SAKAMOTO et al., 2020) assegura que a verificação gramatical ocorra com desempenho estável e resposta imediata, evitando latências que comprometam a atenção do aprendiz. A estruturação sintática por meio do ESP, que traduz o código em linguagem natural a partir da árvore de sintaxe abstrata (AST), elimina ambiguidades e regras implícitas, reduzindo a sobrecarga cognitiva do estudante (Hoobergs & Schrijvers, 2025). Assim, parsers e analisadores projetados para emitir diagnósticos claros fornecem feedbacks previsíveis, fortalecendo a autonomia de estudantes neurodivergentes (Topaloglou et al., 2026; Zubair et al., 2023). A tecnologia atua apenas como facilitadora no ensino de programação para estudantes com TEA, dependendo de estratégias pedagógicas estruturadas, como instrução explícita, *scaffolding*, suportes multimodais e ritmo individualizado, para mitigar sobrecargas cognitivas e sensoriais. Na transição para códigos textuais, barreiras de abstração são superadas pelo paradigma de ESP e pela limitação a subconjuntos sintáticos gerenciáveis, que eliminam ambiguidades e preservam as funções executivas. Por fim, o uso de gramáticas e algoritmos de *parsing* determinísticos e previsíveis assegura diagnósticos de erro imediatos e claros, evitando a frustração decorrente de mensagens obscuras. O estudo cumpre seu objetivo ao integrar estratégias pedagógicas, design sintático e teoria de compiladores no ensino inclusivo de programação para alunos com TEA. Sua principal contribuição é articular o modelo de ESP e a previsibilidade do *parsing* às demandas cognitivas e sensoriais da neurodiversidade, superando a visão meramente instrumental da tecnologia. Aponta como limitações a escassez de estudos longitudinais sobre a transição para linguagens convencionais e sugere, para pesquisas futuras, a automação de analisadores sintáticos acessíveis com suporte a ESP e a capacitação docente em computação inclusiva.

**Palavras-chave:** Complexidade de algoritmos. Ensino de programação. Transtorno do Espectro Autista.

**REFERÊNCIAS**
 
DIEKMANN, L.; TRATT, L. **Don't parse, generate: deterministic parsing and syntax error recovery in interactive programming environments**. *ACM Transactions on Programming Languages and Systems (TOPLAS)*, v. 42, n. 4, art. 17, 2020.
 
ELSHAHAWY, M.; ABOELNAGA, K.; SHARAF, N. **CodaRoutine: a serious game for introducing sequential programming concepts to children with autism.** In: *IEEE GLOBAL ENGINEERING EDUCATION CONFERENCE (EDUCON)*, 2020, Porto. IEEE, 2020. p. 1862–1867. DOI: 10.1109/EDUCON45650.2020.9125196.
 
HOOBERGS, Jesse; SCHRIJVERS, Tom. **Source code without implicitness: explicit source prose for programming education.** In: *UK AND IRELAND COMPUTING EDUCATION RESEARCH CONFERENCE* (UKICER), 2025, Edinburgh. New York: ACM, 2025. 7 p. DOI: 10.1145/3754508.3754510.
 
REDDY, Nitin; P, Sai Teja; BELWAL, Meena. **A survey on top down and bottom up parsing**. *SSRN*, 2025. Trabalho vinculado ao ICOFE-2024. DOI: 10.2139/ssrn.5065432.
 
SAKAMOTO, K.; WASHIZAKI, H.; FUKAZAWA, Y. **An Efficient and Deterministic Disambiguation Approach for Generalized Parsing**. *IEEE Access*, v. 8, p. 147812–147826, 2020.
 
SOLA-ÖZGÜÇ, Canan; ALTIN, Damla. **Teaching block-based coding to a student with autism spectrum disorder**. *Ankara University Faculty of Educational Sciences Journal of Special Education*, Ankara, v. 23, n. 3, p. 565–594, 2022. DOI: 10.21565/ozelegitimdergisi.822554.
 
TOPALOGLOU, Anastasios; TSIOMI, Evaggelia; NANOU, Andromachi; KARAMPATZAKIS, Dimitris. **Programming education for students with autism: a scoping review of pedagogical strategies and tools between 2017–2025**. ***Education. Innovation. Diversity***, [S. l.], v. 1, n. 12, p. 74–98, 2026. DOI: 10.17770/eid2026.1.107..
 
ZUBAIR, Misbahu S.; BROWN, David J.; HUGHES-ROBERTS, Thomas; BATES, Matthew. **Designing accessible visual programming tools for children with autism spectrum condition**. *Universal Access in the Information Society,* [S. l.], v. 22, n. 2, p. 277–296, 2023. DOI: 10.1007/s10209-021-00842-y.
 
[^0]: asakai@brazcubas.edu.br - ID Lattes: 0519974724105439 - Graduação em Engenharia Elétrica - Mestrado e Doutorado em Engenharia Biomédica
[^1]: julia.santos@cs.unicid.edu.br - rgm: 38226189 - ID Lattes: 9220508120698114 - Centro Universitário Braz Cubas - Graduando em Ciência da Computação (6º semestre)
[^2]: matheus.souza03@cs.brazcubas.edu.br - rgm: 38746344 - ID Lattes: 1005808466522164 - Centro Universitário Braz Cubas - Graduando em Ciência da Computação (6º semestre)
[^3]: ronald.rosario@cs.brazcubas.edu.br - rgm: 38899817 - Centro Universitário Braz Cubas - Graduando em Ciência da Computação (6º semestre)
[^4]: william.silva006@cs.brazcubas.edu.br - rgm: 41057619 - Centro Universitário Braz Cubas - Graduando em Ciência da Computação (5° semestre)

---

## Checklist

- [ X ] A introdução termina com o objetivo.
- [ X ] A metodologia descreve o processo realmente realizado.
- [ X ] A revisão compara os artigos.
- [ X ] A conclusão responde ao problema.
- [ X ] O resumo representa o texto completo.

