import sys
from PyQt6 import uic
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QPushButton,
    QLineEdit, QSizePolicy, QFileDialog
)
from PyQt6.QtGui import (
    QPixmap
)
import os

Form, Window = uic.loadUiType(
    "./redimencionar_imagem_qtdesing/design/design.ui")


class App(QMainWindow, Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnSelectImage.clicked.connect(self.open_img)
        self.btnResizeImage.clicked.connect(self.resize_img)
        self.btnSaveImage.clicked.connect(self.save)

    def open_img(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralWidget(),
            'Abri imagem',
            "\\",
            # options=QFileDialog.DontUseNativeDialog
        )
        self.inputPathImage.setText(image)
        self.original_img = QPixmap(image)
        self.labelImg.setPixmap(self.original_img)
        self.inputWidth.setText(str(self.original_img.width()))
        self.inputHeight.setText(str(self.original_img.height()))

    def resize_img(self):

        width = int(self.inputWidth.text())
        self.new_image = self.original_img.scaledToWidth(width)
        self.labelImg.setPixmap(self.new_image)
        self.inputWidth.setText(str(self.new_image.width()))
        self.inputHeight.setText(str(self.new_image.height()))

    def save(self):
        root, extension = os.path.splitext(self.inputPathImage.text())
        root = '/'.join(root.split('/')[0:-1])
        new_root, _ = QFileDialog.getSaveFileName(
            self.centralWidget(),
            'Salvar Imagem',
            f'{root}'
        )
        self.new_image.save(new_root+extension, 'PNG')


if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec()
