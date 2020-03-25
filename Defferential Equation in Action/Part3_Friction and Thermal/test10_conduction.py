# PROBLEM 1
# 
# Model heat conduction in a wire that we will pretend is made up of 100 segments.
# Show how the change in temperature of a given segment depends on the temperature
# of the segments to either side of it by filling in the array coefficients.  This
# is a matrix that can be multiplied by a vector containing every segment's
# temperature after one time step to yield a vector containing all of the initial
# temperatures.  Use numpy.linalg.solve(coefficients, temperatures_old) to compute
# the values of temperatures_new.  Then implement the implicit finite difference 
# method to show how the temperature of each segment changes with time. 


import math
import numpy
import matplotlib.pyplot
import math


ambient_temperature = 300. # K
flame_temperature = 1000. # K
thermal_diffusivity = 10. * 0.001 ** 2 # m2 / s
dx = 0.001 # m
size = 100 # grid units
positions = dx * numpy.arange(size) # m

# Task 2: Set the step size h to 0.5 when submitting.
h = 0.05 # s
end_time = 10.0 # s
num_steps = int(end_time / h)

def heat_conduction_implicit():
    temperatures_old = ambient_temperature * numpy.ones(size) # K
    for i in range(int(4 * size / 10), int(5 * size / 10)):
        temperatures_old[i] = flame_temperature
    temperatures_new = numpy.copy(temperatures_old) # K

    c = h * thermal_diffusivity / dx ** 2
    coefficients = numpy.zeros([size, size])

    # Task 1: Fill the array named "coefficients" with appropriate values.
    for i in range(1,size-1):
        coefficients[i,i] = 1.+2.*c
    for i in range(0,size-1):
        coefficients[i,i+1] = -c
        coefficients[i+1,i] = -c
    coefficients[0,0] = 1.+c
    coefficients[-1,-1] = 1.+c 
    for step in range(num_steps):
        temperatures_new = numpy.linalg.solve(coefficients,temperatures_old)
        # Fill this in with the proper new, implicit method.
        # For comparison, this is the explicit method we've used before:
        # for i in range(1, size - 1):
        #     temp = temperatures_old[i]
        #     temperatures_new[i] = temp + h * thermal_diffusivity / dx ** 2 * (
        #         temperatures_old[i - 1] + temperatures_old[i + 1] - 2.0 * temp)
        temperatures_old = temperatures_new
    return temperatures_old

temperatures = heat_conduction_implicit()


def heat_plot():
    matplotlib.pyplot.plot(positions, temperatures)
    axes = matplotlib.pyplot.gca()                
    axes.set_xlabel('Position in m')
    axes.set_ylabel('Temperature in K')

heat_plot()
matplotlib.pyplot.show()


