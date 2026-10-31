# Tecnologias Usadas na Interface da TEA Language (TL)

Neste arquivo listamos, de forma bem simples e direta, tudo o que foi usado para criar a interface da nossa IDE:

---

### 1. Python 3
* **O que é:** A linguagem de programação principal do projeto.
* **Para que serviu:** Todo o código da interface, o analisador do código (lexer) e as mensagens de erro foram feitos em Python.

---

### 2. CustomTkinter
* **O que é:** Uma biblioteca para Python que cria janelas e botões modernos.
* **Para que serviu:** Usamos para construir toda a parte visual da IDE: as janelas, botões arredondados, caixas de texto e a paleta de cores suaves (com baixo estímulo visual para pessoas com TEA).

---

### 3. Tkinter (Nativo do Python)
* **O que é:** O sistema básico de janelas que já vem com o Python.
* **Para que serviu:** Ajudou na parte de texto do editor (onde o aluno digita o código), na numeração das linhas e na pintura suave das palavras coloridas (destaque de sintaxe).

---

### 4. Módulo `re` (Expressões Regulares)
* **O que é:** Uma ferramenta do próprio Python que sabe procurar e reconhecer padrões de palavras e símbolos.
* **Para que serviu:** Usada pelo compilador para ler o código digitado e identificar o que é comando, o que é número, o que é texto e o que é erro.

---

### 5. Módulo `os` e `sys`
* **O que é:** Ferramentas do próprio Python para mexer em pastas e caminhos do computador.
* **Para que serviu:** Garante que a interface consiga encontrar os outros arquivos do projeto (como o `lexer.py` e o `errors_lexer.py`) sem dar erro de pasta.
