import math
import numpy
import matplotlib.pyplot

total_time = 24.*3600
g = 9.81
earth_mass = 5.97e24
gravitational_constant = 6.67e-11
radius = (gravitational_constant * earth_mass * total_time**2. / 4. / math.pi ** 2.) ** (1. / 3.)
speed = 2.0 * math.pi * radius / total_time

def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position # earth located at origin
    return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth

def calculate_error(num_steps):
    ###Your code here.
    h = total_time/num_steps
    x = numpy.zeros([num_steps+1,2])
    v = numpy.zeros([num_steps+1,2])

    x[0,0] = radius
    v[0,1] = speed

    for step in range(num_steps):
        x[step+1] = x[step]+h*v[step]
        v[step+1] = v[step]+h*acceleration(x[step])
    error = numpy.linalg.norm(x[-1]-x[0])
    matplotlib.pyplot.scatter(h,error)
    # This is used for plotting
    
    h_array.append(h)
    error_array.append(error)
    return error
    
h_array=[]
error_array=[]
for num_steps in [200, 500, 1000, 2000, 5000, 10000]:
    error = calculate_error(num_steps)
matplotlib.pyplot.xlim(xmin=0.)
matplotlib.pyplot.ylim(ymin=0.)
axes = matplotlib.pyplot.gca()
matplotlib.pyplot.show()