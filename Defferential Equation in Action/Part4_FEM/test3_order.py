# QUIZ
#
# Examine the diagram, determine the order of this solver, 
# and set the variable order_of_solver to this number.

import math
import numpy
import matplotlib.pyplot
import math


total_time = 24. * 3600. # s
g = 9.81 # m / s2
earth_mass = 5.97e24 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2
radius = (gravitational_constant * earth_mass * total_time**2. / 4. / math.pi ** 2.) ** (1. / 3.) # m
speed = 2.0 * math.pi * radius / total_time

def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position # earth located at origin
    return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth

a21 = 1. / 4.
a31 = 3. / 32.
a32 = 9. / 32.
a41 = 1932. / 2197.
a42 = -7200. / 2197.
a43 = 7296. / 2197.
a51 = 439. / 216.
a52 = -8.
a53 = 3680. / 513.
a54 = -845. / 4104.
a61 = -8. / 27.
a62 = 2.
a63 = -3544. / 2565
a64 = 1859. / 4104.
a65 = -11. / 40.
b1 = 16. / 135.
b3 = 6656. / 12825.
b4 = 28561. / 56430.
b5 = -9. / 50.
b6 = 2. / 55.

### Modify this code
order_of_solver = 42
### End modified code


def plot_me():
    for num_steps in [50, 100, 200, 500, 1000]:
        h = total_time / num_steps
        x = numpy.zeros([num_steps + 1, 2]) # m
        v = numpy.zeros([num_steps + 1, 2]) # m / s
        x[0, 0] = radius
        v[0, 1] = speed
        for step in range(num_steps):
            kx1 = h * v[step]
            kv1 = h * acceleration(x[step])
            kx2 = h * (v[step] + a21 * kv1)
            kv2 = h * acceleration(x[step] + a21 * kx1)
            kx3 = h * (v[step] + a31 * kv1 + a32 * kv2)
            kv3 = h * acceleration(x[step] + a31 * kx1 + a32 * kx2)
            kx4 = h * (v[step] + a41 * kv1 + a42 * kv2 + a43 * kv3)
            kv4 = h * acceleration(x[step] + a41 * kx1 + a42 * kx2 + a43 * kx3)
            kx5 = h * (v[step] + a51 * kv1 + a52 * kv2 + a53 * kv3 + a54 * kv4)
            kv5 = h * acceleration(x[step] + a51 * kx1 + a52 * kx2 + a53 * kx3 + a54 * kx4)
            kx6 = h * (v[step] + a61 * kv1 + a62 * kv2 + a63 * kv3 + a64 * kv4 + a65 * kv5)
            kv6 = h * acceleration(x[step] + a61 * kx1 + a62 * kx2 + a63 * kx3 + a64 * kx4 + a65 * kx5)
            x[step + 1] = x[step] + b1 * kx1 + b3 * kx3 + b4 * kx4 + b5 * kx5 + b6 * kx6
            v[step + 1] = v[step] + b1 * kv1 + b3 * kv3 + b4 * kv4 + b5 * kv5 + b6 * kv6
                
        error = numpy.linalg.norm(x[-1] - x[0])
        matplotlib.pyplot.scatter(h, error)

    matplotlib.pyplot.ylim(ymin = 1e-5)
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Step size in s')
    axes.set_ylabel('Error in m')
    axes.set_xscale('log')
    axes.set_yscale('log')

plot_me()
matplotlib.pyplot.show()

