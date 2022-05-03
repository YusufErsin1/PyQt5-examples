import sys
from PyQt5 import QtWidgets

class window(QtWidgets.QWidget):
    def __init__(self):
        
        super().__init__() 
        self.init_ui()
    def init_ui(self):
        self.yazi=QtWidgets.QLineEdit()
        self.temiz=QtWidgets.QPushButton("temizle")
        self.yazdir=QtWidgets.QPushButton("yazdır")
        
        v_box=QtWidgets.QVBoxLayout()
        
        v_box.addWidget(self.yazi)
        v_box.addWidget(self.temiz)
        v_box.addWidget(self.yazdir)
        
        self.setLayout(v_box)
        
        self.temiz.clicked.connect(self.click)
        self.yazdir.clicked.connect(self.click)
        self.show()        
        
    def click(self):
        sender=self.sender()
        
        if sender.text()=="temizle":
            self.yazi.clear()
        elif sender.text()=="yazdır":
            print(self.yazi.text())
        

app=QtWidgets.QApplication(sys.argv)
window=window()
sys.exit(app.exec_())
