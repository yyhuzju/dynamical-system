# PROBLEM 2
#
# This program simulates a wildfire in a square area of forest.  Taking into 
# account diffusion, heat loss, wind, and combustion, use the Forward Euler
# Method to show how the temperature and wood density at a given location change
# with time.  Then set up an initial distribution for the wood density.  Pretend 
# that the square of forest has infinitesimally thin parallel lines of constant wood
# density.  These lines all have the same slope, so their y-intercepts can serve
# as indicators of their respective wood densities.  Please see the question
# introduction video for more details.

import math
import numpy
import matplotlib.pyplot
import math


diffusion_coefficient = 5. # m2 / s
ambient_temperature = 310. # K
heat_loss_time_constant = 120. # s
velocity_x = 0.03 # m / s
velocity_y = 0.12 # m / s
ignition_temperature = 561. # K
burn_temperature = 1400. # K
burn_time_constant = 0.5 * 3600. # s
heating_value = (burn_temperature - ambient_temperature) / (
    heat_loss_time_constant * 100.) * burn_time_constant # K / (kg / m2)
slope = 0.4 # dimensionless
intercept_1 = 100. # m
intercept_2 = 170. # m
wood_1 = 100. # kg / m2
wood_2 = 70. # kg / m2

length = 650. # meters; domain extends from -length to +length
# A grid size of 50 x 50 ist much too small to see the correct result. For a better result, set the size to 200 x 200. That computation would, however, be far too long for the Web-based development environment. You may want to run it offline.
size = 100 # number of points per dimension of the grid
dx = 2. * length / size
# Pick a time step below the threshold of instability
h = 0.2 * dx ** 2 / diffusion_coefficient # s
end_time = 30. * 60. # s

# Convert from integer grid positions to coordinates measured in meters
def grid2physical(i, j):
    return i * dx - length + 0.5 * dx, j * dx - length + 0.5 * dx

def wildfire():
    temperatures_old = ambient_temperature * numpy.ones([size, size]) # K
    wood_old = numpy.zeros([size, size]) # kg / m2
    for j in range(0, size):
        for i in range(0, size):
            x, y = grid2physical(i, j)
            temperatures_old[j][i] = (burn_temperature - ambient_temperature) * \
                math.exp(-((x + 50.) ** 2 + (y + 250.) ** 2) / (2. * 50. ** 2)) \
                + ambient_temperature
            # Task 2: Replace the following line to fill the array wood_old according to the description, using the values given above.
            # Given:
            # wood_old[j][i] = 100.
            intercept = y-slope*x
            w = wood_1+(wood_2-wood_1)/(intercept_2-intercept_1)*(intercept-intercept_1)
            wood_old[j][i] = min(wood_1,max(wood_2,w))
            # Your code here

    temperatures_new = numpy.copy(temperatures_old) # K
    wood_new = numpy.copy(wood_old) # kg / m2

    num_steps = int(end_time / h)
    for step in range(num_steps):
        for j in range(1, size - 1):
            for i in range(1, size - 1):
                temp = temperatures_old[j][i]
                # Task 1: Insert heat diffusion, heat loss, wind, and combustion.
                # Given: 
                temp = temperatures_old[j][i]   
                burn_rate = 0.
                if temp >= ignition_temperature:
                    burn_rate = wood_old[j][i]/burn_time_constant
                wood_new[j][i] = wood_old[j][i]-h*burn_rate
                temperatures_new[j][i] = temp+h*(
                    diffusion_coefficient/dx**2*(
                    temperatures_old[j-1][i]+temperatures_old[j][i-1]
                    +temperatures_old[j+1][i]+temperatures_old[j][i+1]
                    -4*temp)
                    -(temp-ambient_temperature)/heat_loss_time_constant
                    -0.5 / dx*(
                        velocity_x*(temperatures_old[j][i+1]-temperatures_old[j][i-1])
                        +velocity_y*(temperatures_old[j+1][i]-temperatures_old[j-1][i]))
                    +heating_value*burn_rate)

         
                # wood_new[j][i] = wood_old[j][i]
                # temperatures_new[j][i] = temp
                
                # Your code here

        temperatures_old, temperatures_new = temperatures_new, temperatures_old
        wood_old, wood_new = wood_new, wood_old
    return temperatures_old, wood_old

temperatures_old, wood_old = wildfire()

def fire_plot():
    dimensions = [-length, length, -length, length]
                 
    axes = matplotlib.pyplot.subplot(121)
    matplotlib.pyplot.imshow(temperatures_old, interpolation = 'nearest', cmap = 'hot', origin = 'lower', extent = dimensions)
    matplotlib.pyplot.colorbar()
    axes.set_title('Temperature in K')
    axes.set_xlabel('x in m')
    axes.set_ylabel('y in m')

    axes = matplotlib.pyplot.subplot(122)
    matplotlib.pyplot.imshow(wood_old, cmap = 'winter', origin = 'lower', extent = dimensions)
    matplotlib.pyplot.colorbar()
    axes.set_title('Density of wood in kg/m$^2$')
    axes.set_xlabel('x in m')
    axes.set_ylabel('y in m')

fire_plot()    
matplotlib.pyplot.show()