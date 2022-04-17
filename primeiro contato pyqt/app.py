import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QPushButton


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do botão')
        self.btn.setStyleSheet('font-size: 16px')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)

        self.btn.clicked.connect(self.action)

        self.setCentralWidget(self.cw)

    def action(self):
        print('Olá Mundo!!')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec()
