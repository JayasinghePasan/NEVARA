import time
from sympy import atan
from mainVariables import beta, PI, airDensity
from aeroAlg0_PitchVsAzimuth import betaVsPitchAngleFunction
from aeroAlg1_LiftDragCoefficients import liftCoefficientFunctionBeta, dragCoefficientFunctionBeta
from aeroAlg2_AeroForces import LSinQ_DCosQ, LCosQ_DSinQ
from Aero____Class_Wings import *


class cycloRotor:

    def __init__(self,rodDataArray):
        self.main           = float(rodDataArray[0])
        self.chordLink      = float(rodDataArray[1])
        self.secondryLink   = float(rodDataArray[2])
        self.eccentry       = float(rodDataArray[3])
        self.wingName       = str(rodDataArray[4])
        self.bladeNumber    = int(rodDataArray[5])
        self.trueChord      = float(rodDataArray[6])
        self.spanLength     = float(rodDataArray[7])
        self.RPM            = float(rodDataArray[8])

        wingObject = wing(self.wingName, self.trueChord, self.spanLength)

        self.pitchAzimuthFunction = betaVsPitchAngleFunction([self.main, self.chordLink, self.secondryLink, self.eccentry])
        self.CLFunctionBeta   = liftCoefficientFunctionBeta(beta, wingObject)
        self.CDFunctionBeta   = dragCoefficientFunctionBeta(beta, wingObject)

        self.CLFunctionPitch  = liftCoefficientFunctionBeta(self.pitchAzimuthFunction, wingObject)
        self.CDFunctionPitch  = dragCoefficientFunctionBeta(self.pitchAzimuthFunction, wingObject)

        self.thrustVertical   = LSinQ_DCosQ(self.main, self.trueChord, self.RPM, self.spanLength, self.CLFunctionPitch, self.CDFunctionPitch )
        self.thrustHorizontal = LCosQ_DSinQ(self.main, self.trueChord, self.RPM, self.spanLength, self.CLFunctionPitch, self.CDFunctionPitch )
        self.thrustResultant  = pow(pow(self.thrustVertical,2) + pow(self.thrustHorizontal,2),0.5)

        self.totalThrustVertical   = 0
        self.totalThrustHorizontal = 0

        for wingNo in range (0,self.bladeNumber):
            self.totalThrustVertical   += self.thrustVertical.subs(beta, beta + wingNo * 2 * PI / self.bladeNumber)
            self.totalThrustHorizontal += self.thrustHorizontal.subs(beta, beta + wingNo * 2 * PI / self.bladeNumber)

        self.totalThrustResultant = pow(pow(self.totalThrustVertical,2) + pow(self.totalThrustHorizontal,2),0.5)
        self.totalThrustDirection = atan(self.totalThrustVertical/self.totalThrustHorizontal)

        print('##Execute ::', time.strftime("%H:%M:%S"), ":: CycloRotor Class object was created")