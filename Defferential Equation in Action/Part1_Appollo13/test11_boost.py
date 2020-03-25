import math
import numpy
import matplotlib.pyplot

h = 3.0 # s
earth_mass = 5.97e24 # kg
spacecraft_mass = 30000. # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

# This is used to keep track of the data that we want to plot.

def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position # earth located at origin
    return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth

def apply_boost():
    num_steps = 7000
    x = numpy.zeros([num_steps + 1, 2]) # m
    v = numpy.zeros([num_steps + 1, 2]) # m / s

    x[0, 0] = 15e6
    x[0, 1] = 1e6    
    v[0, 0] = 2e3
    v[0, 1] = 4e3

    boost_done = False

    for step in range(num_steps):
        if h*step>=2.*3600 and not boost_done:
            ###Your code here.
            v[step] += 300.*v[step]/numpy.linalg.norm(v[step])
            boost_done = True
            matplotlib.pyplot.scatter(x[step,0],x[step,1],c='r')

        acceleration0 = acceleration(x[step])
        xE = x[step] + h * v[step]
        vE = v[step] + h * acceleration0
        x[step + 1] = x[step] + h * 0.5 * (v[step] + vE)
        v[step + 1] = v[step] + h * 0.5 * (acceleration0 + acceleration(xE))

    return x, v

x, v = apply_boost()
matplotlib.pyplot.plot(x[:, 0], x[:, 1])
matplotlib.pyplot.scatter(0, 0)
matplotlib.pyplot.axis('equal')
axes = matplotlib.pyplot.gca()
axes.set_xlabel('Longitudinal position in m')
axes.set_ylabel('Lateral position in m')
matplotlib.pyplot.show()
