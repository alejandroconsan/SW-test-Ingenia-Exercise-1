## Exercise 1
## Alejandro Conde Sánchez
## alejandroconsan@gmail.com

import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer


class ProgressBar(QWidget):
    def __init__(self):
        super().__init__()
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(30, 40, 200, 25)

        self.btnStart = QPushButton('Start', self)
        self.btnStart.move(30, 80)
        self.btnStart.clicked.connect(self.startProgress)

        self.btnStop = QPushButton('Stop', self)
        self.btnStop.move(120, 80)
        self.btnStop.clicked.connect(self.stopBar)

        self.timer = QBasicTimer()
        self.step = 0
        self.n_steps = 100
        self.endtime = 5000
        self.timeout = self.endtime/self.n_steps

    def resetBar(self):
        self.step = 0
        self.progressBar.setValue(0)

    def stopBar(self):
        if self.timer.isActive():
            self.timer.stop()

    def startProgress(self):
        if not(self.timer.isActive()):
            self.timer.start(self.timeout, self)

    def timerEvent(self, event):
        if self.step >= self.n_steps:
            self.timer.stop()
            return
        self.step += 1
        self.progressBar.setValue(self.step)

if __name__=='__main__':
    app = QApplication(sys.argv)
    PB = ProgressBar()
    PB.show()
    sys.exit(app.exec_())