import psycopg2
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

conns = []

class textInput(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("Libreria Papeleria") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('contraseña:')
        self.line = QLineEdit(self)

        self.line.move(80, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)        

    def clickMethod(self):
        ps = self.line.text()
        cn = Connection(ps)
        if not cn:
            print("contraseña incorrecta")
        else:
            conns.append(cn)
            self.close()


def Connection(ps):
    try:
        return psycopg2.connect(database="Libreria_Papeleria",user='postgres',password=ps,host='127.0.0.1',port='5432')
    except:
        return 0
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = textInput()
    mainWin.show()
    print("ew")
    sys.exit( app.exec_() )
    