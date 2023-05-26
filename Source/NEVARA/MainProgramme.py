import time
from mainVariables import rotorDataArray
from Aero____Class_CycloRotor import *
from PyQt5 import QtWidgets
from UI_0_0__Class_MainWindow import MainWindow
import sys


t1 = time.time()
print('##Execute ::', time.strftime("%H:%M:%S"), ":: NEVERA Activated")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

t2 =time.time()
print('##Execute ::', time.strftime("%H:%M:%S"), ":: Programme Ended")
print('Run Time = ', (t2-t1))