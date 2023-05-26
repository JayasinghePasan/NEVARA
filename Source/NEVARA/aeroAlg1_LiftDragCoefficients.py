from aeroAlg0_PitchVsAzimuth import *
from mainVariables import PI

# return lift or drag coefficient as a symbolic function of beta
# state = lift or drag
# rodData = Arrey of lengths of A_rod , B_rod , C_rod , D_rod
# lcCordinates.txt should include a list of  -   "AttachAngle" , "clCoefficient" , "cdCoefficient"

def liftCoefficientFunctionBeta(variable,wingObject):
    lcFunction = Function("lcFunction")
    A_array = wingObject.ClFunctionArray
    lcFunction = A_array[0] * pow(variable, 6) + A_array[1] * pow(variable, 5) + A_array[2] * pow(variable, 4) + A_array[3] * pow(variable, 3) + A_array[4] * pow(variable, 2) + A_array[5] * pow(variable, 1) + A_array[6]

    # AR = wingObject.aspectRatio
    # lcFunctionWithDW = new_cl=(2*PI*AR)/(2+pow((((pow(AR,2)*4*pow(PI,2))/pow(lcFunction,2))+4),(1/2)))
    # return lcFunctionWithDW
    return lcFunction

def dragCoefficientFunctionBeta(variable,wingObject):
    ldFunction = Function("ldFunction")
    A_array = wingObject.CdFunctionArray
    ldFunction = A_array[0] * pow(variable, 6) + A_array[1] * pow(variable, 5) + A_array[2] * pow(variable, 4) + A_array[3] * pow(variable, 3) + A_array[4] * pow(variable, 2) + A_array[5] * pow(variable, 1) + A_array[6]
    return ldFunction
