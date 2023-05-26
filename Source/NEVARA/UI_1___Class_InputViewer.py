from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QLabel, QDoubleSpinBox, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout
from mainVariables import default_Rotor_data as dr,rotorDataArray
from Aero____Class_CycloRotor import cycloRotor
from UI_2___Class_PlotViewer import TabWidgetPlots

class InputWidget(QWidget):
    def __init__(self,tab_widget_main):
        super().__init__()


        # Set tab widget
        self.tab_widget_main = tab_widget_main

        # main_rod       - 0
        # chord_rod      - 1
        # secondary_rods - 2
        # eccentric_rod  - 3
        # blade_name     - 4
        # blade_number   - 5
        # true_chord     - 6
        # Span_length    - 7
        # RPM            - 8

        # Create labels
        label1 = QLabel('Main Link(m):')
        label2 = QLabel('Chord Link(m):')
        label3 = QLabel('Secondary Link(m):')
        label4 = QLabel('Eccentricity Link(m):')
        label5 = QLabel('Aerofoil:')
        label6 = QLabel('Number of Blades:')
        label7 = QLabel('Chord Length(m):')
        label8 = QLabel('Span Length(m):')
        label9 = QLabel('RPM:')

        #Inputs
        self.input1 = QDoubleSpinBox()
        self.input2 = QDoubleSpinBox()
        self.input3 = QDoubleSpinBox()
        self.input4 = QDoubleSpinBox()
        self.input7 = QDoubleSpinBox()
        self.input8 = QDoubleSpinBox()
        self.input9 = QDoubleSpinBox()

        #Input Defaults
        self.input1.setMaximum(10)
        self.input1.setDecimals(4)
        self.input1.setValue(dr[0])

        self.input2.setMaximum(10)
        self.input2.setDecimals(4)
        self.input2.setValue(dr[1])

        self.input3.setMaximum(10)
        self.input3.setDecimals(4)
        self.input3.setValue(dr[2])

        self.input4.setMaximum(10)
        self.input4.setDecimals(4)
        self.input4.setValue(dr[3])

        self.input7.setMaximum(10)
        self.input7.setDecimals(4)
        self.input7.setValue(dr[6])

        self.input8.setMaximum(10)
        self.input8.setDecimals(4)
        self.input8.setValue(dr[7])

        self.input9.setMaximum(10000)
        self.input9.setDecimals(1)
        self.input9.setValue(dr[8])


        #Dropdown Aerofoil
        self.input5 = QComboBox()
        self.input5.addItem('NACA0012')
        self.input5.addItem('NACA0015')
        self.input5.addItem('NACA0016')

        self.input6 = QComboBox()
        self.input6.addItem('6')
        self.input6.addItem('4')
        self.input6.addItem('3')

        #Calculate Button
        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate)

        #Input Layout
        input_layout = QVBoxLayout()
        input_layout.addWidget(label1)
        input_layout.addWidget(self.input1)
        input_layout.addWidget(label2)
        input_layout.addWidget(self.input2)
        input_layout.addWidget(label3)
        input_layout.addWidget(self.input3)
        input_layout.addWidget(label4)
        input_layout.addWidget(self.input4)
        input_layout.addWidget(label5)
        input_layout.addWidget(self.input5)
        input_layout.addWidget(label6)
        input_layout.addWidget(self.input6)
        input_layout.addWidget(label7)
        input_layout.addWidget(self.input7)
        input_layout.addWidget(label8)
        input_layout.addWidget(self.input8)
        input_layout.addWidget(label9)
        input_layout.addWidget(self.input9)
        input_layout.addWidget(self.calculate_button)

        #Widget Layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)
        self.setLayout(main_layout)



    def calculate(self):
        rotorDataArray = [self.input1.value(),self.input2.value(),self.input3.value(),self.input4.value(),self.input5.currentText(),self.input6.currentText(),self.input7.value(),self.input8.value(),self.input9.value()]
        rotor = cycloRotor(rotorDataArray)

        #Add new plot to tab widget
        self.plot_widget = TabWidgetPlots(rotor)
        self.tab_widget_main.addTab(self.plot_widget,  f'Plot {self.tab_widget_main.count()+1}')