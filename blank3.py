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
        
    def __init__(self):
        super().__init__()

        # Sección de ventana y configuración general
        self.setWindowTitle("HeHe")
        self.setMinimumSize(400, 200)

        # Constructor
        self.button0 = QPushButton("Agregar Datos")
        self.button1 = QPushButton("Agregar Datos")
        self.button2 = QPushButton("Comparar")
        self.alt_window = MiniWindow(self)
        self.setDarkMode(self.alt_window)

        # Layout y reacción
        main_box = QVBoxLayout()
        box = QGridLayout()

        self.list0 = [1, 2, 3]
        self.atribute0 = QLabel(self.myUpdate(self.list0))
        self.list1 = [1, 2, 3]
        self.atribute1 = QLabel(self.myUpdate(self.list0))

        box.addWidget(QLabel("Objeto izquierda:"), 0, 0)
        box.addWidget(self.atribute0, 1, 0)
        box.addWidget(self.button0, 2, 0)
        box.addWidget(QLabel("><"), 1, 1)
        box.addWidget(QLabel("Objecto derecha"), 0, 2)
        box.addWidget(self.atribute1, 1, 2)
        box.addWidget(self.button1, 2, 2)

        main_box.addWidget(QLabel("Bienvenidos"))
        main_box.addLayout(box)
        main_box.addWidget(self.button2)

        self.button0.clicked.connect(lambda checked: self.push_reaction(self.alt_window, 0))
        self.button1.clicked.connect(lambda checked: self.push_reaction(self.alt_window, 1))
        self.button2.clicked.connect(lambda checked: self.compare)

        my_window = QWidget()
        my_window.setLayout(main_box)
        self.setDarkMode(my_window)
        self.setCentralWidget(my_window)

    def myUpdate(self, aux: list):
        res = ""
        for i in aux:
            res += str(i) + ", "
