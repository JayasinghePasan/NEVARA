import time
import matplotlib.pyplot as plt
from mainVariables import beta, PI
from sympy.plotting import plot
from mainVariables import beta

        # 0  - Pitch angle vs azimuth angle
        # 1  - Cl vs attack angle
        # 2  - Cd vs attack angle
        # 3  - Cl vs azimuth angle
        # 4  - Cd vs azimuth angle
        # 5  - Vertical thrust   (single)
        # 6  - Horizontal thrust (single)
        # 7  - Resultant thrust  (single)
        # 8  - Vertical thrust   (All)
        # 9  - Horizontal thrust (All)
        # 10 - Resultant thrust  (All)

def plotMasterSingle(rotor, plotNumber):
    plot_temp = plotMasterFunction(rotor, plotNumber)
    plot_temp.show()

def plotMasterFunction(rotor, plotNumber):

    if plotNumber == 0:   # 0  - pitch angle vs azimuth angle
        print('##Execute ::', time.strftime("%H:%M:%S"), ":: Plot(" + str(plotNumber) + ") Created - pitch angle vs azimuth angle")
        return plot(rotor.pitchAzimuthFunction, (beta, 0, 2 * PI), xlabel="Azimuth Angle (rad)", ylabel="Pitch Angle (rad)",show =False)

    if plotNumber == 1:   # 1  - Cl vs azimuth angle
        print('##Execute ::', time.strftime("%H:%M:%S"), ":: Plot(" + str(plotNumber) + ") Created - Cl vs azimuth angle")
        return plot(rotor.CLFunctionBeta, (beta, -18 * PI / 180, 18 * PI / 180), title=str(rotor.wingName),xlabel="Attack Angle (rad)", ylabel="Lift Coefficient",show =False)

    if plotNumber == 2:   # 2  - Cd vs azimuth angle
        print('##Execute ::', time.strftime("%H:%M:%S"), ":: Plot(" + str(plotNumber) + ") Created - Cd vs azimuth angle")
        return plot(rotor.CDFunctionBeta, (beta, -18 * PI / 180, 18 * PI / 180), title=str(rotor.wingName),xlabel="Attack Angle (rad)", ylabel="Drag Coefficient",show =False)

    if plotNumber == 3:    # 3  - Cl vs pitch angle
        print('##Execute ::', time.strftime("%H:%M:%S"), ":: Plot(" + str(plotNumber) + ") Created - Cl vs pitch angle")
        return plot(rotor.CLFunctionPitch, (beta, 0, 2 * PI), title="Cl vs Azimuth Angle : " + str(rotor.wingName),xlabel="Azimuth Angle (rad)", ylabel="Lift Coefficient",show =False)

    if plotNumber == 4:    # 4  - Cd vs pitch angle
        print('##Execute ::', time.strftime("%H:%M:%S"), ":: Plot(" + str(plotNumber) + ") Created - Cd vs pitch angle")
        return plot(rotor.CDFunctionPitch, (beta, 0, 2 * PI), title="Cd vs Azimuth Angle : " + str(rotor.wingName),xlabel="Azimuth Angle (rad)", ylabel="Drag Coefficient",show =False)

    if plotNumber == 5:    # 5  - Vertical thrust   (single)
        print('##Execute ::', time.strftime("%H:%M:%S"), ":: Plot(" + str(plotNumber) + ") Created - Vertical thrust(Single) vs pitch angle")
        return plot(rotor.thrustVertical, (beta, 0, 2 * PI), title="Vertical Thrust vs Azimuth Angle : " + str(rotor.wingName),xlabel="Azimuth Angle (rad)", ylabel="Thrust (N)",show =False)

    if plotNumber == 6:    # 6  - Horizontal thrust (single)
        print('##Execute ::', time.strftime("%H:%M:%S"), ":: Plot(" + str(plotNumber) + ") Created - Horizontal thrust(Single) vs pitch angle")
        return plot(rotor.thrustHorizontal, (beta, 0, 2 * PI),
             title="Horizontal Thrust vs Azimuth Angle : " + str(rotor.wingName),xlabel="Azimuth Angle (rad)", ylabel="Thrust (N)",show =False)

    if plotNumber == 7:    # 7  - Resultant thrust  (single)
        print('##Execute ::', time.strftime("%H:%M:%S"), ":: Plot(" + str(plotNumber) + ") Created - Resultant thrust(Single) vs pitch angle")
        return plot(rotor.thrustResultant, (beta, 0, 2 * PI),title="Resultant Thrust vs Azimuth Angle : " + str(rotor.wingName),xlabel="Azimuth Angle (rad)", ylabel="Thrust (N)",show =False)

    if plotNumber == 8:    # 8  - Vertical thrust   (All)
        plot_main = plot(rotor.totalThrustVertical, (beta, 0, 2 * PI),title="Total Vertical Thrust vs Azimuth Angle : " + str(rotor.wingName),xlabel="Azimuth Angle (rad)", ylabel="Thrust (N)", show=False)
        for i in range (0,rotor.bladeNumber):
            plot_main.extend(plot(rotor.thrustVertical.subs(beta, beta +  i * (2*PI)/rotor.bladeNumber),(beta, 0, 2 * PI),show=False))
        print('##Execute ::', time.strftime("%H:%M:%S"), ":: Plot(" + str(plotNumber) + ") Created - Vertical thrust(All) vs pitch angle")
        return plot_main

    if plotNumber == 9:    # 9  - Horizontal thrust (All)
        plot_main = plot(rotor.totalThrustHorizontal, (beta, 0, 2 * PI),
             title="Total Horizontal Thrust vs Azimuth Angle : " + str(rotor.wingName),xlabel="Azimuth Angle (rad)", ylabel="Thrust (N)",show=False)
        for i in range (0,rotor.bladeNumber):
            plot_main.extend(plot(rotor.thrustHorizontal.subs(beta, beta +  i * (2*PI)/rotor.bladeNumber),(beta, 0, 2 * PI),show=False))
        print('##Execute ::', time.strftime("%H:%M:%S"), ":: Plot(" + str(plotNumber) + ") Created - Horizontal thrust(All) vs pitch angle")
        return plot_main

    if plotNumber == 10:    # 10 - Resultant thrust  (All)
        print('##Execute ::', time.strftime("%H:%M:%S"), ":: Plot(" + str(plotNumber) + ") Created - Resultant thrust(All) vs pitch angle")
        return plot(rotor.totalThrustResultant, (beta, 0, 2 * PI),title="Total Resultant Thrust vs Azimuth Angle : " + str(rotor.wingName),xlabel="Azimuth Angle (rad)", ylabel="Thrust (N)",show =False)

