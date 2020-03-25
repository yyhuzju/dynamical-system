# QUIZ
# 
# Implement the 2D Heat Equation in the 
# heat_conduction function below.

import math
import numpy
import matplotlib.pyplot
import math


ambient_temperature = 300. # K
flame_temperature = 1000. # K
thermal_diffusivity = 10. * 0.001 ** 2 # m2 / s
dx = 0.001 # m
size = 50 # grid units
positions = dx * numpy.arange(size) # m
h = 0.02 # s
end_time = 1. # s
num_steps = int(end_time / h)

def heat_conduction():
    temperatures_old = ambient_temperature * numpy.ones([size, size]) # K
    for iy in range(int(4 * size / 10), int(5 * size / 10)):
        for ix in range(int(4 * size / 10), int(5 * size / 10)):    
            temperatures_old[iy, ix] = flame_temperature
    temperatures_new = numpy.copy(temperatures_old) # K

    for step in range(num_steps):
        for iy in range(1, size - 1):
            for ix in range(1, size - 1):
                ###Your code here.
                temp = temperatures_old[iy,ix]
                temperatures_new[iy,ix] = temp+h*thermal_diffusivity/dx**2*(
                    temperatures_old[iy,ix-1]+temperatures_old[iy,ix+1]+temperatures_old[iy-1,ix]+temperatures_old[iy+1,ix]
                    -4*temp
                )
        temperatures_old, temperatures_new = temperatures_new, temperatures_old

    return temperatures_old

temperatures = heat_conduction()


def plot_me():
    axes = matplotlib.pyplot.gca()
    dimensions = [0, dx * size, 0, dx * size]
    matplotlib.pyplot.imshow(temperatures, cmap = 'hot',
                            interpolation='bessel',
                             origin = 'lower', extent = dimensions)
    matplotlib.pyplot.colorbar().set_label('Temperature in K')
    axes.set_xlabel('Position x in m')
    axes.set_ylabel('Position y in m')                

plot_me()
matplotlib.pyplot.show()

