#Grupo 15: Municipio vs Patrimonio Familiar 
# Dante Farfan - Tomás Teihuel - Joaquin Lespai - Andres Vera - Ricardo Angulo 
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, \
    QPushButton, \
    QDialog, QDialogButtonBox, QMessageBox, QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QColor, QFont, QMouseEvent
from random import randint


class MiniWindow(QDialog):
    def __init__(self, a0: QMainWindow):
        super().__init__()
        self.setWindowTitle("MiniWindow")
        self.setMinimumSize(200, 100)
        self.topParent = a0
        self.index = 0
        QBtn = QDialogButtonBox.StandardButton.Ok
        self.button = QDialogButtonBox(QBtn)
        self.button.clicked.connect(self.setData)
        self.button.accepted.connect(self.accept)
        self.main_layout = QVBoxLayout()
        self.layout = QGridLayout()
        self.entry0 = QLineEdit("0")
        self.entry1 = QLineEdit("0")
        self.entry2 = QLineEdit("0")
        self.entry3 = QLineEdit("0")
        self.layout.addWidget(QLabel("Atributo 1"), 0, 0)
        self.layout.addWidget(self.entry0, 0, 1)
        self.main_layout.addWidget(QLabel("Ingresa los datos:"))
        self.main_layout.addLayout(self.layout)
        self.main_layout.addWidget(self.button)
        self.setLayout(self.main_layout)
        
         def setData(self):
        res = ""
        res += "Atributo1: " + self.entry0.text()
        if self.index == 0:
            self.topParent.list0 = [self.entry0.text()]
            aux = self.topParent.list0
            self.topParent.atribute0.setText(self.topParent.myUpdate(aux))
        else:
            self.topParent.list1 = [self.entry0.text()]
            aux = self.topParent.list1
            self.topParent.atribute1.setText(self.topParent.myUpdate(aux))


class Medida:
    def __init__(self, name, value, faction):
        self.name = name
        self.value = value
        if faction:  # True es Municipio y False es Patrimonio Familiar
            self.equi = value * 93239571.62
        else:
            self.equi = value * 647496.87


class myWindow(QMainWindow):

    def setDarkMode(self, a0, amount=50):
        dark_mode = QColor(0 + amount, 0 + amount, 0 + amount)
        a0.setStyleSheet(f"background-color: {dark_mode.name()}; color: white")

