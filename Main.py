import sys
import os
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QFileDialog
from Organizar import Organizar
# ________ ___  ___  ________   ________  ________      
#|\  _____\\  \|\  \|\   ___  \|\   ____\|\   ____\     
#\ \  \__/\ \  \\\  \ \  \\ \  \ \  \___|\ \  \___|_    
# \ \   __\\ \  \\\  \ \  \\ \  \ \  \    \ \_____  \   
#  \ \  \_| \ \  \\\  \ \  \\ \  \ \  \____\|____|\  \  
#   \ \__\   \ \_______\ \__\\ \__\ \_______\____\_\  \ 
#    \|__|    \|_______|\|__| \|__|\|_______|\_________\
#                                           \|_________|
def SelecionarPasta():
    caminho = QFileDialog.getExistingDirectory(None, "Selecione uma Pasta")
    if caminho:
        window.lineEdit.setText(caminho)
        window.listWidget.addItem(caminho)
    else:
        print("Erro")
def finalizar():
    total_de_pastas = window.listWidget.count()
    if total_de_pastas == 0:
        print("A lista está vazia! Adicione pastas primeiro.")
        return
    
    for i in range(total_de_pastas):
        caminho_da_pasta = window.listWidget.item(i).text()
        try:
            RodarOrganizarOBJ = Organizar(caminho_da_pasta)
            RodarOrganizarOBJ.OrganizarPasta()
            print(f"Pasta organizada com sucesso: {caminho_da_pasta}")
        except Exception as e:
            print(f"Erro ao organizar {caminho_da_pasta}: {e}")
    window.listWidget.clear()
    print("Processo finalizado para todas as pastas!")



# ________  ________  ________  ________  ________     
#|\   __  \|\   __  \|\   ___ \|\   __  \|\   __  \    
#\ \  \|\  \ \  \|\  \ \  \_|\ \ \  \|\  \ \  \|\  \   
# \ \   _  _\ \  \\\  \ \  \ \\ \ \   __  \ \   _  _\  
#  \ \  \\  \\ \  \\\  \ \  \_\\ \ \  \ \  \ \  \\  \| 
#   \ \__\\ _\\ \_______\ \_______\ \__\ \__\ \__\\ _\ 
#    \|__|\|__|\|_______|\|_______|\|__|\|__|\|__|\|__|

PastaRodando = os.path.dirname(os.path.abspath(__file__))
CaminhoMenu = os.path.join(PastaRodando, "Menu.ui")
Tela = QtWidgets.QApplication(sys.argv)
window = uic.loadUi(CaminhoMenu)

window.SelecionarPasta.clicked.connect(SelecionarPasta)
window.FinalizarBTN.clicked.connect(finalizar)

window.show()
sys.exit(Tela.exec())