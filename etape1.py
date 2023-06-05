# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:03:15 2023

@author: piwko
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QHBoxLayout, QLabel, QGridLayout, QWidget 
from PyQt5.QtCore import Qt, QCoreApplication

class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Générateur de couleurs")
        self.setFixedWidth(700)
        self.setFixedHeight(300)
        
        self.layout = QGridLayout()
        
        #slider1 = QGridLayout()
        slider1 = QSlider(Qt.Horizontal)
        slider1.setFixedWidth(500)
        slider1.setFixedHeight(30)
        slider1.setMinimum(0)
        slider1.setMaximum(255)
        #slider12 = QLabel('Rouge')
        #slider12.setStyleSheet('color: red')
        #slider1.addWidget(slider11,0,0)
        #slider1.addWidget(slider12,0,1)
        self.layout.addWidget(slider1,0,0)
        #slider1.sliderMoved.connect(self.slider_position)
        
        slider2 = QSlider(Qt.Horizontal)
        slider2.setFixedWidth(500)
        slider2.setFixedHeight(30)
        slider2.setMinimum(0)
        slider2.setMaximum(255)
        self.layout.addWidget(slider2,1,0)
        
        slider3 = QSlider(Qt.Horizontal)
        slider3.setMinimum(0)
        slider3.setMaximum(255)
        self.layout.addWidget(slider3,2,0)
        
        box = QLabel('a')
        box.setAlignment(Qt.AlignCenter)
        ...
        self.layout.addWidget(box,3,0)
        
        
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def slider_position(self, v):
        print("Slider est à :", v)

app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
window = Fenetre()
window.show()
app.exec_()