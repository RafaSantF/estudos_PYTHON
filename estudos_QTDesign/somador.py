from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

def funcao_soma():
    valor1 = programa.textEdit.text() #Caso seja um QTexEdit utillze -> .toPlainText()
    valor2 = programa.textEdit_2.text()
    soma = float(valor1) + float(valor2)
    programa.label.setNum(soma) #Caso seja uma string usa-se 'setText'
    
def funcao_apagar_soma():
    programa.label.clear()

def gerar_messagebox():
    QMessageBox.about(programa, "POPUP!!", "Voce gerou um popup!")

def fechar_janela():
    programa.close()

def abrir_segunda_tela():
    programa2.show()

def frame1():
    programa.frame_2.close()
    programa.frame.show()

def frame2():
    programa.frame.close()
    programa.frame_2.show()


app= QtWidgets.QApplication([])
programa = uic.loadUi("somador.ui") #CONEXAO DESTE ARQUIVO PYTHON COM QT DESIGN
programa2= uic.loadUi("segunda_tela.ui") #CONEXAO DA SEGUNDA TELA COM QT DESIGN 
programa.pushButton.clicked.connect(funcao_soma) #BotAo somador
programa.pushButton_2.clicked.connect(funcao_apagar_soma) #BotAo para limpar resultado
programa.pushButton_3.clicked.connect(gerar_messagebox) #BotAo para gerar o popup
programa.pushButton_4.clicked.connect(fechar_janela) #BotAo para fechar janela
programa.pushButton_5.clicked.connect(abrir_segunda_tela) #BotAo para abrir um segunda tela
programa.pushButton_6.clicked.connect(frame1) #BotAo para abrir o frame 1 e fechar o frame 2
programa.pushButton_7.clicked.connect(frame2) #BotAo para abrir o frame 2 e fechar o frame 1


programa.show()
app.exec()