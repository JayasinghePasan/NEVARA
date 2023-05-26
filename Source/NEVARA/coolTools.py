import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy import *
from mainVariables import beta


#return rad-s when RPM is given
def RPMtoRads(RPM):
    return (RPM*2*np.pi)/60

#Returns Two NumPy arrays containing the x and y values for the plot.
def plot_symbolic_function(f_beta, min_deg=0, max_deg=360, num_points=180):
       # Convert degrees to radians
    min_rad = np.deg2rad(min_deg)
    max_rad = np.deg2rad(max_deg)

    # Create an array of x values (angles in radians)
    x_vals = np.linspace(min_rad, max_rad, num_points)

    # Evaluate the function at the x values
    y_vals = sp.lambdify(sp.symbols('beta'), f_beta, 'numpy')(x_vals)

    # Convert the x values back to degrees
    x_vals = np.rad2deg(x_vals)

    return x_vals, y_vals


# apply limit a and b to the integral solved by base integral
# a=upper integral limit
# b=lower integral limit
def limitIntegral(a,b,function,variable):
    output = sp.integrate(function)
    return output.subs(variable,a) - output.subs(variable,b)



#return a arrey of integral limits when number of blades are given
def BladeLimitFinder(bladeNumber):
    limitArrrey = []
    for i in range(0,bladeNumber):
        element1 = (2 * np.pi) / bladeNumber * i
        element2 = element1 + (2 * np.pi)
        elementArrey = [element1,element2]
        limitArrrey.append(elementArrey)
    return  limitArrrey


def shift(key, array):
    return array[-key:] + array[:-key]

# return a plot for a single function when function and variable given
#function = Function to be drawn
#beta     = 'x' Variable
#range    = Arrey of range of 'x' in radians
#steps    =  number of calculation steps needed in the range
def SingleFunctionPlotter(function,beta,rangeInRad,steps):
    beta_input = np.linspace(rangeInRad[0], rangeInRad[1], steps)
    beta_input_deg = np.linspace(rangeInRad[0] * 180 / np.pi, rangeInRad[1] * 180 / np.pi, steps)
    lift_output = []
    for element in beta_input:
        lift_output.append(function.subs(beta,element))

    return plt.plot(beta_input_deg,lift_output)


# return a plot of a sumFunction when function arrey is given with beta
#functionArrey = functions to be drawn as a arrey
#beta     = 'x' Variable
#range    = Arrey of range of 'x' in radians
#steps    =  number of calculation steps needed in the range
def MultipleFunctionPlotter(functionArrey,beta, rangeInRad, steps):
    allarreys = []
    beta_input = np.linspace(rangeInRad[0], rangeInRad[1], steps)
    beta_input_deg = np.linspace(rangeInRad[0] * 180 / np.pi, rangeInRad[1] * 180 / np.pi, steps)

    for func in functionArrey:
        lift_output = []
        for element in beta_input:
            lift_output.append(func.subs(beta, element))
        allarreys.append(lift_output)

    sumArrey = np.sum(allarreys,axis=0) #add each element of all arreys

    return plt.plot(beta_input_deg, sumArrey)


