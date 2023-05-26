import numpy as np
import sympy as sp
from sympy import *

beta = symbols('beta')
PI = np.pi
airDensity = 1.225
colours = ["#1f77b4","#2ca02c","#9467bd","#ff7f0e","#8c564b","#FFFF00"]

# main_rod       - 0
# chord_rod      - 1
# secondary_rods - 2
# eccentric_rod  - 3
# blade_name     - 4
# blade_number   - 5
# true_chord     - 6
# Span_length    - 7
# RPM            - 8

default_Rotor_data =[(1.2192/2), 0.075, 0.6134, 0.0230, 'NACA0012', 6, 0.3048, 1.2192, 400]

rotorDataArray = []