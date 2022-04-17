from PyQt5.QtCore import Qt, QTimer, QTime

from instr import *

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3

class TestWin(QWidget):
    def timer_test(self):
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time 
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm;ss"))
        self.text_timer.setFont(QFont("Times", 36, QFront.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0")
        if time.toString("hh:mm:ss") == "00:00:00"
            self.timer.stop()

    def timer_sits(self):
        time = QTime(0, 0, 30)
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer2Event(self):
        self.timer.time.setTaxi(time.toString("hh:mm:ss")[6:8])

    def timer_final(self):
        time = QTime(0,1,0) 
        self.timer.time.connect(self.timer3Event)

    def timer3Event(self):
        if int(time.toString("hh:mm:ss")[6:8]) => 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0") 
        elif int(time.toString("hh:mm:ss")[6:8]) <=15:
            self.text_timer.setStyleSheet("color:rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")

        connects(self):
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)

        next_click(self):
        self.hide()
        self.exp = Experiment(self.line_age.text(),self.line_test1.text(),self.line_test2.text(),self.line_test3.text())