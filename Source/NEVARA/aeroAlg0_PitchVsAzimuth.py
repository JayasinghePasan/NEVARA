from sympy import *
from mainVariables import beta
from mainVariables import PI
import time



#Input rodData = [main,chord,secondry,eccentry]
# return function of pitchAngle vs Assymuth Angle
def betaVsPitchAngleFunction(rodData):

    lm,c,ls,e = rodData[0],rodData[1],rodData[2],rodData[3]
    l = Function('l')
    l = pow(pow(e,2)+pow(lm,2)+ 2*e*lm*sin(beta),0.5)

    pitchFunction = Function('pitchFunction')
    pitchFunction = (PI/2) - acos((pow(l,2)+pow(c,2)-pow(ls,2))/(2*l*c)) - asin(e*cos(beta)/l)

    return pitchFunction

