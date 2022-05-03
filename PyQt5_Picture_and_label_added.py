import sys
from PyQt5 import QtWidgets,QtGui

def window():
    app=QtWidgets.QApplication(sys.argv)
    window=QtWidgets.QWidget()
    window.setWindowTitle("try2")
    label1=QtWidgets.QLabel(window)
    label2=QtWidgets.QLabel(window)
    label3=QtWidgets.QLabel(window)
    label3.setPixmap(QtGui.QPixmap("C:/Users/yusuf/Desktop/image.jpg"))
    label1.setText("try in")
    label2.setPixmap(QtGui.QPixmap("image1.jpg"))
    window.setGeometry(100, 100, 600, 500)
    label1.move(300,25)
    label2.move(150,50)
    label3.move(120,225)
    window.show()
    sys.exit(app.exec_())
window()
