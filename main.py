# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:03:15 2023

@author: piwko
"""
# import os
# os.environ["PYTHONPATH"] = "."
#from widgets.sliders import SliderWidget
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QWidget, QAction, QStatusBar, QToolBar, QPushButton, QComboBox, QMessageBox
from PyQt5.QtGui import QIcon, QKeySequence
import sys



class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()

##################################################################
# menus et toolbar
        self.setMinimumWidth(600)
        self.setMinimumHeight(300)
        
        self.action1 = QAction(QIcon("icones\\arrow-reinit.png"), "Réinitialiser", self)
        self.action2 = QAction(QIcon("icones\\palette.png"), "Réinitialiser la palette", self)
        self.action3 = QAction(QIcon("flag-red.png"), "Filtre rouge (fonctionnel)", self)
        #self.action3.setStatusTip("C'est le troisième bouton")
        #self.action3.triggered.connect(self.onMyToolBarButtonClick)
        self.action4 = QAction(QIcon("icones/flag-green.png"), "Filtre vert (fonctionnel)", self)
        self.action5 = QAction(QIcon("icones/flag-blue.png"), "Filtre bleu (fonctionnel)", self)
        self.action6 = QAction(QIcon("icones/flag-negatif.png"), "Négatif", self)
        self.action7 = QAction(QIcon("icones/flag-grey.png"), "Gris", self)
        self.action8 = QAction(QIcon("icones/doc-save.png"), "Sauvegarder", self)
        self.action9 = QAction(QIcon("icones/doc-quit.png"), "Quitter", self)
        self.action10 = QAction(QIcon("icones/doc-charger.png"), "Charger", self)
        
        self.action1.setShortcut(QKeySequence("Ctrl+D"))
        self.action2.setShortcut(QKeySequence("Ctrl+P"))
        self.action3.setShortcut(QKeySequence("Ctrl+R"))
        self.action4.setShortcut(QKeySequence("Ctrl+V"))
        self.action5.setShortcut(QKeySequence("Ctrl+B"))
        self.action6.setShortcut(QKeySequence("Ctrl+N"))
        self.action7.setShortcut(QKeySequence("Ctrl+G"))
        self.action8.setShortcut(QKeySequence("Ctrl+S"))
        self.action9.setShortcut(QKeySequence("Ctrl+Q"))
        
        
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
        
        self.menuEffets = self.menuBar().addMenu("Effets")
        
        self.menuSauvegarder = self.menuBar().addMenu("Sauvegarder")
        self.menuSauvegarder.addAction(self.action8)
        self.menuSauvegarder.addAction(self.action10)
        
        self.menuQuitter = self.menuBar().addMenu("Quitter")
        self.menuQuitter.addAction(self.action9)
        
        
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
        self.toolbar.addAction(self.action9)
        self.toolbar.addAction(self.action10)

##################################################################

        self.main_window_layout = QGridLayout()
        self.sliders = SliderWidget(self)
        self.sliders.SLIDERS_SIGNAL.connect(self.__update_color)

        self.color_label = QLabel(self)
        self.color_label.setText("Ma couleur")
        self.color_label.setAlignment(Qt.AlignCenter)

        #self.main_window_layout.addWidget(self.sliders, 0, 0)
        #self.main_window_layout.addWidget(self.color_label, 1, 0)

        self.widget = QWidget()
        self.widget.setLayout(self.main_window_layout)
        self.setCentralWidget(self.widget)

    # def slider_position(self, v):
    #     print("Slider est à :", v)
    
##################################################################
# grille
        self.grid = QGridLayout()
        self.grid.setSpacing(5)
        self.buttons_base = []
        for i in range(9):
            for j in range(9):
                self.wg = QPushButton()
                self.wg.clicked.connect(self.set_color2)#######################
                self.wg.setMinimumWidth(50)
                self.wg.setMinimumHeight(50)
                self.wg.setStyleSheet("background-color: white")
                self.buttons_base.append(self.wg)
                self.grid.addWidget(self.wg,i,j)
                
        self.wg = QWidget()
        self.wg.setLayout(self.grid)
        self.main_window_layout.addWidget(self.wg, 2, 1)
##################################################################
# widgets manquants et leur organisation

# "COULEURS" et "GRILLE" en (1,0) et (1,1)
        self.COULEURS = QLabel("COULEURS")
        self.main_window_layout.addWidget(self.COULEURS, 1, 0)
        self.GRILLE = QLabel("GRILLE")
        self.main_window_layout.addWidget(self.GRILLE, 1, 1)
            
        
#partie verticale de gauche : QVBoxLayout en (2,0)
        self.vertical = QVBoxLayout()
        self.gridc = QGridLayout()
        self.gridc.setSpacing(5)
        rainbow = [["red","green"],
                   ["blue","yellow"],
                   ["orange","violet"],
                   ["pink","turquoise"],
                   ["gray","brown"]] # pour la palette prédéfinie
        for i in range(5):
            for j in range(2):
                self.wc = QPushButton()
                self.wc.clicked.connect(self.apply_color)####################OK
                self.wc.clicked.connect(self.get_color2)#####################OK
                self.wc.setStyleSheet(f"background-color: {rainbow[i][j]}")
                self.gridc.addWidget(self.wc,i,j)
        self.wc = QWidget()
        self.wc.setLayout(self.gridc)
        
        self.AJC = QPushButton("AJOUTER COULEUR A LA PALETTE")
        self.AJC.clicked.connect(self.demande)
        self.AJC.clicked.connect(self.select_color)##########################OK
        
        self.vertical.addWidget(self.wc)
        self.vertical.addWidget(self.sliders) #vient de plus haut
        self.vertical.addWidget(self.color_label) #vient de plus haut
        self.vertical.addWidget(self.AJC)
        
        self.widgeth = QWidget()
        self.widgeth.setLayout(self.vertical)
        self.main_window_layout.addWidget(self.widgeth, 2, 0)

#partie du coin : QLabel en (0,0)        
        self.OUTILS = QLabel("OUTILS")
        self.main_window_layout.addWidget(self.OUTILS, 0, 0)
        
#partie horizontale du haut : en (0,1)
        self.horizontal = QHBoxLayout()
        self.H_outil = QComboBox()
        self.H_outil.currentIndexChanged.connect(self.tool_changed)##########OK
        #self.H_outil.addItem("Choisissez votre outil") # pas besoin ...
        self.H_outil.addItem("Stylo")
        self.H_outil.addItem("Gomme")
        self.H_outil.addItem("Baguette")
        self.H_outil.addItem("Pot")

        self.Hcolordisplay = QLabel()
        self.Hprojet = QComboBox()
        self.Hprojet.addItem("projet")#########################################
        
        self.horizontal.addWidget(self.H_outil)
        self.horizontal.addWidget(self.Hcolordisplay)
        self.horizontal.addWidget(self.Hprojet)
        
        self.widgetv = QWidget()
        self.widgetv.setLayout(self.horizontal)
        self.main_window_layout.addWidget(self.widgetv, 0, 1)

##################################################################
#connexions des QAction
        self.action1.triggered.connect(self.onReset) # reset grille de dessin
        self.action2.triggered.connect(self.onResetPalette) # reset palette de couleur
        
        self.action3.triggered.connect(self.redFilter) # filtres de couleur
        self.action4.triggered.connect(self.greenFilter)
        self.action5.triggered.connect(self.blueFilter)
        #self.action6.triggered.connect(self.nFilter)
        #self.action7.triggered.connect(self.greyFilter)
        
        #self.action8.triggered.connect(self.onSave) # sauvegarder
        self.action9.triggered.connect(self.onExit) # quitter
        
        self.action10.triggered.connect(self.charger_projet)
##################################################################
# SAUVEGARDE
    def onSave(self):
        projet = []
        for row in range(self.grid.rowCount()):
            ligne = []
            for col in range(self.grid.columnCount()):
                button = self.grid.itemAtPosition(row, col).widget()
                couleur = button.palette().color(button.backgroundRole()).name()
                ligne.append(couleur)
            projet.append(ligne)

        nom_projet = self.Hprojet.currentText()  # Obtenir le nom du projet à partir de la QComboBox
        fichier = f"{nom_projet}.json"  # Utiliser le nom du projet comme nom de fichier

        with open(fichier, 'w') as f:
            json.dump(projet, f)

    def charger_projet(self):
        #nom_projet = self.Hprojet.currentText()  # Obtenir le nom du projet sélectionné dans la QComboBox
        #fichier = f"{nom_projet}.json"  # Utiliser le nom du projet pour trouver le fichier
        fichier = "projet.json"
        with open(fichier, 'r') as f:
            projet = json.load(f)

        # Effacer les boutons existants dans le QGridLayout
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)

        # Recréer les boutons avec les couleurs du projet chargé
        for row, ligne in enumerate(projet):
            for col, couleur in enumerate(ligne):
                button = QPushButton()
                button.setStyleSheet(f"background-color: {couleur};")
                self.grid.addWidget(button, row, col)

##################################################################
# QUITTER
    def onExit(self, event):
        reply = QMessageBox.question(self, "Confirmation", "Êtes-vous sûr de vouloir quitter ?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            app.quit()
        else:
            event.ignore()

##################################################################

# pour la demande de choix de l'emplacement sur la palette
    def demande(self):
        QMessageBox.information(self, 'Information', 'vous devez choisir un emplacement dans la palette')
##################################################################
# pour créer une pelette de couleurs rouge
    def redFilter(self):
        rainbow = [[0, 28], [57, 85], [113, 142], [170, 198], [227, 255]]
        for i in range(5):
            for j in range(2):
                self.wc = QPushButton()
                self.wc.clicked.connect(self.apply_color)####################OK
                self.wc.clicked.connect(self.get_color2)#####################OK
                self.wc.setStyleSheet(f"background-color: rgb({rainbow[i][j]},0,0)")
                self.gridc.addWidget(self.wc,i,j)
    def greenFilter(self):
        rainbow = [[0, 28], [57, 85], [113, 142], [170, 198], [227, 255]]
        for i in range(5):
            for j in range(2):
                self.wc = QPushButton()
                self.wc.clicked.connect(self.apply_color)####################OK
                self.wc.clicked.connect(self.get_color2)#####################OK
                self.wc.setStyleSheet(f"background-color: rgb(0,{rainbow[i][j]},0)")
                self.gridc.addWidget(self.wc,i,j)
    def blueFilter(self):
        rainbow = [[0, 28], [57, 85], [113, 142], [170, 198], [227, 255]]
        for i in range(5):
            for j in range(2):
                self.wc = QPushButton()
                self.wc.clicked.connect(self.apply_color)####################OK
                self.wc.clicked.connect(self.get_color2)#####################OK
                self.wc.setStyleSheet(f"background-color: rgb(0,0,{rainbow[i][j]})")
                self.gridc.addWidget(self.wc,i,j)
        
##################################################################
# outils et couleurs
    def tool_changed(self, index): # teste quel est l'état du QComboBox
        if self.H_outil.currentText() == "Stylo":  # "Stylo" sélectionné
            for button in self.buttons_base:
                button.clicked.connect(self.set_color2)
            self.disconnect_baguettesignals()
            self.disconnect_potsignals()
            self.disconnect_gommesignals()
        if self.H_outil.currentText() == "Gomme":
            for button in self.buttons_base:
                button.clicked.connect(self.gomme_set)
            self.disconnect_baguettesignals()
            self.disconnect_potsignals()
            self.disconnect_stylosignals()
        if self.H_outil.currentText() == "Baguette":
            for button in self.buttons_base:
                button.clicked.connect(self.baguette_magique)
            self.disconnect_potsignals()
            self.disconnect_stylosignals()
            self.disconnect_gommesignals()
        if self.H_outil.currentText() == "Pot":
            for button in self.buttons_base:
                button.clicked.connect(self.pot_magique)
            self.disconnect_baguettesignals()
            self.disconnect_stylosignals()
            self.disconnect_gommesignals()
    
    # utilisée dans tool_changed : permet de déconnecter les signaux de tous les boutons de la fonction baguette_magique
    def disconnect_baguettesignals(self):
        for button in self.buttons_base:
            button.clicked.disconnect(self.baguette_magique)
    def disconnect_potsignals(self):
        for button in self.buttons_base:
            button.clicked.disconnect(self.pot_magique)
    def disconnect_stylosignals(self):
        for button in self.buttons_base:
            button.clicked.disconnect(self.baguette_magique)
    def disconnect_gommesignals(self):
        for button in self.buttons_base:
            button.clicked.disconnect(self.pot_magique)

    def get_color2(self):
        sender_button = self.sender()
        background_color = sender_button.palette().color(sender_button.backgroundRole())
        self.color_label.setStyleSheet(f"background-color: {background_color.name()}")
        # ligne en plus pour l'apperçu de la couleur en haut
        self.Hcolordisplay.setStyleSheet(f"background-color: {background_color.name()};")
    
    def set_color2(self):
        sender_button = self.sender()
        background_color = self.color_label.palette().color(self.color_label.backgroundRole())
        sender_button.setStyleSheet(f"background-color: {background_color.name()}")

# gomme et fonctionnement
    def gomme_set(self):
        sender_button = self.sender()# Récupérer le bouton qui a émis le signal
        sender_button.setStyleSheet("background-color: white") # Réinitialiser le fond du bouton en blanc
        
# baguette fonctionnement
    def baguette_magique(self):
        sender_button = self.sender()
        background_color_bm = sender_button.palette().color(sender_button.backgroundRole())
        self.color_label.setStyleSheet(f"background-color: {background_color_bm.name()}")
        # ligne en plus pour l'apperçu de la couleur en haut
        self.Hcolordisplay.setStyleSheet(f"background-color: {background_color_bm.name()};")
        for row in range(self.grid.rowCount()):
            for column in range(self.grid.columnCount()):
                widget = self.grid.itemAtPosition(row, column).widget()
                specific_color_bm = widget.palette().color(widget.backgroundRole()) # Obtenez la couleur de background du bouton
                if specific_color_bm == background_color_bm: # Vérifiez si la couleur de background correspond à la couleur spécifique souhaitée
                    widget.setStyleSheet("background-color: white") # Mettez le fond en blanc pour les boutons ayant cette couleur
       
# pot fonctionnement
    def pot_magique(self):
        sender_button = self.sender()
        background_color_p = sender_button.palette().color(sender_button.backgroundRole())
        self.color_label.setStyleSheet(f"background-color: {background_color_p.name()}")
        # ligne en plus pour l'apperçu de la couleur en haut
        self.Hcolordisplay.setStyleSheet(f"background-color: {background_color_p.name()};")
        for row in range(self.grid.rowCount()):
            for column in range(self.grid.columnCount()):
                widget = self.grid.itemAtPosition(row, column).widget()
                specific_color_p = widget.palette().color(widget.backgroundRole())
                print(specific_color_p.name())
                if specific_color_p.name() == "#ffffff" or specific_color_p is None:
                    widget.setStyleSheet(f"background-color: {background_color_p.name()}")
        
# ajout d'une couleur à la palette suivant celle-ci
    def select_color(self):
        self.selected_color = self.color_label.palette().color(self.color_label.backgroundRole())
    '''def select_color(self):
        color_dialog = self.color_label.text()
        self.selected_color = color_dialog'''

    def apply_color(self):
        # Récupérer le bouton qui a émis le signal
        sender_button = self.sender()
        if sender_button.property("colorApplied") is None:
            # Convertir la couleur en une chaîne de format CSS
            color_string = self.selected_color.name()
            # Appliquer la couleur sélectionnée au bouton
            sender_button.setStyleSheet(f"background-color: {color_string}")
            # Ajouter une propriété au bouton pour indiquer que la couleur a été appliquée
            sender_button.setProperty("colorApplied", True)
    '''def apply_color(self):
        # Récupérer le bouton qui a émis le signal
        sender_button = self.sender()
        if self.selected_color is not None:
            # Appliquer la couleur sélectionnée au bouton
            sender_button.setStyleSheet(f"background-color: {self.selected_color}")'''
            
##################################################################
# reset_grille et reset_palette
    def onReset(self):
        for row in range(self.grid.rowCount()): # déjà le bon QGridLayout : self.grid
            for column in range(self.grid.columnCount()):
                item = self.grid.itemAtPosition(row, column)
                if item is not None:
                    widget = item.widget()
                    widget.setStyleSheet("background-color: white")
                    
    def onResetPalette(self):
        rainbow = [["red","green"],
                   ["blue","yellow"],
                   ["orange","violet"],
                   ["pink","turquoise"],
                   ["gray","brown"]] # pour la palette prédéfinie
        for i in range(5):
            for j in range(2):
                self.wc = QPushButton()
                self.wc.clicked.connect(self.apply_color)####################OK
                self.wc.clicked.connect(self.get_color2)#####################OK
                self.wc.setStyleSheet(f"background-color: {rainbow[i][j]}")
                self.gridc.addWidget(self.wc,i,j)
    '''def reset_palette(self):
        for row in range(self.gridc.rowCount()): # déjà le bon QGridLayout : self.gridc
            for column in range(self.gridc.columnCount()):
                item = self.gridc.itemAtPosition(row, column)
                if item is not None:
                    widget = item.widget()
                    widget.setStyleSheet("") # Réinitialise la feuille de style du widget
                    widget.setProperty("colorApplied", None)  # Réinitialise la propriété "colorApplied"'''
                    
##################################################################

    def __update_color(self, red: int, green: int, blue: int) -> None:
        """_summary_

        Args:
            red (int): _description_
            green (int): _description_
            blue (int): _description_
        """
        self.color_label.setText(f"rgb({red}, {green}, {blue})")
        self.color_label.setStyleSheet(f"background: rgb({red}, {green}, {blue})")

##################################################################

if __name__ == "__main__":
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = Fenetre()
    window.setWindowTitle("Générateur de PixelArt")
    window.show()
    app.exec_()
