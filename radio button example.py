import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QRadioButton,QVBoxLayout,QLabel

class window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.init_ui()
    def init_ui(self):
        self.radio_yazisi=QLabel("sizce hangisi doğru dildir")
        self.java=QRadioButton("Java")
        self.pyhton=QRadioButton("Pyhton")
        self.php=QRadioButton("Php")    
        self.yazi_alani=QLabel("")
        self.buton= QPushButton("Gönder")
        
        v_box=QVBoxLayout()
        
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.pyhton)
        v_box.addWidget(self.php)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)
        
        self.setLayout(v_box)
        self.setWindowTitle("RadioButton Example")
        
        self.buton.clicked.connect(lambda: self.click(self.pyhton.isChecked(),self.java.isChecked(),self.php.isChecked(),self.yazi_alani))
        
        
        self.show()
        
    def click(self,pyhton,java,php,yazi_alani):
        if pyhton:
            yazi_alani.setText("pyhton seçildi")
        if java:
            yazi_alani.setText("java seçildi")
        if php:
             yazi_alani.setText("php seçildi")


app=QApplication(sys.argv)
window=window()
sys.exit(app.exec_())
