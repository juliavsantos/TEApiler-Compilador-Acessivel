# Arquivo principal da Interface / IDE da TEA Language (TL)
# Tudo aqui foi feito em Python usando CustomTkinter e Tkinter

import os
import sys
import tkinter as tk
from tkinter import font as tkfont
import customtkinter as ctk

# Aqui a gente adiciona a pasta principal para conseguir importar o lexer e os erros
pasta_atual = os.path.dirname(os.path.abspath(__file__))
pasta_raiz = os.path.dirname(pasta_atual)
if pasta_raiz not in sys.path:
    sys.path.insert(0, pasta_raiz)

# Aqui a gente importa o analisador da TEA Language
try:
    from lexer import tokenizar
    import errors_lexer
    from tokens_dict import TOKENS
except Exception as e:
    tokenizar = None
    errors_lexer = None
    TOKENS = None
    print(f"Aviso ao carregar o lexer: {e}")


# Exemplos prontos da própria documentação da TL para carregar no editor
EXEMPLOS_TL = {
    "1. Olá Mundo": (
        "PROGRAMA\n\n"
        'ESCREVA "Olá mundo!"\n\n'
        "FIM_PROGRAMA"
    ),
    "2. Calcular Média de Notas": (
        "PROGRAMA\n\n"
        "fisica = 9\n"
        "quimica = 6\n"
        "biologia = 10\n\n"
        "total = fisica + quimica + biologia\n"
        "media = total / 3\n\n"
        'ESCREVA "A sua media é: " + media\n\n'
        "SE media MAIOR_OU_IGUAL 7 ENTAO:\n"
        '    ESCREVA "Passou de ano!"\n'
        "SENAO:\n"
        '    ESCREVA "Reprovado..."\n'
        "FIM_SE\n\n"
        "FIM_PROGRAMA"
    ),
    "3. Contagem Regressiva (ENQUANTO)": (
        "PROGRAMA\n\n"
        "ANOTA: Começamos com 5 e vamos diminuindo\n"
        "inicio = 5\n\n"
        'ESCREVA "Começando a contagem:"\n\n'
        "ENQUANTO inicio MAIOR_OU_IGUAL 0 FACA:\n"
        "    ESCREVA inicio\n"
        "    inicio = inicio - 1\n"
        "FIM_ENQUANTO\n\n"
        'ESCREVA "Fim da contagem!"\n\n'
        "FIM_PROGRAMA"
    ),
    "4. Repetição Simples (REPITA)": (
        "PROGRAMA\n\n"
        "soma = 0\n\n"
        "ANOTA: Repete o comando 3 vezes\n"
        "REPITA 3 VEZES:\n"
        "    soma = soma + 10\n"
        "    ESCREVA soma\n"
        "FIM_REPITA\n\n"
        "FIM_PROGRAMA"
    ),
    "5. Testar Sugestão de Erro Amigável": (
        "PROGRAMA\n\n"
        "ANOTA: Esse exemplo usa '==' e '%' de outras linguagens\n"
        "ANOTA: O nosso compilador vai sugerir o jeito certo da TL!\n"
        "numero = 4\n\n"
        "SE numero % 2 == 0 ENTAO:\n"
        '    ESCREVA "O número é par!"\n'
        "FIM_SE\n\n"
        "FIM_PROGRAMA"
    )
}


class IDE_TEALanguage(ctk.CTk):
    """
    Essa classe é a janela principal da nossa IDE.
    Ela controla as telas, as cores calmas e os botões.
    """
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("TEA Language (TL) - Ambiente Acessível")
        self.geometry("1080, 720")
        self.minsize(900, 600)

        # Usamos o modo escuro suave por padrão para não cansar a vista
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Tamanho da letra inicial (o usuário pode aumentar ou diminuir)
        self.tamanho_fonte = 14

        # Aqui guardamos o container principal onde as telas vão aparecer
        self.container = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.container.pack(fill="both", expand=True)

        # Criamos as duas telas: tela de apresentação e tela do editor
        self.tela_apresentacao = TelaApresentacao(parent=self.container, controller=self)
        self.tela_editor = TelaEditor(parent=self.container, controller=self)

        # Começamos mostrando a tela de apresentação
        self.mostrar_apresentacao()

    def mostrar_apresentacao(self):
        # Esconde o editor e mostra a tela inicial
        self.tela_editor.pack_forget()
        self.tela_apresentacao.pack(fill="both", expand=True)

    def mostrar_editor(self, codigo_inicial=None):
        # Esconde a tela inicial e mostra o editor
        self.tela_apresentacao.pack_forget()
        self.tela_editor.pack(fill="both", expand=True)
        if codigo_inicial:
            self.tela_editor.definir_codigo(codigo_inicial)

    def alternar_tema(self):
        # Troca entre o tema escuro suave e o tema claro suave
        atual = ctk.get_appearance_mode()
        novo = "light" if atual == "Dark" else "dark"
        ctk.set_appearance_mode(novo)
        self.tela_editor.atualizar_cores_editor()

    def mudar_tamanho_fonte(self, delta):
        # Aumenta ou diminui a letra para facilitar a leitura
        novo_tamanho = max(11, min(24, self.tamanho_fonte + delta))
        if novo_tamanho != self.tamanho_fonte:
            self.tamanho_fonte = novo_tamanho
            self.tela_editor.atualizar_tamanho_fonte()


class TelaApresentacao(ctk.CTkFrame):
    """
    Essa é a tela inicial de apresentação da TEA Language (TL).
    Ela é bem limpa, sem excesso de botões ou cores fortes.
    """
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0)
        self.controller = controller

        # Área central para organizar as coisas com respiro
        centro = ctk.CTkFrame(self, corner_radius=16, fg_color=("gray90", "#262b33"))
        centro.place(relx=0.5, rely=0.5, anchor="center")

        # Título principal bem visível
        titulo = ctk.CTkLabel(
            centro,
            text="TEA Language (TL)",
            font=ctk.CTkFont(size=34, weight="bold"),
            text_color=("#1f2937", "#93c5fd")
        )
        titulo.pack(padx=40, pady=(40, 10))

        # Frase explicativa simples
        subtitulo = ctk.CTkLabel(
            centro,
            text="Linguagem de programação simples e acessível voltada para pessoas com TEA",
            font=ctk.CTkFont(size=15),
            text_color=("gray40", "#cbd5e1"),
            wraplength=520
        )
        subtitulo.pack(padx=40, pady=(0, 25))

        # Caixinha com os 3 pontos mais legais da linguagem
        card_pontos = ctk.CTkFrame(centro, corner_radius=12, fg_color=("gray85", "#1e232a"))
        card_pontos.pack(padx=40, pady=(0, 30), fill="x")

        pontos = [
            ("✨ Palavras em Português", "Sem símbolos difíceis: use PROGRAMA, SE, REPITA e ESCREVA."),
            ("🤝 Dicas Amigáveis", "Se errar uma palavra, o compilador sugere o jeito certo com calma."),
            ("🎯 Foco no Aprendizado", "Uma instrução por linha para organizar as ideias sem confusão.")
        ]

        for titulo_ponto, desc_ponto in pontos:
            p_box = ctk.CTkFrame(card_pontos, fg_color="transparent")
            p_box.pack(anchor="w", padx=20, pady=10)
            
            lbl_tit = ctk.CTkLabel(
                p_box,
                text=titulo_ponto,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=("#2563eb", "#60a5fa")
            )
            lbl_tit.pack(anchor="w")

            lbl_desc = ctk.CTkLabel(
                p_box,
                text=desc_ponto,
                font=ctk.CTkFont(size=12),
                text_color=("gray30", "#94a3b8")
            )
            lbl_desc.pack(anchor="w")

        # Botões de ação principais
        botoes_box = ctk.CTkFrame(centro, fg_color="transparent")
        botoes_box.pack(padx=40, pady=(0, 35))

        btn_novo = ctk.CTkButton(
            botoes_box,
            text="Criar Novo Código",
            font=ctk.CTkFont(size=15, weight="bold"),
            height=44,
            corner_radius=10,
            fg_color="#3b82f6",
            hover_color="#2563eb",
            command=self.acao_novo_codigo
        )
        btn_novo.pack(side="left", padx=10)

        btn_exemplos = ctk.CTkButton(
            botoes_box,
            text="Ver Exemplos Prontos",
            font=ctk.CTkFont(size=15),
            height=44,
            corner_radius=10,
            fg_color=("gray75", "#334155"),
            hover_color=("gray65", "#475569"),
            text_color=("black", "white"),
            command=self.acao_abrir_exemplos
        )
        btn_exemplos.pack(side="left", padx=10)

    def acao_novo_codigo(self):
        # Abre o editor já com a estrutura básica da linguagem pronta
        estrutura_padrao = (
            "PROGRAMA\n\n"
            "ANOTA: Escreva seus comandos aqui embaixo\n"
            'ESCREVA "Olá, TEA Language!"\n\n'
            "FIM_PROGRAMA\n"
        )
        self.controller.mostrar_editor(estrutura_padrao)

    def acao_abrir_exemplos(self):
        # Abre o editor carregando o primeiro exemplo
        self.controller.mostrar_editor(EXEMPLOS_TL["1. Olá Mundo"])


class TelaEditor(ctk.CTkFrame):
    """
    Essa é a tela principal do editor de código da TL.
    Aqui a pessoa escreve o código, insere blocos rápidos com um clique
    e clica para verificar se o código está certinho.
    """
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0)
        self.controller = controller

        # Criamos o topo com os botões principais
        self.criar_barra_superior()

        # Corpo com a barra de blocos à esquerda e o editor ao centro
        self.corpo = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.corpo.pack(fill="both", expand=True, padx=12, pady=(0, 8))

        # Barra de apoio lateral com blocos de um clique
        self.criar_barra_lateral_blocos()

        # Área central dividida entre editor de código e painel de feedback
        self.area_central = ctk.CTkFrame(self.corpo, corner_radius=10, fg_color="transparent")
        self.area_central.pack(side="left", fill="both", expand=True)

        # Editor de texto com numeração de linhas
        self.criar_area_editor()

        # Painel inferior com as mensagens do compilador
        self.criar_painel_feedback()

        # Configura as cores e a numeração das linhas
        self.atualizar_cores_editor()
        self.atualizar_numeros_linhas()

    def criar_barra_superior(self):
        # Barra no topo para navegação e ferramentas
        topo = ctk.CTkFrame(self, height=54, corner_radius=10, fg_color=("gray90", "#1e232a"))
        topo.pack(fill="x", padx=12, pady=10)

        # Botão para voltar à tela inicial
        btn_voltar = ctk.CTkButton(
            topo,
            text="🏠 Início",
            width=90,
            height=34,
            corner_radius=8,
            fg_color=("gray80", "#334155"),
            hover_color=("gray70", "#475569"),
            text_color=("black", "white"),
            command=self.controller.mostrar_apresentacao
        )
        btn_voltar.pack(side="left", padx=(10, 10), pady=10)

        # Título da tela
        lbl_titulo = ctk.CTkLabel(
            topo,
            text="Editor TEA Language (TL)",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=("#1f2937", "#93c5fd")
        )
        lbl_titulo.pack(side="left", padx=5)

        # Menu para escolher um exemplo pronto
        self.menu_exemplos = ctk.CTkOptionMenu(
            topo,
            values=list(EXEMPLOS_TL.keys()),
            command=self.ao_selecionar_exemplo,
            width=180,
            height=34,
            corner_radius=8,
            fg_color=("gray80", "#334155"),
            button_color=("gray75", "#475569"),
            text_color=("black", "white")
        )
        self.menu_exemplos.set("Exemplos Prontos...")
        self.menu_exemplos.pack(side="left", padx=10)

        # Botão principal: Verificar Código (Chama o Lexer)
        btn_verificar = ctk.CTkButton(
            topo,
            text="🔍 Verificar Código",
            width=140,
            height=34,
            corner_radius=8,
            fg_color="#10b981",
            hover_color="#059669",
            font=ctk.CTkFont(weight="bold"),
            command=self.verificar_codigo
        )
        btn_verificar.pack(side="right", padx=(10, 10))

        # Botão para limpar o código
        btn_limpar = ctk.CTkButton(
            topo,
            text="Limpar",
            width=80,
            height=34,
            corner_radius=8,
            fg_color=("gray80", "#334155"),
            hover_color=("gray70", "#475569"),
            text_color=("black", "white"),
            command=self.limpar_codigo
        )
        btn_limpar.pack(side="right", padx=5)

        # Botões de tamanho da fonte (Acessibilidade)
        btn_zoom_menos = ctk.CTkButton(
            topo,
            text="A-",
            width=38,
            height=34,
            corner_radius=8,
            fg_color=("gray80", "#334155"),
            hover_color=("gray70", "#475569"),
            text_color=("black", "white"),
            command=lambda: self.controller.mudar_tamanho_fonte(-1)
        )
        btn_zoom_menos.pack(side="right", padx=3)

        btn_zoom_mais = ctk.CTkButton(
            topo,
            text="A+",
            width=38,
            height=34,
            corner_radius=8,
            fg_color=("gray80", "#334155"),
            hover_color=("gray70", "#475569"),
            text_color=("black", "white"),
            command=lambda: self.controller.mudar_tamanho_fonte(1)
        )
        btn_zoom_mais.pack(side="right", padx=3)

        # Botão para alternar tema (claro / escuro suave)
        btn_tema = ctk.CTkButton(
            topo,
            text="🌓 Tema",
            width=70,
            height=34,
            corner_radius=8,
            fg_color=("gray80", "#334155"),
            hover_color=("gray70", "#475569"),
            text_color=("black", "white"),
            command=self.controller.alternar_tema
        )
        btn_tema.pack(side="right", padx=5)

    def criar_barra_lateral_blocos(self):
        # Barra na lateral esquerda que ajuda a pessoa a colocar blocos de código com um clique
        barra = ctk.CTkFrame(self.corpo, width=190, corner_radius=10, fg_color=("gray90", "#1e232a"))
        barra.pack(side="left", fill="y", padx=(0, 10))
        barra.pack_propagate(False)

        lbl_apoio = ctk.CTkLabel(
            barra,
            text="Blocos de Apoio",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=("#1f2937", "#93c5fd")
        )
        lbl_apoio.pack(padx=10, pady=(12, 2))

        lbl_dica = ctk.CTkLabel(
            barra,
            text="Clique para inserir:",
            font=ctk.CTkFont(size=11),
            text_color=("gray40", "#94a3b8")
        )
        lbl_dica.pack(padx=10, pady=(0, 10))

        # Lista de blocos práticos da linguagem TL
        blocos = [
            ("PROGRAMA", "PROGRAMA\n\nFIM_PROGRAMA\n"),
            ("ESCREVA", 'ESCREVA "Texto aqui"\n'),
            ("LEIA", "LEIA variavel\n"),
            ("SE ... ENTAO", "SE condicao ENTAO:\n    \nFIM_SE\n"),
            ("SE / SENAO", "SE condicao ENTAO:\n    \nSENAO:\n    \nFIM_SE\n"),
            ("REPITA VEZES", "REPITA 3 VEZES:\n    \nFIM_REPITA\n"),
            ("ENQUANTO FACA", "ENQUANTO condicao FACA:\n    \nFIM_ENQUANTO\n"),
            ("ANOTA (comentário)", "ANOTA: Escreva sua observação aqui\n"),
            ("CONSTANTE", "CONSTANTE valor_fixo = 10\n"),
            ("PARAR", "PARAR\n")
        ]

        # Cria os botões para cada bloco
        for nome, texto_bloco in blocos:
            btn = ctk.CTkButton(
                barra,
                text=nome,
                height=30,
                corner_radius=6,
                font=ctk.CTkFont(size=12),
                fg_color=("gray82", "#2d3748"),
                hover_color=("gray72", "#4a5568"),
                text_color=("black", "#e2e8f0"),
                command=lambda t=texto_bloco: self.inserir_bloco(t)
            )
            btn.pack(fill="x", padx=10, pady=3)

    def criar_area_editor(self):
        # Caixa onde fica o editor de texto com números de linha
        self.frame_editor = ctk.CTkFrame(self.area_central, corner_radius=10, fg_color=("white", "#181b20"))
        self.frame_editor.pack(fill="both", expand=True)

        # Barra de rolagem compartilhada
        scrollbar = tk.Scrollbar(self.frame_editor, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # Coluna da esquerda com os números das linhas
        self.texto_linhas = tk.Text(
            self.frame_editor,
            width=4,
            padx=4,
            pady=8,
            takefocus=0,
            border=0,
            highlightthickness=0,
            state="disabled",
            cursor="arrow"
        )
        self.texto_linhas.pack(side="left", fill="y")

        # Campo de texto principal onde a pessoa digita
        self.campo_codigo = tk.Text(
            self.frame_editor,
            wrap="none",
            padx=10,
            pady=8,
            border=0,
            highlightthickness=0,
            undo=True,
            yscrollcommand=self.rolar_sincronizado
        )
        self.campo_codigo.pack(side="left", fill="both", expand=True)

        # Conecta a barra de rolagem com os dois textos
        scrollbar.config(command=self.ao_rolar_barra)

        # Eventos para atualizar cores e linhas quando a pessoa digita ou rola
        self.campo_codigo.bind("<KeyRelease>", self.ao_digitar)
        self.campo_codigo.bind("<MouseWheel>", lambda e: self.atualizar_numeros_linhas())
        self.campo_codigo.bind("<Button-4>", lambda e: self.atualizar_numeros_linhas())
        self.campo_codigo.bind("<Button-5>", lambda e: self.atualizar_numeros_linhas())

    def criar_painel_feedback(self):
        # Painel inferior que mostra mensagens amigáveis e acolhedoras
        self.painel_feedback = ctk.CTkFrame(
            self.area_central,
            height=160,
            corner_radius=10,
            fg_color=("gray90", "#1e232a")
        )
        self.painel_feedback.pack(fill="x", pady=(8, 0))
        self.painel_feedback.pack_propagate(False)

        # Cabeçalho do feedback
        cabecalho = ctk.CTkFrame(self.painel_feedback, fg_color="transparent")
        cabecalho.pack(fill="x", padx=12, pady=(8, 4))

        self.lbl_status_feedback = ctk.CTkLabel(
            cabecalho,
            text="Pronto para verificar seu código na TEA Language",
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=("gray30", "#93c5fd")
        )
        self.lbl_status_feedback.pack(side="left")

        # Caixa com o texto da mensagem do ajudante
        self.caixa_feedback = ctk.CTkTextbox(
            self.painel_feedback,
            font=ctk.CTkFont(size=13),
            corner_radius=8,
            fg_color=("gray85", "#262b33")
        )
        self.caixa_feedback.pack(fill="both", expand=True, padx=10, pady=(0, 8))
        self.caixa_feedback.insert(
            "end",
            "Dica: Digite seu código acima e clique em 'Verificar Código'.\n"
            "Se tiver qualquer dúvida de escrita, nós te ajudamos com calma!"
        )
        self.caixa_feedback.configure(state="disabled")

    def rolar_sincronizado(self, *args):
        # Rola o campo de código e a coluna de linhas juntos
        self.texto_linhas.yview_moveto(args[0])
        self.atualizar_numeros_linhas()

    def ao_rolar_barra(self, *args):
        # Quando mexe na barra de rolagem, move os dois
        self.campo_codigo.yview(*args)
        self.texto_linhas.yview(*args)
        self.atualizar_numeros_linhas()

    def atualizar_numeros_linhas(self):
        # Calcula e desenha os números das linhas ao lado do código
        self.texto_linhas.configure(state="normal")
        self.texto_linhas.delete("1.0", "end")

        linhas = self.campo_codigo.get("1.0", "end-1c").split("\n")
        total = len(linhas)
        numeros = "\n".join(str(i) for i in range(1, total + 1))
        self.texto_linhas.insert("1.0", numeros)
        self.texto_linhas.configure(state="disabled")

    def ao_digitar(self, event=None):
        # Atualiza a numeração e faz o destaque suave das palavras da linguagem
        self.atualizar_numeros_linhas()
        self.colorir_sintaxe()

    def colorir_sintaxe(self):
        # Pinta suavemente as palavras reservadas, textos e comentários
        codigo = self.campo_codigo.get("1.0", "end-1c")

        # Limpa as cores antigas
        for tag in ["palavra_chave", "operador_texto", "texto", "numero", "comentario"]:
            self.campo_codigo.tag_remove(tag, "1.0", "end")

        # Palavras reservadas principais da TL
        palavras_chave = [
            "PROGRAMA", "FIM_PROGRAMA", "SE", "ENTAO", "SENAO", "FIM_SE",
            "ENQUANTO", "FACA", "FIM_ENQUANTO", "REPITA", "VEZES", "FIM_REPITA",
            "PARAR", "CONSTANTE", "ESCREVA", "LEIA"
        ]

        # Operadores por extenso da TL
        operadores_texto = [
            "IGUAL_A", "DIFERENTE_DE", "MAIOR_QUE", "MENOR_QUE",
            "MAIOR_OU_IGUAL", "MENOR_OU_IGUAL", "E", "OU", "NAO", "RESTO_DE",
            "VERDADE", "FALSO"
        ]

        import re

        # Colorir palavras-chave
        for kw in palavras_chave:
            padrao = rf"\b{kw}\b"
            for m in re.finditer(padrao, codigo):
                inicio = f"1.0 + {m.start()} chars"
                fim = f"1.0 + {m.end()} chars"
                self.campo_codigo.tag_add("palavra_chave", inicio, fim)

        # Colorir operadores por extenso
        for op in operadores_texto:
            padrao = rf"\b{op}\b"
            for m in re.finditer(padrao, codigo):
                inicio = f"1.0 + {m.start()} chars"
                fim = f"1.0 + {m.end()} chars"
                self.campo_codigo.tag_add("operador_texto", inicio, fim)

        # Colorir textos entre aspas
        for m in re.finditer(r'"[^"\r\n]*"', codigo):
            inicio = f"1.0 + {m.start()} chars"
            fim = f"1.0 + {m.end()} chars"
            self.campo_codigo.tag_add("texto", inicio, fim)

        # Colorir números
        for m in re.finditer(r"\b[0-9]+(?:\.[0-9]+)?\b", codigo):
            inicio = f"1.0 + {m.start()} chars"
            fim = f"1.0 + {m.end()} chars"
            self.campo_codigo.tag_add("numero", inicio, fim)

        # Colorir comentários (iniciando com ANOTA)
        for m in re.finditer(r"\bANOTA\b[^\r\n]*", codigo):
            inicio = f"1.0 + {m.start()} chars"
            fim = f"1.0 + {m.end()} chars"
            self.campo_codigo.tag_add("comentario", inicio, fim)

    def atualizar_cores_editor(self):
        # Ajusta as cores suaves para cada tema (sem sobrecarga sensorial)
        modo = ctk.get_appearance_mode()
        fonte_base = ("Courier New", self.controller.tamanho_fonte)

        if modo == "Dark":
            fundo_editor = "#181b20"
            texto_editor = "#e2e8f0"
            fundo_linhas = "#13161a"
            texto_linhas = "#64748b"
            cor_cursor = "#60a5fa"

            # Cores suaves da sintaxe
            cor_kw = "#60a5fa"        # Azul calmo
            cor_op = "#a78bfa"        # Lavanda suave
            cor_texto = "#34d399"     # Verde suave
            cor_num = "#f59e0b"       # Âmbar suave
            cor_comentario = "#94a3b8" # Cinza claro
        else:
            fundo_editor = "#ffffff"
            texto_editor = "#1e293b"
            fundo_linhas = "#f1f5f9"
            texto_linhas = "#94a3b8"
            cor_cursor = "#2563eb"

            cor_kw = "#2563eb"
            cor_op = "#7c3aed"
            cor_texto = "#059669"
            cor_num = "#d97706"
            cor_comentario = "#64748b"

        # Aplica no campo de código
        self.campo_codigo.configure(
            bg=fundo_editor,
            fg=texto_editor,
            insertbackground=cor_cursor,
            font=fonte_base
        )

        # Aplica na coluna de números
        self.texto_linhas.configure(
            bg=fundo_linhas,
            fg=texto_linhas,
            font=fonte_base
        )

        # Configura as tags de cor do texto
        self.campo_codigo.tag_configure("palavra_chave", foreground=cor_kw, font=(fonte_base[0], fonte_base[1], "bold"))
        self.campo_codigo.tag_configure("operador_texto", foreground=cor_op, font=(fonte_base[0], fonte_base[1], "bold"))
        self.campo_codigo.tag_configure("texto", foreground=cor_texto)
        self.campo_codigo.tag_configure("numero", foreground=cor_num)
        self.campo_codigo.tag_configure("comentario", foreground=cor_comentario, font=(fonte_base[0], fonte_base[1], "italic"))

        self.colorir_sintaxe()

    def atualizar_tamanho_fonte(self):
        # Atualiza a fonte após o usuário clicar em A+ ou A-
        self.atualizar_cores_editor()

    def definir_codigo(self, codigo):
        # Coloca um novo código no editor
        self.campo_codigo.delete("1.0", "end")
        self.campo_codigo.insert("1.0", codigo)
        self.ao_digitar()

    def limpar_codigo(self):
        # Limpa o editor
        self.campo_codigo.delete("1.0", "end")
        self.ao_digitar()
        self.mostrar_feedback(
            "Editor limpo. Comece a escrever seu novo código na TEA Language!",
            tipo="normal"
        )

    def inserir_bloco(self, texto):
        # Insere o bloco escolhido na posição onde o cursor estiver
        self.campo_codigo.insert("insert", texto)
        self.campo_codigo.focus_set()
        self.ao_digitar()

    def ao_selecionar_exemplo(self, nome_exemplo):
        # Quando o usuário escolhe um exemplo pronto da lista
        if nome_exemplo in EXEMPLOS_TL:
            self.definir_codigo(EXEMPLOS_TL[nome_exemplo])
            self.mostrar_feedback(
                f"Exemplo carregado: '{nome_exemplo}'.\nClique em 'Verificar Código' para testar!",
                tipo="normal"
            )

    def mostrar_feedback(self, texto, tipo="normal"):
        # Mostra o texto no painel inferior de forma acolhedora
        self.caixa_feedback.configure(state="normal")
        self.caixa_feedback.delete("1.0", "end")
        self.caixa_feedback.insert("end", texto)
        self.caixa_feedback.configure(state="disabled")

        if tipo == "sucesso":
            self.lbl_status_feedback.configure(
                text="✅ Tudo certo com o seu código!",
                text_color=("#059669", "#34d399")
            )
        elif tipo == "atencao":
            self.lbl_status_feedback.configure(
                text="💡 Dica do Ajudante TL:",
                text_color=("#d97706", "#fbbf24")
            )
        else:
            self.lbl_status_feedback.configure(
                text="Status do Código TL",
                text_color=("gray30", "#93c5fd")
            )

    def verificar_codigo(self):
        # Pega o código digitado e passa pelo analisador léxico da TL
        codigo = self.campo_codigo.get("1.0", "end-1c").strip()

        if not codigo:
            self.mostrar_feedback("O editor está vazio. Digite algo ou use um exemplo pronto!", tipo="normal")
            return

        if tokenizar is None:
            self.mostrar_feedback("Não foi possível carregar o arquivo lexer.py.", tipo="atencao")
            return

        try:
            tokens = tokenizar(codigo)
        except Exception as e:
            self.mostrar_feedback(f"Aconteceu algo inesperado ao ler o código: {e}", tipo="atencao")
            return

        # Procura se existe algum erro léxico nos tokens encontrados
        erros_encontrados = []
        tokens_validos = []

        for t in tokens:
            if t.token in TOKENS.get("ERROS_LEXICOS", {}):
                mensagem = errors_lexer.formatar_mensagem(t)
                erros_encontrados.append(f"• Linha {t.linha}: {mensagem}")
            else:
                if t.token != "EOF":
                    tokens_validos.append(t)

        # Se encontrou erro, mostra as dicas amigáveis que o grupo definiu
        if erros_encontrados:
            msg = (
                "Encontramos algumas coisinhas para você ajustar:\n\n" +
                "\n\n".join(erros_encontrados) +
                "\n\n👉 Dica: Você pode corrigir a palavra no texto e clicar em 'Verificar Código' novamente!"
            )
            self.mostrar_feedback(msg, tipo="atencao")
        else:
            # Se não teve erro, parabeniza e lista os tokens de forma clara
            resumo_tokens = [f"'{t.lexema}' ({t.categoria})" for t in tokens_validos[:12]]
            mais = f"... e mais {len(tokens_validos) - 12} tokens." if len(tokens_validos) > 12 else ""
            msg = (
                "Parabéns! O seu código foi analisado e está certinho, sem nenhum erro de escrita!\n\n"
                f"Palavras identificadas: {', '.join(resumo_tokens)} {mais}"
            )
            self.mostrar_feedback(msg, tipo="sucesso")


# Ponto de partida do aplicativo
if __name__ == "__main__":
    app = IDE_TEALanguage()
    app.mainloop()
