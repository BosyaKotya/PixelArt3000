import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton


class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Choose level')
        self.setGeometry(300, 300, 300, 300)
        self.psem = QPushButton(self)
        self.psem.setText('57')
        self.psem.resize(150, 150)
        self.psem.move(75, 75)
        self.parrot = QPushButton(self)
        self.parrot.setText('Попугай')
        self.parrot.resize(75, 75)
        self.parrot.move(0, 0)
        self.heart = QPushButton(self)
        self.heart.setText('Сердце')
        self.heart.resize(75, 75)
        self.heart.move(0, 225)
        self.cool = QPushButton(self)
        self.cool.setText('Крутой')
        self.cool.resize(75, 75)
        self.cool.move(225, 0)
        self.ok = QPushButton(self)
        self.ok.setText('OK эмоджи')
        self.ok.resize(75, 75)
        self.parrot.move(225, 225)
        self.psem.show()
        self.parrot.show()
        self.heart.show()
        self.cool.show()
        self.ok.show()
        self.psem.clicked.connect(self.show_psem)
        self.parrot.clicked.connect(self.show_parrot)
        self.heart.clicked.connect(self.show_heart)
        self.cool.clicked.connect(self.show_cool)
        self.ok.clicked.connect(self.show_ok)

    def show_psem(self):
        self.w2 = Psem()
        self.w2.show()
        self.close()

    def show_parrot(self):
        self.w2 = Papug()
        self.w2.show()
        self.close()

    def show_heart(self):
        self.w2 = Heart()
        self.w2.show()
        self.close()

    def show_cool(self):
        self.w2 = Cool()
        self.w2.show()
        self.close()

    def show_ok(self):
        self.w2 = Ok()
        self.w2.show()
        self.close()


class Cool(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 360)
        self.setWindowTitle('Cool')

        x = 14
        y = 14
        n = 20
        self.colors = ['#FFFFFF', '#000000', '#FFA500']
        self.cool = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 2, 2, 2, 2, 1, 1, 0, 0, 0],
                     [0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0],
                     [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
                     [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 2, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 2, 1],
                     [1, 2, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 2, 1],
                     [1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1],
                     [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
                     [0, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0],
                     [0, 0, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1, 0, 0],
                     [0, 0, 0, 1, 1, 2, 2, 2, 2, 1, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0]]

        self.bts = [[QPushButton(str(self.cool[i][j]), self) for j in range(x)] for i in range(y)]
        for i in range(y):
            for j in range(x):
                self.bts[i][j].resize(n, n)
                self.bts[i][j].move(n*j, n*i)
                self.bts[i][j].clicked.connect(self.opa)
                self.bts[i][j].setStyleSheet('QPushButton {background-color: ' + self.colors[0] + ';}')
                if self.bts[i][j].text() == '0':
                    self.bts[i][j].setStyleSheet('QPushButton {background-color: white; color: white;}')

        self.okbtn = QPushButton('exit', self)
        self.okbtn.resize(50, 40)
        self.okbtn.move(190, 280)
        self.okbtn.clicked.connect(self.ok)
        self.restartbtn = QPushButton('restart', self)
        self.restartbtn.resize(50, 40)
        self.restartbtn.move(190, 320)
        self.restartbtn.clicked.connect(self.restart)
        self.c = 0

        self.cbts = [QPushButton(str(i), self) for i in range(3)]
        for i in range(3):
            self.cbts[i].resize(40, 40)
            self.cbts[i].clicked.connect(self.ccl)
            self.cbts[i].setStyleSheet('QPushButton {background-color: ' + self.colors[i] + ';}')
        self.cbts[1].setStyleSheet('QPushButton {background-color: #000000; color: white;}')
        self.cbts[0].move(0, 320)
        self.cbts[1].move(40, 320)
        self.cbts[2].move(80, 320)

    def opa(self):
        sender = self.sender()
        sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: black;}')
        if int(sender.text()) == self.c:
            sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: '+self.colors[self.c]+';}')
        elif self.c == 1:
            sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: white;}')

    def ccl(self):
        self.c = int(self.sender().text())
        
    def ok(self):
        self.close()
        
    def restart(self):
        x = 14
        y = 14
        for i in range(y):
            for j in range(x):
                self.bts[i][j].setStyleSheet('QPushButton {background-color: ' + self.colors[0] + ';}')
                if self.bts[i][j].text() == '0':
                    self.bts[i][j].setStyleSheet('QPushButton {background-color: white; color: white;}')
        

class Ok(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 220, 360)
        self.setWindowTitle('Ok')

        x = 11
        y = 15
        n = 20
        self.colors = ['#FFFFFF', '#000000', '#FFA500']
        self.ok = [[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 2, 2, 1, 0, 0, 0],
                   [0, 0, 0, 0, 1, 1, 2, 2, 1, 0, 0],
                   [0, 0, 0, 1, 2, 2, 1, 2, 2, 1, 0],
                   [0, 0, 0, 0, 1, 2, 2, 1, 2, 1, 0],
                   [0, 0, 1, 1, 1, 1, 2, 1, 2, 2, 1],
                   [0, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1],
                   [1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1],
                   [0, 1, 0, 0, 0, 1, 2, 2, 2, 2, 1],
                   [1, 2, 1, 0, 0, 1, 2, 2, 2, 2, 1],
                   [1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1],
                   [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                   [0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 0],
                   [0, 0, 0, 1, 2, 2, 2, 2, 1, 0, 0],
                   [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0]]

        self.bts = [[QPushButton(str(self.ok[i][j]), self) for j in range(x)] for i in range(y)]
        for i in range(y):
            for j in range(x):
                self.bts[i][j].resize(n, n)
                self.bts[i][j].move(n*j, n*i)
                self.bts[i][j].clicked.connect(self.opa)
                self.bts[i][j].setStyleSheet('QPushButton {background-color: ' + self.colors[0] + ';}')
                if self.bts[i][j].text() == '0':
                    self.bts[i][j].setStyleSheet('QPushButton {background-color: white; color: white;}')

        self.okbtn = QPushButton('exit', self)
        self.okbtn.resize(50, 40)
        self.okbtn.move(120, 320)
        self.okbtn.clicked.connect(self.close)
        self.restartbtn = QPushButton('restart', self)
        self.restartbtn.resize(50, 40)
        self.restartbtn.move(170, 320)
        self.restartbtn.clicked.connect(self.restart)
        self.c = 0

        self.cbts = [QPushButton(str(i), self) for i in range(3)]
        for i in range(3):
            self.cbts[i].resize(50, 40)
            self.cbts[i].clicked.connect(self.ccl)
            self.cbts[i].setStyleSheet('QPushButton {background-color: ' + self.colors[i] + ';}')
        self.cbts[1].setStyleSheet('QPushButton {background-color: #000000; color: white;}')
        self.cbts[0].move(0, 320)
        self.cbts[1].move(40, 320)
        self.cbts[2].move(80, 320)

    def opa(self):
        sender = self.sender()
        sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: black;}')
        if int(sender.text()) == self.c:
            sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: '+self.colors[self.c]+';}')
        elif self.c == 1:
            sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: white;}')

    def ccl(self):
        self.c = int(self.sender().text())

    def restart(self):
        x = 11
        y = 15
        for i in range(y):
            for j in range(x):
                self.bts[i][j].setStyleSheet('QPushButton {background-color: ' + self.colors[0] + ';}')
                if self.bts[i][j].text() == '0':
                    self.bts[i][j].setStyleSheet('QPushButton {background-color: white; color: white;}')
        
        
class Heart(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 360)
        self.setWindowTitle('Heart')
        
        x = 13
        y = 12
        n = 20
        
        self.colors = ['#FFFFFF', '#000000','#FF0000']
        self.heart = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 1, 2, 2, 1, 0, 0, 0, 1, 2, 2, 1, 0],
         [1, 2, 2, 2, 2, 1, 0, 1, 2, 2, 2, 2, 1],
         [1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1],
         [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
         [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
         [0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0],
         [0, 0, 0, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        self.bts = [[QPushButton(str(self.heart[i][j]), self) for j in range(x)] for i in range(y)]
        for i in range(y):
            for j in range(x):
                self.bts[i][j].resize(n, n)
                self.bts[i][j].move(n*j, n*i)
                self.bts[i][j].clicked.connect(self.opa)
                self.bts[i][j].setStyleSheet('QPushButton {background-color: ' + self.colors[0] + ';}')
                if self.bts[i][j].text() == '0':
                    self.bts[i][j].setStyleSheet('QPushButton {background-color: white; color: white;}')

        self.okbtn = QPushButton('exit', self)
        self.okbtn.resize(50, 40)
        self.okbtn.move(190, 280)
        self.okbtn.clicked.connect(self.close)
        self.restartbtn = QPushButton('restart', self)
        self.restartbtn.resize(50, 40)
        self.restartbtn.move(190, 320)
        self.restartbtn.clicked.connect(self.restart)
        self.c = 0

        self.cbts = [QPushButton(str(i), self) for i in range(3)]
        for i in range(3):
            self.cbts[i].resize(40, 40)
            self.cbts[i].clicked.connect(self.ccl)
            self.cbts[i].setStyleSheet('QPushButton {background-color: ' + self.colors[i] + ';}')
        self.cbts[1].setStyleSheet('QPushButton {background-color: #000000; color: white;}')
        self.cbts[0].move(0, 320)
        self.cbts[1].move(40, 320)
        self.cbts[2].move(80, 320)

    def opa(self):
        sender = self.sender()
        sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: black;}')
        if int(sender.text()) == self.c:
            sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: '+self.colors[self.c]+';}')
        elif self.c == 1:
            sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: white;}')

    def ccl(self):
        self.c = int(self.sender().text())

    def restart(self):
        x = 13
        y = 12
        for i in range(y):
            for j in range(x):
                self.bts[i][j].setStyleSheet('QPushButton {background-color: ' + self.colors[0] + ';}')
                if self.bts[i][j].text() == '0':
                    self.bts[i][j].setStyleSheet('QPushButton {background-color: white; color: white;}')


class Papug(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 240, 460)
        self.setWindowTitle('Papug')

        x = 12
        y = 19
        n = 20
        self.colors = ['#FFFFFF', '#000000', '#FF0000', '#00FF00', '#0000FF', '#9400D3', '#FFFF00']
        self.parrot = [[0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                       [2, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
                       [6, 6, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0],
                       [6, 6, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
                       [6, 1, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0],
                       [0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0],
                       [0, 2, 2, 2, 6, 6, 2, 0, 0, 0, 0, 0],
                       [0, 2, 2, 3, 6, 6, 6, 0, 0, 0, 0, 0],
                       [0, 2, 2, 3, 3, 6, 6, 6, 0, 0, 0, 0],
                       [0, 0, 2, 2, 4, 3, 3, 6, 0, 0, 0, 0],
                       [0, 0, 2, 2, 4, 4, 3, 3, 3, 0, 0, 0],
                       [0, 5, 5, 2, 2, 4, 4, 4, 3, 0, 0, 0],
                       [0, 5, 0, 0, 0, 2, 4, 4, 4, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 2, 4, 4, 4, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 2, 5, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 2, 5, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]]

        self.bts = [[QPushButton(str(self.parrot[i][j]), self) for j in range(x)] for i in range(y)]
        for i in range(y):
            for j in range(x):
                self.bts[i][j].resize(n, n)
                self.bts[i][j].move(n*j, n*i)
                self.bts[i][j].clicked.connect(self.opa)
                self.bts[i][j].setStyleSheet('QPushButton {background-color: ' + self.colors[0] + ';}')
                if self.bts[i][j].text() == '0':
                    self.bts[i][j].setStyleSheet('QPushButton {background-color: white; color: white;}')

        self.okbtn = QPushButton('exit', self)
        self.okbtn.resize(50, 40)
        self.okbtn.move(190, 380)
        self.okbtn.clicked.connect(self.close)
        self.okbtn.clicked.connect(self.close)
        self.restartbtn = QPushButton('restart', self)
        self.restartbtn.resize(50, 40)
        self.restartbtn.move(190, 420)
        self.restartbtn.clicked.connect(self.restart)
        self.c = 0

        self.cbts = [QPushButton(str(i), self) for i in range(7)]
        for i in range(7):
            self.cbts[i].resize(40, 40)
            self.cbts[i].clicked.connect(self.ccl)
            self.cbts[i].setStyleSheet('QPushButton {background-color: ' + self.colors[i] + ';}')
        self.cbts[1].setStyleSheet('QPushButton {background-color: #000000; color: white;}')
        self.cbts[0].move(0, 380)
        self.cbts[1].move(40, 380)
        self.cbts[2].move(80, 380)
        self.cbts[3].move(0, 420)
        self.cbts[4].move(40, 420)
        self.cbts[5].move(80, 420)
        self.cbts[6].move(120, 420)

    def opa(self):
        sender = self.sender()
        sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: black;}')
        if int(sender.text()) == self.c:
            sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: '+self.colors[self.c]+';}')
        elif self.c == 1:
            sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: white;}')

    def ccl(self):
        self.c = int(self.sender().text())

    def restart(self):
        x = 12
        y = 19
        for i in range(y):
            for j in range(x):
                self.bts[i][j].setStyleSheet('QPushButton {background-color: ' + self.colors[0] + ';}')
                if self.bts[i][j].text() == '0':
                    self.bts[i][j].setStyleSheet('QPushButton {background-color: white; color: white;}')


class Psem(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 260, 260)
        self.setWindowTitle('57')

        x = 13
        y = 9
        n = 20
        self.colors = ['#FFFFFF', '#FF0000', '#FFA500', '#FFFF00', '#00FF00', '#0000FF', '#9400D3']
        self.psem = [[5, 4, 3, 2, 1, 0, 0, 0, 1, 2, 3, 4, 5],
                [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
                [0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 3, 0, 0],
                [0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 4, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0, 0],
                [5, 0, 0, 2, 0, 0, 0, 0, 0, 6, 0, 0, 0],
                [0, 4, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

        self.bts = [[QPushButton(str(self.psem[i][j]), self) for j in range(x)] for i in range(y)]
        for i in range(y):
            for j in range(x):
                self.bts[i][j].resize(n, n)
                self.bts[i][j].move(n*j, n*i)
                self.bts[i][j].clicked.connect(self.opa)
                self.bts[i][j].setStyleSheet('QPushButton {background-color: ' + self.colors[0] + ';}')
                if self.bts[i][j].text() == '0':
                    self.bts[i][j].setStyleSheet('QPushButton {background-color: white; color: white;}')

        self.okbtn = QPushButton('exit', self)
        self.okbtn.resize(50, 40)
        self.okbtn.move(190, 180)
        self.okbtn.clicked.connect(self.close)
        self.restartbtn = QPushButton('restart', self)
        self.restartbtn.resize(50, 40)
        self.restartbtn.move(190, 220)
        self.restartbtn.clicked.connect(self.restart)
        self.c = 0

        self.cbts = [QPushButton(str(i), self) for i in range(7)]
        for i in range(7):
            self.cbts[i].resize(40, 40)
            self.cbts[i].clicked.connect(self.ccl)
            self.cbts[i].setStyleSheet('QPushButton {background-color: ' + self.colors[i] + ';}')
        self.cbts[0].move(0, 180)
        self.cbts[1].move(40, 180)
        self.cbts[2].move(80, 180)
        self.cbts[3].move(0, 220)
        self.cbts[4].move(40, 220)
        self.cbts[5].move(80, 220)
        self.cbts[6].move(120, 220)

    def opa(self):
        sender = self.sender()
        sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: black;}')
        if int(sender.text()) == self.c:
            sender.setStyleSheet('QPushButton {background-color: ' + self.colors[self.c] + '; color: '+self.colors[self.c]+';}')

    def ccl(self):
        self.c = int(self.sender().text())

    def restart(self):
        x = 13
        y = 9
        for i in range(y):
            for j in range(x):
                self.bts[i][j].setStyleSheet('QPushButton {background-color: ' + self.colors[0] + ';}')
                if self.bts[i][j].text() == '0':
                    self.bts[i][j].setStyleSheet('QPushButton {background-color: white; color: white;}')


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('PixelArt')

    def show_window_1(self):
        self.w1 = Window1()
        self.w1.psem.clicked.connect(self.show_psem)
        self.w1.psem.clicked.connect(self.w1.close)
        self.w1.parrot.clicked.connect(self.show_parrot)
        self.w1.parrot.clicked.connect(self.w1.close)
        self.w1.heart.clicked.connect(self.show_heart)
        self.w1.heart.clicked.connect(self.w1.close)
        self.w1.cool.clicked.connect(self.show_cool)
        self.w1.cool.clicked.connect(self.w1.close)
        self.w1.ok.clicked.connect(self.show_ok)
        self.w1.ok.clicked.connect(self.w1.close)
        self.w1.show()

    def show_psem(self):
        self.w2 = Psem()
        self.w2.show()
        self.close()
        
    def show_parrot(self):
        self.w2 = Papug()
        self.w2.show()
        self.close()
        
    def show_heart(self):
        self.w2 = Heart()
        self.w2.show()
        self.close()
        
    def show_cool(self):
        self.w2 = Cool()
        self.w2.show()
        self.close()
        
    def show_ok(self):
        self.w2 = Ok()
        self.w2.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window1()
    w.show()
    sys.exit(app.exec_())
