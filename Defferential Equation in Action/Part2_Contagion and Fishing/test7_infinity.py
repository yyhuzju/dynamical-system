import math
import numpy
import matplotlib.pyplot
import math


end_time = 0.64
h = 0.0001
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))

x = numpy.zeros(num_steps + 1)
x[0] = 3.

def forward_euler():
    for step in range(num_steps):
        ###Your code here.  
        x[step+1] = x[step]+h*(x[step]**2+1)/2.
    #########check the content of x and of end_time
    return x

x = forward_euler()


def plot_me():
    matplotlib.pyplot.plot(times, x)
    matplotlib.pyplot.show()

plot_me()
matplotlib.pyplot.show()