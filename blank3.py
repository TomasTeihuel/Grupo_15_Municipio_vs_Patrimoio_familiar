import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, \
    QPushButton, \
    QDialog, QDialogButtonBox, QMessageBox, QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont
from random import randint

class MiniWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MiniWindow")
        self.setMinimumSize(200, 100)
        self.topParent = a0
        self.index = 0
        QBtn = QDialogButtonBox.StandardButton.Ok 
        self.button = QDialogButtonBox(QBtn)
        self.button.accepted.connect(self.accept)
        self.button.rejected.connect(self.reject)
        self.main_layout = QVBoxLayout()
        self.layout = QGridLayout()
        self.entry0 = QLineEdit("0")
        self.entry1 = QLineEdit("0")
        self.entry2 = QLineEdit("0")
        self.entry3 = QLineEdit("0")
        self.layout.addWidget(QLabel("Atributo 1"), 0, 0)
        self.layout.addWidget(QLabel("Atributo 2"), 1, 0)
        self.layout.addWidget(QLabel("Atributo 3"), 2, 0)
        self.layout.addWidget(QLabel("Atributo 4"), 3, 0)
        self.layout.addWidget(self.entry0, 0, 1)
        self.layout.addWidget(self.entry1, 1, 1)
        self.layout.addWidget(self.entry2, 2, 1)
        self.layout.addWidget(self.entry3, 3, 1)
        self.main_layout.addWidget(QLabel("Ingresa los datos:"))
        self.main_layout.addLayout(self.layout)
        self.main_layout.addWidget(self.button)
        self.setLayout(self.main_layout)
        
    def setData(self):
        res = ""
        res += "Atributo1: " + self.entry0.text() + "\n"
        res += "Atributo2: " + self.entry1.text() + "\n"
        res += "Atributo3: " + self.entry2.text() + "\n"
        res += "Atributo4: " + self.entry3.text()
        if self.index == 0:
            self.topParent.atribute0.setText(res)
        else:
            self.topParent.atribute1.setText(res)
class objText:
    def __init__(self, aux: list):
        pass


class myWindow(QMainWindow):

    def setDarkMode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0 + amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")
