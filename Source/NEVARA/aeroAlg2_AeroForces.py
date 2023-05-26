import matplotlib.pyplot as plt
from sympy import *
from coolTools import *
from aeroAlg1_LiftDragCoefficients import *
from mainVariables import airDensity
import time



# returns symbolic function of Lift when link(wing) number given
def LSinQ_DCosQ(main, trueChord, RPM, spanLength, lcFunctionPitch, ldFunctionPitch, inducedVelocity=0):
    LSinQ = Function('LSinQ')
    DCosQ = Function('DCosQ')

    LSinQ = 0.5 * lcFunctionPitch * airDensity * trueChord * pow(main * RPMtoRads(RPM) + inducedVelocity, 2) * sp.sin(beta) * spanLength
    DCosQ = 0.5 * ldFunctionPitch * airDensity * trueChord * pow(main * RPMtoRads(RPM) + inducedVelocity, 2) * sp.cos(beta) * spanLength

    print('##Execute ::', time.strftime("%H:%M:%S"), ":: LSinQ-DCosQ is returned")
    return LSinQ-DCosQ

# returns symbolic function of Lift when link(wing) number given
def LCosQ_DSinQ(main, trueChord, RPM, spanLength, lcFunctionPitch, ldFunctionPitch, inducedVelocity=0):
    LCosQ = Function('LCosQ')
    DSinQ = Function('DSinQ')

    LCosQ = 0.5 * lcFunctionPitch * airDensity * trueChord * pow(main * RPMtoRads(RPM) + inducedVelocity, 2) * sp.cos(beta) * spanLength
    DSinQ = 0.5 * ldFunctionPitch * airDensity * trueChord * pow(main * RPMtoRads(RPM) + inducedVelocity, 2) * sp.sin(beta) * spanLength

    print('##Execute ::', time.strftime("%H:%M:%S"), ":: LCosQ-DSinQ is returned")
    return LCosQ-DSinQ





