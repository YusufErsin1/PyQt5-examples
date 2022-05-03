import sys
from PyQt5 import QtWidgets,QtGui

def window():
    app=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    button1=QtWidgets.QPushButton("Tamam")#burada yazıda yazabilirim
    button2=QtWidgets.QPushButton("İptal") 
    button3=QtWidgets.QPushButton("Delete")
    button4=QtWidgets.QPushButton("Okay")
    h_box=QtWidgets.QHBoxLayout()

    h_box.addWidget(button1)
    h_box.addWidget(button2)
    window.setLayout(h_box)
    h_box.addStretch()#sola yasladı
    
    window.setWindowTitle("Try 3")
    window.show()
    sys.exit(app.exec_())
window()