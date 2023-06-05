# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:03:15 2023

@author: piwko
"""
# import os
# os.environ["PYTHONPATH"] = "."
from widgets.sliders import SliderWidget
from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QHBoxLayout, QLabel, QGridLayout, QWidget
import sys


class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_window_layout = QGridLayout()
        self.sliders = SliderWidget(self)
        self.sliders.SLIDERS_SIGNAL.connect(self.__update_color)

        self.color_label = QLabel(self)
        self.color_label.setText("0, 0, 0")

        self.main_window_layout.addWidget(self.sliders, 0, 0)
        self.main_window_layout.addWidget(self.color_label, 1, 0)

        self.widget = QWidget()
        self.widget.setLayout(self.main_window_layout)
        self.setCentralWidget(self.widget)

    # def slider_position(self, v):
    #     print("Slider est à :", v)

    def __update_color(self, red: int, green: int, blue: int) -> None:
        """_summary_

        Args:
            red (int): _description_
            green (int): _description_
            blue (int): _description_
        """
        self.color_label.setText(f"{red}, {green}, {blue}")


if __name__ == "__main__":
    app = QCoreApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    window = Fenetre()
    window.setWindowTitle("Générateur de couleurs")
    window.show()
    app.exec_()
