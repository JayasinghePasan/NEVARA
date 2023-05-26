import sys
import numpy as np
from mainVariables import  beta, PI, colours
from sympy import *
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTabWidget
import pyqtgraph as pg
from coolTools import plot_symbolic_function
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDoubleSpinBox, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout
from mainVariables import default_Rotor_data as dr,rotorDataArray
from UI_2_1__Class_Geometry import Geom




class TabWidgetPlots(QWidget):
    def __init__(self,rot):
        super().__init__()
        self.initUI(rot)

    def initUI(self,rot):

        # Create a tab widget for displaying plots
        self.tab_widget = QtWidgets.QTabWidget()

        ##### TAB 0 - Geometry and FEA ####
        # self.tab_widget.addTab(Geom(rot),"Geometry")

        #### TAB 1 ####
        self.plot_tab_1 = QtWidgets.QWidget()
        self.plot_tab_1_layout = QtWidgets.QGridLayout(self.plot_tab_1)
        self.plot_tab_1_layout.setContentsMargins(0, 0, 0, 0)
        self.plot_tab_1_layout.setSpacing(0)
        self.tab_widget.addTab(self.plot_tab_1, str(rot.wingName))
        ##############################################################
        # plot 1.1 - Cl vs Attack Angle
        ##############################################################
        self.plot_tab_1_1 = pg.PlotWidget(title="Cl vs Attack Angle - "+ str(rot.wingName))
        self.plot_tab_1_1.showGrid(x=True, y= True)
        self.plot_tab_1_1.setLabel("bottom", "Attack Angle(deg)")
        self.plot_tab_1_1.setLabel("left", "Lift Coefficient")
        x_val, y_val = plot_symbolic_function(rot.CLFunctionBeta,min_deg=-20, max_deg=20)
        self.plot_tab_1_1.plot(x_val, y_val, pen='r')
        self.plot_tab_1_layout.addWidget(self.plot_tab_1_1, 0, 0, 1, 1)
        ##############################################################
        # plot 1.2 - Cd vs Attack Angle
        ##############################################################
        self.plot_tab_1_2 = pg.PlotWidget(title="Cd vs Attack Angle - "+ str(rot.wingName))
        self.plot_tab_1_2.showGrid(x=True, y= True)
        self.plot_tab_1_2.setLabel("bottom", "Attack Angle(deg)")
        self.plot_tab_1_2.setLabel("left", "Drag Coefficient")
        x_val, y_val = plot_symbolic_function(rot.CDFunctionBeta,min_deg=-20, max_deg=20)
        self.plot_tab_1_2.plot(x_val, y_val, pen='r')
        self.plot_tab_1_layout.addWidget(self.plot_tab_1_2, 1, 0, 1, 1)



        #### TAB 2 ####
        self.plot_tab_2 = pg.PlotWidget(title="Pitch vs Azimuth Angle")
        self.tab_widget.addTab(self.plot_tab_2, "Pitch-Az")
        self.plot_tab_2.showGrid(x=True, y= True)
        self.plot_tab_2.setLabel("bottom", "Azimuth Angle(deg)")
        self.plot_tab_2.setLabel("left", "Pitch Angle(deg)")
        x_val, y_val = plot_symbolic_function(rot.pitchAzimuthFunction)
        self.plot_tab_2.plot(x_val, y_val*180/np.pi, pen='r')



        #### TAB 3 ####
        self.plot_tab_3 = QtWidgets.QWidget()
        self.plot_tab_3_layout = QtWidgets.QGridLayout(self.plot_tab_3)
        self.plot_tab_3_layout.setContentsMargins(0, 0, 0, 0)
        self.plot_tab_3_layout.setSpacing(0)
        self.tab_widget.addTab(self.plot_tab_3, "C-Az")
        ##############################################################
        # plot 3.1 - Cl vs Azimuth Angle
        ##############################################################
        self.plot_tab_3_1 = pg.PlotWidget(title="Cl vs Azimuth Angle - "+ str(rot.wingName))
        self.plot_tab_3_1.showGrid(x=True, y= True)
        self.plot_tab_3_1.setLabel("bottom", "Azimuth Angle(deg)")
        self.plot_tab_3_1.setLabel("left", "Lift Coefficient")
        x_val, y_val = plot_symbolic_function(rot.CLFunctionPitch)
        self.plot_tab_3_1.plot(x_val, y_val, pen='r')
        self.plot_tab_3_layout.addWidget(self.plot_tab_3_1, 0, 0, 1, 1)
        ##############################################################
        # plot 3.2 - Cd vs Azimuth Angle
        ##############################################################
        self.plot_tab_3_2 = pg.PlotWidget(title="Cd vs Azimuth Angle - "+ str(rot.wingName))
        self.plot_tab_3_2.showGrid(x=True, y= True)
        self.plot_tab_3_2.setLabel("bottom", "Azimuth Angle(deg)")
        self.plot_tab_3_2.setLabel("left", "Drag Coefficient")
        x_val, y_val = plot_symbolic_function(rot.CDFunctionPitch)
        self.plot_tab_3_2.plot(x_val, y_val, pen='r')
        self.plot_tab_3_layout.addWidget(self.plot_tab_3_2, 1, 0, 1, 1)



        #### TAB 4 ####
        self.plot_tab_4 = QtWidgets.QWidget()
        self.plot_tab_4_layout = QtWidgets.QGridLayout(self.plot_tab_4)
        self.plot_tab_4_layout.setContentsMargins(0, 0, 0, 0)
        self.plot_tab_4_layout.setSpacing(0)
        self.tab_widget.addTab(self.plot_tab_4, "Thrust(s)")
        ##############################################################
        # plot 4.1 - Thrust-v(s) vs Azimuth Angle
        ##############################################################
        self.plot_tab_4_1 = pg.PlotWidget(title="Thrust-v(s) vs Azimuth Angle - "+ str(rot.wingName))
        self.plot_tab_4_1.showGrid(x=True, y= True)
        self.plot_tab_4_1.setLabel("bottom", "Azimuth Angle(deg)")
        self.plot_tab_4_1.setLabel("left", "Thrust-v(N)")
        x_val, y_val = plot_symbolic_function(rot.thrustVertical)
        self.plot_tab_4_1.plot(x_val, y_val, pen='r')
        self.plot_tab_4_layout.addWidget(self.plot_tab_4_1, 0, 0, 1, 1)
        ##############################################################
        # plot 4.2 - Thrust-h(s) vs Azimuth Angle
        ##############################################################
        self.plot_tab_4_2 = pg.PlotWidget(title="Thrust-h(s) vs Azimuth Angle - "+ str(rot.wingName))
        self.plot_tab_4_2.showGrid(x=True, y= True)
        self.plot_tab_4_2.setLabel("bottom", "Azimuth Angle(deg)")
        self.plot_tab_4_2.setLabel("left", "Thrust-h(N)")
        x_val, y_val = plot_symbolic_function(rot.thrustHorizontal)
        self.plot_tab_4_2.plot(x_val, y_val, pen='r')
        self.plot_tab_4_layout.addWidget(self.plot_tab_4_2, 1, 0, 1, 1)



        #### TAB 5 ####
        self.plot_tab_5 = pg.PlotWidget(title="Thrust-R(s) vs Azimuth Angle")
        self.tab_widget.addTab(self.plot_tab_5, "Thrust-R(s)")
        self.plot_tab_5.showGrid(x=True, y= True)
        self.plot_tab_5.setLabel("bottom", "Azimuth Angle(deg)")
        self.plot_tab_5.setLabel("left", "Thrust(N)")
        x_val, y_val = plot_symbolic_function(rot.thrustResultant)
        self.plot_tab_5.plot(x_val, y_val, pen='r')



        #### TAB 6 ####
        self.plot_tab_6 = QtWidgets.QWidget()
        self.plot_tab_6_layout = QtWidgets.QGridLayout(self.plot_tab_6)
        self.plot_tab_6_layout.setContentsMargins(0, 0, 0, 0)
        self.plot_tab_6_layout.setSpacing(0)
        self.tab_widget.addTab(self.plot_tab_6, "Thrust(a)")
        ##############################################################
        # plot 6.1 - Thrust-v(s) vs Azimuth Angle
        ##############################################################
        self.plot_tab_6_1 = pg.PlotWidget(title="Thrust-v(a) vs Azimuth Angle - "+ str(rot.wingName))
        self.plot_tab_6_1.showGrid(x=True, y= True)
        self.plot_tab_6_1.setLabel("bottom", "Azimuth Angle(deg)")
        self.plot_tab_6_1.setLabel("left", "Thrust-h(N)")
        x_val, y_val = plot_symbolic_function(rot.totalThrustVertical)
        self.plot_tab_6_1.plot(x_val, y_val, pen='r')
        for wingNo in range(rot.bladeNumber):
            beta = symbols('beta')
            x_val, y_val = plot_symbolic_function(rot.thrustVertical.subs(beta, beta + wingNo * 2 * PI / rot.bladeNumber))
            self.plot_tab_6_1.plot(x_val, y_val, pen=colours[wingNo])
        self.plot_tab_6_layout.addWidget(self.plot_tab_6_1, 0, 0, 1, 1)
        ##############################################################
        # plot 6.2 - Thrust-h(s) vs Azimuth Angle
        ##############################################################
        self.plot_tab_6_2 = pg.PlotWidget(title="Thrust-h(a) vs Azimuth Angle - "+ str(rot.wingName))
        self.plot_tab_6_2.showGrid(x=True, y= True)
        self.plot_tab_6_2.setLabel("bottom", "Azimuth Angle(deg)")
        self.plot_tab_6_2.setLabel("left", "Thrust-v(N)")
        x_val, y_val = plot_symbolic_function(rot.totalThrustHorizontal)
        self.plot_tab_6_2.plot(x_val, y_val, pen='r')
        for wingNo in range(rot.bladeNumber):
            beta = symbols('beta')
            x_val, y_val = plot_symbolic_function(rot.thrustHorizontal.subs(beta, beta + wingNo * 2 * PI / rot.bladeNumber))
            self.plot_tab_6_2.plot(x_val, y_val, pen=colours[wingNo])
        self.plot_tab_6_layout.addWidget(self.plot_tab_6_2, 1, 0, 1, 1)



        #### TAB 7 ####
        self.plot_tab_7 = pg.PlotWidget(title="Thrust-R(a) vs Azimuth Angle")
        self.tab_widget.addTab(self.plot_tab_7, "Thrust-R(a)")
        self.plot_tab_7.showGrid(x=True, y= True)
        self.plot_tab_7.setLabel("bottom", "Azimuth Angle(deg)")
        self.plot_tab_7.setLabel("left", "Thrust(N)")
        x_val, y_val = plot_symbolic_function(rot.totalThrustResultant)
        self.plot_tab_7.plot(x_val, y_val, pen='r')
        self.plot_tab_7.setYRange(0,max(y_val))


        #### TAB LAST - DATA ####
        dataTablayout = QVBoxLayout()
        label1 = QLabel('Main Link(m):          ' + str (rot.main))
        label2 = QLabel('Chord Link(m):         ' + str (rot.chordLink))
        label3 = QLabel('Secondary Link(m):     ' + str (rot.secondryLink))
        label4 = QLabel('Eccentricity Link(m):  ' + str (rot.eccentry))
        label5 = QLabel('Aerofoil:              ' + str (rot.wingName))
        label6 = QLabel('Number of Blades:      ' + str (rot.bladeNumber))
        label7 = QLabel('Chord Length(m):       ' + str (rot.trueChord))
        label8 = QLabel('Span Length(m):        ' + str (rot.spanLength))
        label9 = QLabel('RPM:                   ' + str (rot.RPM))
        dataTablayout.addWidget(label1)
        dataTablayout.addWidget(label2)
        dataTablayout.addWidget(label3)
        dataTablayout.addWidget(label4)
        dataTablayout.addWidget(label5)
        dataTablayout.addWidget(label6)
        dataTablayout.addWidget(label7)
        dataTablayout.addWidget(label8)
        dataTablayout.addWidget(label9)

        self.dataTab = QtWidgets.QWidget()
        self.dataTab.setLayout(dataTablayout)
        self.tab_widget.addTab(self.dataTab, "Data")


        #Layout
        self.tab_widget_layout = QtWidgets.QVBoxLayout()
        self.tab_widget_layout.addWidget(self.tab_widget)

        #Close button
        close_button = QPushButton('Close')
        close_button.clicked.connect(self.close)
        self.tab_widget_layout.addWidget(close_button)
        self.setLayout(self.tab_widget_layout)

    def close(self):
        parent_widget = self.parent()
        if isinstance(parent_widget, QTabWidget):
            parent_widget.removeTab(parent_widget.indexOf(self))
        else:
            parent_widget.removeWidget(self)

