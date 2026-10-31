# Atalho simples para iniciar a IDE da TEA Language (TL)
# Basta rodar: python3 iniciar_ide.py

import os
import sys

# Pega o caminho da pasta Interface
pasta_interface = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Interface")
sys.path.insert(0, pasta_interface)

# Inicia o aplicativo da IDE
from ide_tl import IDE_TEALanguage

if __name__ == "__main__":
    print("Iniciando a IDE da TEA Language (TL)...")
    app = IDE_TEALanguage()
    app.mainloop()
