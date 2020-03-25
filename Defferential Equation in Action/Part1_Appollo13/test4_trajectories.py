import math
import numpy
import matplotlib.pyplot

h = 0.1
g = 9.81
acceleration = numpy.array([0.,-g])
initial_speed = 20.

def trajectory():
    angles = numpy.linspace(20.,70.,6)

    num_steps = 30
    x=numpy.zeros([num_steps+1,2])
    v=numpy.zeros([num_steps+1,2])

    for angle in angles:
        angle_rad = math.pi /180.0*angle
        x[0,0]=0.
        x[0,1]=0.
        v[0,0] = initial_speed*math.cos(angle_rad)
        v[0,1] = initial_speed*math.sin(angle_rad)
        for step in range(num_steps):
            x[step+1]=x[step]+h*v[step]
            v[step+1]=v[step]+h*acceleration
        matplotlib.pyplot.plot(x[:,0],x[:,1])
    return x,v
x,v=trajectory()

matplotlib.pyplot.show()
