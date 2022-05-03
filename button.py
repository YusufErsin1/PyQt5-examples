import sys
from PyQt5 import QtWidgets

def window():
    app=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    button=QtWidgets.QPushButton(window)
    button.setText("Button")
    button.move(300,250)
    
    window.setWindowTitle("try 3")
    window.show()
    sys.exit(app.exec_())
window()
