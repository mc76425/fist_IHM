# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:03:15 2023

@author: piwko
"""

from PyQt5.QtWidgets import QSlider, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import Qt, pyqtSignal


class SliderWidget(QWidget):
    # Create cutom signal to notifiy slider's change in main window
    SLIDERS_SIGNAL = pyqtSignal([int, int, int])

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Générateur de couleurs")

        # self.main_window_layout = QGridLayout()
        self.__slider_layout = QGridLayout()
        self.setLayout(self.__slider_layout)

        self.__slider1 = QSlider(Qt.Horizontal)
        self.__slider2 = QSlider(Qt.Horizontal)
        self.__slider3 = QSlider(Qt.Horizontal)

        self.__slider1.setMinimum(0)
        self.__slider1.setMaximum(255)

        self.__slider2.setMinimum(0)
        self.__slider2.setMaximum(255)

        self.__slider3.setMinimum(0)
        self.__slider3.setMaximum(255)

        self.__slider_layout.addWidget(self.__slider1, 0, 0)
        self.__slider_layout.addWidget(self.__slider2, 1, 0)
        self.__slider_layout.addWidget(self.__slider3, 2, 0)

        self.__slider1_label_color = QLabel(self)
        self.__slider1_label_color.setText("Rouge")
        self.__slider1_label_color.setStyleSheet(
            'color: red; background-color: None')
        self.__slider2_label_color = QLabel(self)
        self.__slider2_label_color.setText("Vert")
        self.__slider2_label_color.setStyleSheet(
            'color: green; background-color: None')
        self.__slider3_label_color = QLabel(self)
        self.__slider3_label_color.setText("Bleu")
        self.__slider3_label_color.setStyleSheet(
            'color: blue; background-color: None')

        self.__slider_layout.addWidget(self.__slider1_label_color, 0, 1)
        self.__slider_layout.addWidget(self.__slider2_label_color, 1, 1)
        self.__slider_layout.addWidget(self.__slider3_label_color, 2, 1)

        self.__slider1.valueChanged.connect(self.__update_label_red_value)
        self.__slider2.valueChanged.connect(self.__update_label_green_value)
        self.__slider3.valueChanged.connect(self.__update_label_blue_value)

    def get_positions(self):
        """_summary_

        Returns:
            tuple: RGB values from sliders positions
        """
        return (self.__slider1.value(), self.__slider2.value(), self.__slider3.value())

    def __update_label_red_value(self, value: int) -> None:
        """update label red string

        Args:
            value (int): slider one position
        """
        if value == 0:
            self.__slider1_label_color.setText("Rouge")
        else:
            self.__slider1_label_color.setText(str(value))

        self.SLIDERS_SIGNAL.emit(self.__slider1.value(
        ), self.__slider2.value(), self.__slider3.value())

    def __update_label_green_value(self, value: int) -> None:
        """update label green string

        Args:
            value (int): slider one position
        """
        if value == 0:
            self.__slider2_label_color.setText("Vert")
        else:
            self.__slider2_label_color.setText(str(value))

        self.SLIDERS_SIGNAL.emit(self.__slider1.value(
        ), self.__slider2.value(), self.__slider3.value())

    def __update_label_blue_value(self, value: int) -> None:
        """update label blue string

        Args:
            value (int): slider one position
        """
        if value == 0:
            self.__slider3_label_color.setText("Bleu")
        else:
            self.__slider3_label_color.setText(str(value))

        self.SLIDERS_SIGNAL.emit(self.__slider1.value(
        ), self.__slider2.value(), self.__slider3.value())
