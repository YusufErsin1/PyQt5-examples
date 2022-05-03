import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init__ui()
    def init__ui(self):
        self.buton=QtWidgets.QPushButton("Bana tıkla")
        self.yazi_alani=QtWidgets.QLabel("Buna henüz tıklanmadı")
        self.sayi=0
        
        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        
        
        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        
        
        self.setLayout(h_box)
        
        self.buton.clicked.connect(self.click)
        self.show()
    def click(self):
        self.sayi+=1
        self.yazi_alani.setText("Bana "+str(self.sayi)+" tıklandi")

app=QtWidgets.QApplication(sys.argv)
window=Window()
sys.exit(app.exec_())