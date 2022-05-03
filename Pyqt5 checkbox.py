import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout

class window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):
        
        self.checkbox=QCheckBox("Onaylıyor musunuz?")
        self.yazi_alani=QLabel("")
        self.buton=QPushButton("GİR")
        
        v_box=QVBoxLayout()
        
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)
        
        self.setLayout(v_box)
        self.buton.clicked.connect(lambda: self.click(self.checkbox.isChecked(),self.yazi_alani))
        self.show()
    
    def click(self,clickbox,yazi_alani):
        if clickbox:
            self.yazi_alani.setText("Checkbox tıklandı.")
        else:
            self.yazi_alani.setText("Checkbox tıklanmadı.")
    
    
app=QApplication(sys.argv)
window=window()
sys.exit(app.exec_())
    
