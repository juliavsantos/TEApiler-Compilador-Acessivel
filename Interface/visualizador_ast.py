# Visualizador da AST (árvore sintática) da TEA Language (TL)
#
# Esse arquivo desenha a árvore que o parser montou e mostra, passo a passo,
# os três percursos clássicos: pré-ordem, em-ordem e pós-ordem.
#
# Como usar dentro da IDE:  botão "🌳 Árvore" (ver ide_tl.py)
# Como usar sozinho:        python Interface/visualizador_ast.py [arquivo.txt]

import html
import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkfont
import customtkinter as ctk


# ---------------------------------------------------------------------------
# 1) Medidas do desenho (em "unidades base"; o zoom multiplica tudo isso)
# ---------------------------------------------------------------------------
ALT_NO = 48      # altura de cada caixinha
LARG_MIN = 74    # largura mínima de cada caixinha
H_GAP = 16       # espaço horizontal entre irmãos
V_GAP = 84       # distância vertical entre um nível e o outro
MARGEM = 28      # respiro em volta da árvore


# ---------------------------------------------------------------------------
# 2) Cores suaves (mesma ideia da IDE: sem sobrecarga sensorial)
#    Cada categoria tem: (preenchimento, borda, texto)
# ---------------------------------------------------------------------------
PALETAS = {
    "Dark": {
        "fundo": "#181b20", "painel": "#1e232a", "texto": "#e2e8f0",
        "suave": "#94a3b8", "linha": "#475569",
        "destaque": "#fbbf24", "destaque_texto": "#1e293b",
        "badge": "#e2e8f0", "badge_texto": "#1e293b",
        "comando": ("#1e3a5f", "#60a5fa", "#e2e8f0"),
        "operador": ("#33295c", "#a78bfa", "#e2e8f0"),
        "numero": ("#4a3512", "#f59e0b", "#e2e8f0"),
        "texto_cat": ("#12392f", "#34d399", "#e2e8f0"),
        "variavel": ("#14343b", "#67e8f9", "#e2e8f0"),
    },
    "Light": {
        "fundo": "#ffffff", "painel": "#f1f5f9", "texto": "#1e293b",
        "suave": "#64748b", "linha": "#94a3b8",
        "destaque": "#f59e0b", "destaque_texto": "#1e293b",
        "badge": "#1e293b", "badge_texto": "#ffffff",
        "comando": ("#dbeafe", "#2563eb", "#1e293b"),
        "operador": ("#ede9fe", "#7c3aed", "#1e293b"),
        "numero": ("#fef3c7", "#d97706", "#1e293b"),
        "texto_cat": ("#d1fae5", "#059669", "#1e293b"),
        "variavel": ("#cffafe", "#0891b2", "#1e293b"),
    },
}

# Nome das categorias na legenda: (chave na paleta, nome mostrado)
LEGENDA = [
    ("comando", "comando"),
    ("operador", "operador"),
    ("numero", "número"),
    ("texto_cat", "texto / lógico"),
    ("variavel", "variável"),
]


# ---------------------------------------------------------------------------
# 3) Explicações de cada percurso (aparecem na janela)
# ---------------------------------------------------------------------------
MODOS = {
    "pre": (
        "Pré-ordem  ( nó → esquerda → direita )",
        "Visita o nó primeiro e só depois os filhos, da esquerda para a direita. "
        "É como o índice de um livro: o título vem antes dos subtítulos. "
        "Serve para copiar ou imprimir a estrutura da árvore."
    ),
    "em": (
        "Em-ordem  ( esquerda → nó → direita )",
        "Visita o filho da esquerda, depois o nó e por fim o da direita. "
        "Nas contas e comparações, isso lê a expressão do jeito que a gente escreve, mas repare: "
        "os parênteses somem! Quem guarda a ordem das contas é a forma da árvore. "
        "(Comandos como PROGRAMA, SE e ESCREVA não têm esquerda e direita, "
        "então o nó vem primeiro, como no código.)"
    ),
    "pos": (
        "Pós-ordem  ( esquerda → direita → nó )",
        "Visita os filhos primeiro e o nó por último. É a ordem que o compilador "
        "usa para calcular: precisa dos dois valores antes de fazer a conta. "
        "Exemplo: 2 * (3 + 1) vira  2  3  1  +  *"
    ),
}
NOMES_MODOS = {"Pré-ordem": "pre", "Em-ordem": "em", "Pós-ordem": "pos"}


# ---------------------------------------------------------------------------
# 4) Árvore "visual": transforma o dicionário da AST em nós fáceis de desenhar
# ---------------------------------------------------------------------------
class NoVisual:
    """Um nó da árvore já com texto bonitinho e posição na tela."""

    def __init__(self, tipo, rotulo, legenda, categoria):
        self.tipo = tipo            # tipo original da AST (ex: "OpAritmetica")
        self.rotulo = rotulo        # texto principal (ex: "*")
        self.legenda = legenda      # explicação pequena (ex: "conta")
        self.categoria = categoria  # define a cor
        self.filhos = []            # lista de (nome_da_ligacao, NoVisual)
        self.x = 0.0                # centro horizontal
        self.y = 0.0                # centro vertical
        self.larg = 0.0             # largura da caixinha
        self.larg_sub = 0.0         # largura que a subárvore inteira ocupa
        self.larg_filhos = 0.0      # largura só dos filhos juntos


def descrever_no(d):
    """Devolve (rótulo, legenda, categoria) de um nó da AST."""
    tipo = d["tipo"]
    nome = d.get("nome", "")
    op = d.get("op", "")
    valor = d.get("valor")

    if tipo == "Programa":
        return "PROGRAMA", "início", "comando"
    if tipo == "Atribuir":
        return f"{nome} =", "guardar valor", "comando"
    if tipo == "Constante":
        return f"CONSTANTE {nome}", "valor fixo", "comando"
    if tipo == "Escreva":
        return "ESCREVA", "mostrar na tela", "comando"
    if tipo == "Leia":
        return f"LEIA {nome}", "ler do teclado", "comando"
    if tipo == "Se":
        return "SE", "decisão", "comando"
    if tipo == "Enquanto":
        return "ENQUANTO", "repete enquanto", "comando"
    if tipo == "Repita":
        return "REPITA", "repete N vezes", "comando"
    if tipo == "Parar":
        return "PARAR", "sai da repetição", "comando"
    if tipo == "OpAritmetica":
        return str(op), "conta", "operador"
    if tipo == "OpRelacional":
        return str(op), "comparação", "operador"
    if tipo == "OpLogica":
        return str(op), "lógica", "operador"
    if tipo == "Nao":
        return "NAO", "negação", "operador"
    if tipo == "Negativo":
        return "-", "número negativo", "operador"
    if tipo == "Numero":
        return str(valor), "número", "numero"
    if tipo == "Texto":
        texto = str(valor)
        if len(texto) > 16:
            texto = texto[:15] + "…"
        return f'"{texto}"', "texto", "texto_cat"
    if tipo == "Logico":
        return ("VERDADE" if valor else "FALSO"), "lógico", "texto_cat"
    if tipo == "Variavel":
        return str(nome), "variável", "variavel"
    return tipo, "", "comando"


# Nomes mais amigáveis para as ligações entre os nós
NOMES_LIGACAO = {"condicao": "condição", "entao": "então", "senao": "senão"}


def converter(d):
    """Transforma o dicionário da AST (ast.para_dict()) em NoVisual."""
    rotulo, legenda, categoria = descrever_no(d)
    no = NoVisual(d["tipo"], rotulo, legenda, categoria)

    for chave, valor in d.items():
        if chave == "tipo":
            continue
        nome = NOMES_LIGACAO.get(chave, chave)
        if isinstance(valor, dict):
            no.filhos.append((nome, converter(valor)))
        elif isinstance(valor, list):
            # Em listas (corpo, entao, senao) só a primeira ligação leva o nome
            for i, item in enumerate(valor):
                if isinstance(item, dict):
                    no.filhos.append((nome if i == 0 else "", converter(item)))
    return no


def todos_os_nos(raiz):
    """Lista todos os nós (em pré-ordem), útil para desenhar e contar."""
    lista = [raiz]
    for _, filho in raiz.filhos:
        lista.extend(todos_os_nos(filho))
    return lista


# ---------------------------------------------------------------------------
# 5) Os três percursos
# ---------------------------------------------------------------------------
# Nós que têm "esquerda" e "direita" de verdade
OPERADORES_BINARIOS = ("OpAritmetica", "OpRelacional", "OpLogica")


def percurso(raiz, modo):
    """
    Devolve a lista de nós na ordem em que são visitados.

    pre : nó, depois os filhos
    pos : filhos, depois o nó
    em  : filho da esquerda, nó, filho da direita.
          Isso só faz sentido em nós com "esquerda" e "direita", ou seja, as
          contas, comparações e operações lógicas (OPERADORES_BINARIOS).
          Nos outros nós (PROGRAMA, SE, ESCREVA...) o nó vem primeiro,
          do mesmo jeito que lemos o código.
    """
    ordem = []

    def visitar(no):
        filhos = [f for _, f in no.filhos]
        if modo == "pre":
            ordem.append(no)
            for f in filhos:
                visitar(f)
        elif modo == "pos":
            for f in filhos:
                visitar(f)
            ordem.append(no)
        elif no.tipo in OPERADORES_BINARIOS and len(filhos) == 2:  # em-ordem de verdade
            visitar(filhos[0])
            ordem.append(no)
            visitar(filhos[1])
        else:  # comandos: o nó vem primeiro (igual à pré-ordem)
            ordem.append(no)
            for f in filhos:
                visitar(f)

    visitar(raiz)
    return ordem


# ---------------------------------------------------------------------------
# 6) Posição dos nós na tela
# ---------------------------------------------------------------------------
def posicionar_arvore(raiz, medir_texto_rotulo, medir_texto_legenda):
    """
    Calcula x, y e largura de cada nó (em unidades base).
    Devolve (largura_total, altura_total) do desenho.
    A ideia: cada subárvore reserva a largura que precisa, então nada se sobrepõe.
    """
    def medir(no):
        no.larg = max(
            LARG_MIN,
            max(medir_texto_rotulo(no.rotulo), medir_texto_legenda(no.legenda)) + 24
        )
        for _, f in no.filhos:
            medir(f)
        no.larg_filhos = (
            sum(f.larg_sub for _, f in no.filhos) + H_GAP * max(0, len(no.filhos) - 1)
        )
        no.larg_sub = max(no.larg, no.larg_filhos)

    profundidade = [0]

    def posicionar(no, esquerda, nivel):
        profundidade[0] = max(profundidade[0], nivel)
        no.y = MARGEM + nivel * V_GAP + ALT_NO / 2

        inicio = esquerda + (no.larg_sub - no.larg_filhos) / 2
        for _, f in no.filhos:
            posicionar(f, inicio, nivel + 1)
            inicio += f.larg_sub + H_GAP

        if no.filhos:
            meio = (no.filhos[0][1].x + no.filhos[-1][1].x) / 2
            minimo = esquerda + no.larg / 2
            maximo = esquerda + no.larg_sub - no.larg / 2
            no.x = min(max(meio, minimo), maximo)
        else:
            no.x = esquerda + no.larg_sub / 2

    medir(raiz)
    posicionar(raiz, MARGEM, 0)
    largura = raiz.larg_sub + 2 * MARGEM
    altura = 2 * MARGEM + profundidade[0] * V_GAP + ALT_NO
    return largura, altura


# ---------------------------------------------------------------------------
# 7) Exportar a árvore como imagem SVG (para colocar no blog, slides, etc.)
# ---------------------------------------------------------------------------
def gerar_svg(raiz, largura, altura, ordem=None, legenda_rodape=""):
    p = PALETAS["Light"]
    numeros = {id(n): i + 1 for i, n in enumerate(ordem or [])}
    esc = html.escape
    rodape = 34 if legenda_rodape else 0
    larg_i, alt_i = int(largura), int(altura + rodape)

    s = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{larg_i}" height="{alt_i}" '
        f'viewBox="0 0 {larg_i} {alt_i}" font-family="Arial, Helvetica, sans-serif">',
        f'<rect width="100%" height="100%" fill="{p["fundo"]}"/>',
    ]

    nos = todos_os_nos(raiz)

    # Linhas entre os nós
    for no in nos:
        for nome, f in no.filhos:
            x1, y1 = no.x, no.y + ALT_NO / 2
            x2, y2 = f.x, f.y - ALT_NO / 2
            ym = (y1 + y2) / 2
            s.append(
                f'<polyline points="{x1:.1f},{y1:.1f} {x1:.1f},{ym:.1f} {x2:.1f},{ym:.1f} '
                f'{x2:.1f},{y2:.1f}" fill="none" stroke="{p["linha"]}" stroke-width="1.5"/>'
            )
            if nome:
                ty = (ym + y2) / 2
                lw = len(nome) * 5.2 + 6  # largura aproximada do fundinho
                s.append(
                    f'<rect x="{x2 - lw / 2:.1f}" y="{ty - 6:.1f}" width="{lw:.1f}" '
                    f'height="12" fill="{p["fundo"]}"/>'
                )
                s.append(
                    f'<text x="{x2:.1f}" y="{ty + 3:.1f}" font-size="9" '
                    f'text-anchor="middle" fill="{p["suave"]}">{esc(nome)}</text>'
                )

    # Caixinhas
    for no in nos:
        fundo, borda, cor_texto = p[no.categoria]
        x1, y1 = no.x - no.larg / 2, no.y - ALT_NO / 2
        s.append(
            f'<rect x="{x1:.1f}" y="{y1:.1f}" width="{no.larg:.1f}" height="{ALT_NO}" '
            f'rx="10" fill="{fundo}" stroke="{borda}" stroke-width="2"/>'
        )
        s.append(
            f'<text x="{no.x:.1f}" y="{no.y - 8:.1f}" font-size="9" text-anchor="middle" '
            f'fill="{p["suave"]}">{esc(no.legenda)}</text>'
        )
        s.append(
            f'<text x="{no.x:.1f}" y="{no.y + 10:.1f}" font-size="13" font-weight="bold" '
            f'text-anchor="middle" fill="{cor_texto}">{esc(no.rotulo)}</text>'
        )
        if id(no) in numeros:
            bx, by = no.x + no.larg / 2, no.y - ALT_NO / 2
            s.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="10" fill="{p["badge"]}"/>')
            s.append(
                f'<text x="{bx:.1f}" y="{by + 4:.1f}" font-size="11" font-weight="bold" '
                f'text-anchor="middle" fill="{p["badge_texto"]}">{numeros[id(no)]}</text>'
            )

    if legenda_rodape:
        s.append(
            f'<text x="{MARGEM}" y="{altura + 20:.1f}" font-size="12" fill="{p["suave"]}">'
            f'{esc(legenda_rodape)}</text>'
        )

    s.append("</svg>")
    return "\n".join(s)


# ---------------------------------------------------------------------------
# 8) A janela
# ---------------------------------------------------------------------------
class JanelaArvoreAST(ctk.CTkToplevel):
    """
    Janela que desenha a AST e anima os percursos.

    ast_dict  : resultado de ast.para_dict()
    total_nos : quantidade de nós informada pelo parser (opcional)
    """

    def __init__(self, mestre, ast_dict, total_nos=None, codigo=""):
        super().__init__(mestre)
        self.title("Árvore Sintática (AST) - TEA Language")
        self.geometry("1100x740")
        self.minsize(820, 560)

        # Dados da árvore
        self.raiz = converter(ast_dict)
        self.todos = todos_os_nos(self.raiz)
        self.total_nos = total_nos if total_nos else len(self.todos)
        self.codigo = codigo

        # Estado da animação
        self.modo = "pre"
        self.ordem = percurso(self.raiz, self.modo)
        self.indice = {id(n): i for i, n in enumerate(self.ordem)}
        self.passo = 0            # quantos nós já foram visitados
        self.tocando = False
        self._job_tique = None
        self._job_redesenho = None
        self.escala = 1.0

        # Calcula as posições uma vez só (em unidades base)
        fonte_rot = tkfont.Font(self, family="Arial", size=11, weight="bold")
        fonte_leg = tkfont.Font(self, family="Arial", size=8)
        self.largura, self.altura = posicionar_arvore(
            self.raiz, fonte_rot.measure, fonte_leg.measure
        )

        self._montar_interface()
        self._atualizar_texto_modo()
        self.atualizar()

        # Atalhos de teclado (ótimo para apresentar!)
        self.bind("<Right>", lambda e: self.proximo())
        self.bind("<Left>", lambda e: self.anterior())
        self.bind("<space>", lambda e: self.alternar_reproducao())
        self.bind("<Home>", lambda e: self.reiniciar())
        self.protocol("WM_DELETE_WINDOW", self.fechar)

        # Espera a janela aparecer para ajustar o zoom ao tamanho dela
        self.after(250, self.ajustar_a_janela)
        self.after(150, self.focus)

    # ----- Construção da tela ------------------------------------------------
    def _montar_interface(self):
        cinza = ("gray90", "#1e232a")
        botao = dict(
            height=32, corner_radius=8,
            fg_color=("gray80", "#334155"), hover_color=("gray70", "#475569"),
            text_color=("black", "white"),
        )

        # Topo: título, quantidade de nós e ferramentas
        topo = ctk.CTkFrame(self, corner_radius=10, fg_color=cinza)
        topo.pack(fill="x", padx=12, pady=(10, 6))

        ctk.CTkLabel(
            topo, text="🌳 Árvore Sintática (AST)",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=("#1f2937", "#93c5fd"),
        ).pack(side="left", padx=(14, 10), pady=10)

        ctk.CTkLabel(
            topo, text=f"{self.total_nos} nós",
            font=ctk.CTkFont(size=12), text_color=("gray40", "#94a3b8"),
        ).pack(side="left", padx=4)

        ctk.CTkButton(topo, text="Exportar SVG", width=110, command=self.exportar_svg, **botao
                      ).pack(side="right", padx=(4, 12), pady=8)
        ctk.CTkButton(topo, text="Ajustar", width=70, command=self.ajustar_a_janela, **botao
                      ).pack(side="right", padx=4)
        ctk.CTkButton(topo, text="+", width=36, command=lambda: self.zoom(1.15), **botao
                      ).pack(side="right", padx=2)
        ctk.CTkButton(topo, text="−", width=36, command=lambda: self.zoom(1 / 1.15), **botao
                      ).pack(side="right", padx=2)
        ctk.CTkLabel(topo, text="Zoom:", font=ctk.CTkFont(size=12),
                     text_color=("gray40", "#94a3b8")).pack(side="right", padx=(4, 2))

        # Controles do percurso
        controles = ctk.CTkFrame(self, corner_radius=10, fg_color=cinza)
        controles.pack(fill="x", padx=12, pady=(0, 6))

        self.seletor_modo = ctk.CTkSegmentedButton(
            controles, values=list(NOMES_MODOS.keys()), command=self._ao_trocar_modo,
            font=ctk.CTkFont(size=13, weight="bold"),
        )
        self.seletor_modo.set("Pré-ordem")
        self.seletor_modo.pack(side="left", padx=12, pady=10)

        ctk.CTkButton(controles, text="↺ Recomeçar", width=100, command=self.reiniciar, **botao
                      ).pack(side="left", padx=4)
        ctk.CTkButton(controles, text="◀ Anterior", width=95, command=self.anterior, **botao
                      ).pack(side="left", padx=4)
        ctk.CTkButton(controles, text="Próximo ▶", width=95, command=self.proximo,
                      height=32, corner_radius=8, fg_color="#3b82f6", hover_color="#2563eb"
                      ).pack(side="left", padx=4)
        self.btn_play = ctk.CTkButton(
            controles, text="▶ Reproduzir", width=120, command=self.alternar_reproducao,
            height=32, corner_radius=8, fg_color="#10b981", hover_color="#059669",
            font=ctk.CTkFont(weight="bold"),
        )
        self.btn_play.pack(side="left", padx=4)

        self.slider_vel = ctk.CTkSlider(controles, from_=1, to=5, number_of_steps=4, width=90)
        self.slider_vel.set(2)
        self.slider_vel.pack(side="right", padx=(4, 14))
        ctk.CTkLabel(controles, text="Velocidade:", font=ctk.CTkFont(size=12),
                     text_color=("gray40", "#94a3b8")).pack(side="right")

        # Área do desenho (canvas com barras de rolagem)
        area = ctk.CTkFrame(self, corner_radius=10, fg_color=("white", "#181b20"))
        area.pack(fill="both", expand=True, padx=12, pady=(0, 6))
        area.grid_rowconfigure(0, weight=1)
        area.grid_columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(area, highlightthickness=0, bd=0)
        self.canvas.grid(row=0, column=0, sticky="nsew", padx=4, pady=4)
        sb_y = tk.Scrollbar(area, orient="vertical", command=self.canvas.yview)
        sb_y.grid(row=0, column=1, sticky="ns")
        sb_x = tk.Scrollbar(area, orient="horizontal", command=self.canvas.xview)
        sb_x.grid(row=1, column=0, sticky="ew")

        self.canvas.configure(xscrollcommand=sb_x.set, yscrollcommand=sb_y.set)

        self.canvas.bind("<Configure>", self._ao_redimensionar)
        self.canvas.bind("<MouseWheel>", self._roda_vertical)
        self.canvas.bind("<Shift-MouseWheel>", self._roda_horizontal)
        self.canvas.bind("<Button-4>", lambda e: self.canvas.yview_scroll(-1, "units"))
        self.canvas.bind("<Button-5>", lambda e: self.canvas.yview_scroll(1, "units"))

        # Legenda das cores
        legenda = ctk.CTkFrame(self, fg_color="transparent")
        legenda.pack(fill="x", padx=16, pady=(0, 2))
        ctk.CTkLabel(legenda, text="Cores:", font=ctk.CTkFont(size=12),
                     text_color=("gray40", "#94a3b8")).pack(side="left", padx=(0, 8))
        for chave, nome in LEGENDA:
            cor_claro = PALETAS["Light"][chave][1]
            cor_escuro = PALETAS["Dark"][chave][1]
            ctk.CTkLabel(
                legenda, text=f"● {nome}", font=ctk.CTkFont(size=12, weight="bold"),
                text_color=(cor_claro, cor_escuro),
            ).pack(side="left", padx=8)

        # Painel inferior: explicação do percurso + ordem de visita
        painel = ctk.CTkFrame(self, corner_radius=10, fg_color=cinza)
        painel.pack(fill="x", padx=12, pady=(4, 10))

        self.lbl_titulo_modo = ctk.CTkLabel(
            painel, text="", anchor="w", font=ctk.CTkFont(size=14, weight="bold"),
            text_color=("#d97706", "#fbbf24"),
        )
        self.lbl_titulo_modo.pack(fill="x", padx=14, pady=(10, 0))

        self.lbl_explica = ctk.CTkLabel(
            painel, text="", anchor="w", justify="left", wraplength=1000,
            font=ctk.CTkFont(size=13), text_color=("gray20", "#cbd5e1"),
        )
        self.lbl_explica.pack(fill="x", padx=14, pady=(2, 6))

        self.lbl_status = ctk.CTkLabel(
            painel, text="", anchor="w", font=ctk.CTkFont(size=13, weight="bold"),
            text_color=("#2563eb", "#93c5fd"),
        )
        self.lbl_status.pack(fill="x", padx=14, pady=(0, 4))

        moldura_seq = ctk.CTkFrame(painel, corner_radius=8, fg_color=("gray85", "#262b33"))
        moldura_seq.pack(fill="x", padx=12, pady=(0, 12))
        moldura_seq.grid_columnconfigure(0, weight=1)
        self.texto_seq = tk.Text(
            moldura_seq, height=3, wrap="word", bd=0, highlightthickness=0,
            padx=10, pady=8, cursor="arrow", takefocus=0,
        )
        self.texto_seq.grid(row=0, column=0, sticky="ew", padx=(2, 0), pady=2)
        sb_seq = tk.Scrollbar(moldura_seq, orient="vertical", command=self.texto_seq.yview)
        sb_seq.grid(row=0, column=1, sticky="ns")
        self.texto_seq.configure(yscrollcommand=sb_seq.set)

        # Ajusta a quebra de linha do texto quando a janela muda de tamanho
        self.bind("<Configure>", self._ao_redimensionar_janela)

    # ----- Ajudas de tema ----------------------------------------------------
    def _paleta(self):
        return PALETAS["Dark" if ctk.get_appearance_mode() == "Dark" else "Light"]

    def _ao_redimensionar_janela(self, event):
        if event.widget is self:
            self.lbl_explica.configure(wraplength=max(300, event.width - 60))

    # ----- Zoom e rolagem ----------------------------------------------------
    def zoom(self, fator):
        self.escala = max(0.4, min(2.2, self.escala * fator))
        self.desenhar()

    def ajustar_a_janela(self):
        self.update_idletasks()
        cw = max(200, self.canvas.winfo_width() - 24)
        ch = max(150, self.canvas.winfo_height() - 12)
        self.escala = max(0.45, min(1.3, cw / self.largura, ch / self.altura))
        self.desenhar()

    def _roda_vertical(self, event):
        self.canvas.yview_scroll(-1 if event.delta > 0 else 1, "units")

    def _roda_horizontal(self, event):
        self.canvas.xview_scroll(-1 if event.delta > 0 else 1, "units")

    def _ao_redimensionar(self, event):
        # Espera um pouquinho para não redesenhar a cada pixel arrastado
        if self._job_redesenho:
            self.after_cancel(self._job_redesenho)
        self._job_redesenho = self.after(60, self.desenhar)

    # ----- Desenho -----------------------------------------------------------
    def _ret_arredondado(self, x1, y1, x2, y2, r, **kw):
        # Pontos repetidos deixam as retas retas e arredondam só os cantos
        pontos = [
            x1 + r, y1, x1 + r, y1, x2 - r, y1, x2 - r, y1, x2, y1, x2, y1 + r,
            x2, y1 + r, x2, y2 - r, x2, y2 - r, x2, y2, x2 - r, y2, x2 - r, y2,
            x1 + r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y2 - r, x1, y1 + r,
            x1, y1 + r, x1, y1,
        ]
        return self.canvas.create_polygon(pontos, smooth=True, **kw)

    def desenhar(self):
        self._job_redesenho = None
        c = self.canvas
        p = self._paleta()
        s = self.escala
        c.delete("all")
        c.configure(bg=p["fundo"])

        larg_vis = max(c.winfo_width(), 100)
        alt_vis = max(c.winfo_height(), 100)
        larg_desenho, alt_desenho = self.largura * s, self.altura * s
        # Centraliza quando a árvore é menor que a janela
        ox = max(0, (larg_vis - larg_desenho) / 2)
        c.configure(scrollregion=(0, 0, max(larg_desenho, larg_vis), max(alt_desenho, alt_vis)))

        fonte_rot = ("Arial", max(6, round(11 * s)), "bold")
        fonte_leg = ("Arial", max(5, round(8 * s)))
        fonte_lig = ("Arial", max(5, round(8 * s)))
        fonte_num = ("Arial", max(6, round(9 * s)), "bold")

        # 1) Linhas entre os nós (e o nome de cada ligação)
        for no in self.todos:
            for nome, f in no.filhos:
                x1, y1 = ox + no.x * s, (no.y + ALT_NO / 2) * s
                x2, y2 = ox + f.x * s, (f.y - ALT_NO / 2) * s
                ym = (y1 + y2) / 2  # altura da "barra" horizontal do cotovelo
                c.create_line(x1, y1, x1, ym, x2, ym, x2, y2, fill=p["linha"],
                              width=max(1, 1.5 * s))
                if nome:
                    t = c.create_text(x2, (ym + y2) / 2, text=nome,
                                      fill=p["suave"], font=fonte_lig)
                    caixa = c.bbox(t)
                    fundo = c.create_rectangle(caixa[0] - 2, caixa[1], caixa[2] + 2, caixa[3],
                                               fill=p["fundo"], outline="")
                    c.tag_lower(fundo, t)

        # 2) Caixinhas dos nós
        rodando = self.passo > 0
        for no in self.todos:
            i = self.indice[id(no)]
            visitado = rodando and i < self.passo
            atual = rodando and i == self.passo - 1
            apagado = rodando and i >= self.passo

            x1, y1 = ox + (no.x - no.larg / 2) * s, (no.y - ALT_NO / 2) * s
            x2, y2 = ox + (no.x + no.larg / 2) * s, (no.y + ALT_NO / 2) * s
            cx, cy = (x1 + x2) / 2, (y1 + y2) / 2

            fundo, borda, cor_texto = p[no.categoria]
            cor_leg = p["suave"]
            espessura = 2
            if apagado:
                fundo, borda, cor_texto = p["painel"], p["linha"], p["suave"]
                espessura = 1
            elif visitado:
                espessura = 3

            if atual:  # anel de destaque em volta do nó da vez
                self._ret_arredondado(x1 - 5 * s, y1 - 5 * s, x2 + 5 * s, y2 + 5 * s,
                                      14 * s, fill="", outline=p["destaque"], width=3)

            self._ret_arredondado(x1, y1, x2, y2, 10 * s, fill=fundo, outline=borda,
                                  width=espessura)
            c.create_text(cx, cy - 9 * s, text=no.legenda, fill=cor_leg, font=fonte_leg)
            c.create_text(cx, cy + 8 * s, text=no.rotulo, fill=cor_texto, font=fonte_rot)

            if visitado:  # bolinha com o número da ordem de visita
                r = 10 * s
                cor_bola = p["destaque"] if atual else p["badge"]
                cor_num = p["destaque_texto"] if atual else p["badge_texto"]
                c.create_oval(x2 - r, y1 - r, x2 + r, y1 + r, fill=cor_bola, outline="")
                c.create_text(x2, y1, text=str(i + 1), fill=cor_num, font=fonte_num)

    # ----- Percurso ----------------------------------------------------------
    def _ao_trocar_modo(self, nome):
        self.parar_reproducao()
        self.modo = NOMES_MODOS[nome]
        self.ordem = percurso(self.raiz, self.modo)
        self.indice = {id(n): i for i, n in enumerate(self.ordem)}
        self.passo = 0
        self._atualizar_texto_modo()
        self.atualizar()

    def _atualizar_texto_modo(self):
        titulo, explicacao = MODOS[self.modo]
        self.lbl_titulo_modo.configure(text=titulo)
        self.lbl_explica.configure(text=explicacao)

    def proximo(self):
        if self.passo < len(self.ordem):
            self.passo += 1
            self.atualizar()

    def anterior(self):
        self.parar_reproducao()
        if self.passo > 0:
            self.passo -= 1
            self.atualizar()

    def reiniciar(self):
        self.parar_reproducao()
        self.passo = 0
        self.atualizar()

    def alternar_reproducao(self):
        if self.tocando:
            self.parar_reproducao()
            return
        if self.passo >= len(self.ordem):
            self.passo = 0
            self.atualizar()
        self.tocando = True
        self.btn_play.configure(text="⏸ Pausar")
        self._tique()

    def parar_reproducao(self):
        self.tocando = False
        if self._job_tique:
            self.after_cancel(self._job_tique)
            self._job_tique = None
        self.btn_play.configure(text="▶ Reproduzir")

    def _tique(self):
        if not self.tocando:
            return
        if self.passo >= len(self.ordem):
            self.parar_reproducao()
            return
        self.proximo()
        atraso = int(2400 / max(1, self.slider_vel.get()))
        self._job_tique = self.after(atraso, self._tique)

    # ----- Atualizações da tela ---------------------------------------------
    def atualizar(self):
        self.desenhar()
        self._atualizar_sequencia()
        self._atualizar_status()

    def _atualizar_status(self):
        total = len(self.ordem)
        if self.passo == 0:
            texto = "Clique em «Próximo ▶» ou «Reproduzir» para começar  (atalhos: ← → e Espaço)"
        else:
            no = self.ordem[self.passo - 1]
            texto = f"Passo {self.passo} de {total}:  visitando  {no.rotulo}  ({no.legenda})"
            if self.passo == total:
                texto += "   —   fim do percurso!"
        self.lbl_status.configure(text=texto)

    def _atualizar_sequencia(self):
        """Mostra a ordem de visita em texto: 2 → * → 3 → + → 1"""
        p = self._paleta()
        t = self.texto_seq
        t.configure(state="normal", bg="#262b33" if p is PALETAS["Dark"] else "#d9dee5")
        t.delete("1.0", "end")

        fonte = ("Courier New", 13)
        t.tag_configure("neutro", foreground=p["texto"], font=fonte)
        t.tag_configure("feito", foreground=p["texto"], font=fonte)
        t.tag_configure("futuro", foreground=p["suave"], font=fonte)
        t.tag_configure("seta", foreground=p["suave"], font=fonte)
        t.tag_configure("atual", foreground=p["destaque_texto"], background=p["destaque"],
                        font=("Courier New", 13, "bold"))

        for i, no in enumerate(self.ordem):
            if i:
                t.insert("end", "  →  ", "seta")
            if self.passo == 0:
                marca = "neutro"
            elif i == self.passo - 1:
                marca = "atual"
            elif i < self.passo:
                marca = "feito"
            else:
                marca = "futuro"
            t.insert("end", f" {no.rotulo} ", marca)

        faixa = t.tag_ranges("atual")
        if faixa:
            t.see(faixa[0])
        t.configure(state="disabled")

    # ----- Exportar ----------------------------------------------------------
    def exportar_svg(self):
        nome_modo = {"pre": "pre-ordem", "em": "em-ordem", "pos": "pos-ordem"}[self.modo]
        caminho = filedialog.asksaveasfilename(
            parent=self, defaultextension=".svg", initialfile=f"ast_{nome_modo}.svg",
            filetypes=[("Imagem SVG", "*.svg")],
        )
        if not caminho:
            return
        rodape = f"Percurso em {nome_modo}  (os números mostram a ordem de visita)"
        try:
            with open(caminho, "w", encoding="utf-8") as arq:
                arq.write(gerar_svg(self.raiz, self.largura, self.altura, self.ordem, rodape))
        except OSError as erro:
            self.lbl_status.configure(text=f"Não foi possível salvar: {erro}")
            return
        self.lbl_status.configure(text=f"Imagem salva em: {caminho}")

    def fechar(self):
        self.parar_reproducao()
        if self._job_redesenho:
            self.after_cancel(self._job_redesenho)
        self.destroy()


# ---------------------------------------------------------------------------
# 9) Rodar sozinho (bom para testar): python Interface/visualizador_ast.py [arquivo]
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    pasta_raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if pasta_raiz not in sys.path:
        sys.path.insert(0, pasta_raiz)

    from src.compilador.lexer import tokenizar
    from src.compilador.parser import analisar_sintaxe

    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as arq:
            codigo_demo = arq.read()
    else:
        codigo_demo = "PROGRAMA\n  x = 2 * (3 + 1)\nFIM_PROGRAMA"

    arvore, quantidade = analisar_sintaxe(tokenizar(codigo_demo.strip()))

    ctk.set_appearance_mode("dark")
    raiz_tk = ctk.CTk()
    raiz_tk.withdraw()
    janela = JanelaArvoreAST(raiz_tk, arvore.para_dict(),  quantidade, codigo_demo)
    janela.protocol("WM_DELETE_WINDOW", lambda: (janela.fechar(), raiz_tk.destroy()))
    raiz_tk.mainloop()