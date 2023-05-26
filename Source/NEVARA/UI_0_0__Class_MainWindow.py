import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, QPushButton, QLineEdit, QStatusBar
from PyQt5.QtGui import QIcon

from Aero____Class_CycloRotor import cycloRotor
from mainVariables import default_Rotor_data
from UI_2___Class_PlotViewer import TabWidgetPlots
from UI_1___Class_InputViewer import InputWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #Window properties
        self.setWindowTitle('NEVARA CYCLOR Tools')
        self.setWindowIcon(QIcon('drone.png'))

        #Status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('CycloRotor Computational Model Version 3.0.1 - Nevara (04.14.2022)')

        self.tab_widget_rotors = QTabWidget()
        self.input_widget = InputWidget(self.tab_widget_rotors)

        #Colour Palate
        self.setStyleSheet('''
            QMainWindow {
                background-color: #3B4542;
                font-family: 'Roboto', sans-serif;
            }
            QTabWidget::pane {
                border: none;
                background-color: #5A6965;
            }
            QTabBar::tab {
                background-color: #4B574A;
                color: #ffffff;
                padding: 10px;

            }
            QTabBar::tab:selected {
                background-color: #478232;
                color: #ffffff;
            }
            QLabel {
                color: #ffffff;
            }
        ''')

        #Layout
        layout = QHBoxLayout()
        layout.addWidget(self.input_widget)
        layout.addWidget(self.tab_widget_rotors)

        #Main WIndow
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setGeometry(100, 100, 1200, 800)





