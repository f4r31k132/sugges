# напиши здесь код основного приложения и первого экрана
from instr import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def unitUI(self):
        self.hello_text = QLabel(txt_hello)
        self.instructions =QLabel(txt_instruction)
        self.button = QLabelButton(txt_next)
        self.layout = QVBoxLayout()
        self.hello_text.addWidget(self.layout)
        self.instructions.addWidget(self.layout)
        self.btn.add.Widget(self.layout)    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self): 
        self.hide()
        self.tw = TestWin()           
app = QApplications({}) 
mw = MainWin()
app.exec_()  
     