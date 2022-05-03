import sys
from PyQt5 import QtWidgets

def window():
    app=QtWidgets.QApplication(sys.argv)
   
    button1=QtWidgets.QPushButton("Evet")
    button2=QtWidgets.QPushButton("Hayır")
    h_box=QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(button1)
    h_box.addWidget(button2)
    
    v_box
    
    window=QtWidgets.QWidget()
    window.setWindowTitle("TRY 5")
    
    window.setLayout(h_box)
    window.show()
    sys.exit(app.exec_())
window()
