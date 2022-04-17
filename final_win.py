# напиши здесь код третьего экрана приложения
from PyQt5. QtCore import Qt
from PyQt5. QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QRadioButton, QGridLayout
    QGroup, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *
from final_win import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.set_appear() 

        self.show()

    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.btn_text = QPushButton(txt_sendresult, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)

        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)

        self.line_name = QLineEdit(txt_hintname)

        self.line_age = QLineEdit(txt_hintage)

        self.line_test1 = QLineEdit(txt__hinttest1)

        self.line_test2 = QLineEdit(txt_hinttest2)

        self.line_test3 = QLineEdit(txt_hinttest3)

        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QVBoxLayout()
        self.r_line.addWidget(self.text_timer, alignnment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignnment = Qt.AlignCenter)            
        self.l_line.addWidget(self.line_name, alignnment = Qt.AlignCenter)   
        self.l_line.addWidget(self.text_age, alignnment = Qt.AlignCenter)   
        self.l_line.addWidget(self.line_age, alignnment = Qt.AlignCenter)   
        self.l_line.addWidget(self.text_test1, alignnment = Qt.AlignCenter)   
        self.l_line.addWidget(self.btn_test1, alignnment = Qt.AlignCenter)   
        self.l_line.addWidget(self.line_test1, alignnment = Qt.AlignCenter)   
        self.l_line.addWidget(self.text_test2, alignnment = Qt.AlignCenter)   
        self.l_line.addWidget(self.btn_test2, alignnment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_test3, alignnment = Qt.AlignCenter) 
        self.l_line.addWidget(self.btn_test3, alignnment = Qt.AlignCenter) 
        self.l_line.addWidget(self.line_test2, alignnment = Qt.AlignCenter)
        self.l_line.addWidget(self.line_test3, alignnment = Qt.AlignCenter) 
        self.l_line.addWidget(self.btn_next, alignnment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

    def next_click(self):
        self.hide()
        self.fw = FinalWin()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)    

        