# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:05:14 2023

@author: piwko
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QStatusBar, QSlider, QHBoxLayout, QLabel, QGridLayout, QWidget, QToolBar
from PyQt5.QtCore import Qt, QCoreApplication, pyqtSignal
from PyQt5.QtGui import QIcon, QKeySequence

class menus(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setMinimumWidth(600)
        self.setMinimumHeight(300)
        
        self.action1 = QAction(QIcon("arrow-reinit.png"), "Réinitialiser", self)
        self.action2 = QAction(QIcon("palette.png"), "Réinitialiser la palette", self)
        self.action3 = QAction(QIcon("flag-red.png"), "Filtre rouge", self)
        #self.action3.setStatusTip("C'est le troisième bouton")
        #self.action3.triggered.connect(self.onMyToolBarButtonClick)
        self.action4 = QAction(QIcon("flag-green.png"), "Filtre vert", self)
        self.action5 = QAction(QIcon("flag-blue.png"), "Filtre bleu", self)
        self.action6 = QAction(QIcon("flag-negatif.png"), "Négatif", self)
        self.action7 = QAction(QIcon("flag-grey.png"), "Gris", self)
        self.action8 = QAction(QIcon("doc-save.png"), "Sauvegarder", self)
        
        self.action1.setShortcut(QKeySequence("Ctrl+D"))
        self.action2.setShortcut(QKeySequence("Ctrl+P"))
        self.action3.setShortcut(QKeySequence("Ctrl+R"))
        self.action4.setShortcut(QKeySequence("Ctrl+V"))
        self.action5.setShortcut(QKeySequence("Ctrl+B"))
        self.action6.setShortcut(QKeySequence("Ctrl+N"))
        self.action7.setShortcut(QKeySequence("Ctrl+G"))
        self.action8.setShortcut(QKeySequence("Ctrl+S"))
        
        
        
        self.setStatusBar(QStatusBar())
        
        self.menuGrille = self.menuBar().addMenu("Grille")
        self.menuGrille.addAction(self.action1)
        self.menuGrille.addSeparator()
        self.menuGrille.addAction(self.action2)
        
        self.menuFiltre = self.menuBar().addMenu("Filtre")
        self.menuFiltre.addAction(self.action3)
        self.menuFiltre.addAction(self.action4)
        self.menuFiltre.addAction(self.action5)
        self.menuFiltre.addSeparator()
        self.menuFiltre.addAction(self.action6)
        self.menuFiltre.addAction(self.action7)
        
        self.menuSauvegarder = self.menuBar().addMenu("Sauvegarder")
        self.menuSauvegarder.addAction(self.action8)
        
        self.menuQuitter = self.menuBar().addMenu("Quitter")
        
        
        self.toolbar = QToolBar("Barre d'outils")
        self.addToolBar(self.toolbar)
        
        self.toolbar.addAction(self.action1)
        self.toolbar.addAction(self.action2)
        self.toolbar.addAction(self.action3)
        self.toolbar.addAction(self.action4)
        self.toolbar.addAction(self.action5)
        self.toolbar.addAction(self.action6)
        self.toolbar.addAction(self.action7)
        self.toolbar.addAction(self.action8)

        
    def onMyToolBarButtonClick(self):
        print("click")

if __name__ == "__main__":
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = menus()
    window.setWindowTitle("Générateur de PixelArt")
    window.show()
    app.exec_()
