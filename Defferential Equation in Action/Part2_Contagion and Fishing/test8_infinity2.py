import math
import numpy
import matplotlib.pyplot
import math

# This is used to keep track of the data that we want to plot.
data = []

def forward_euler():
    end_time = 10.
    h = 0.01
    num_steps = int(end_time / h)
    times = h * numpy.array(range(num_steps + 1))

    x = numpy.zeros(num_steps + 1)
    for x0 in [0., 0.01, 1e-300]:
        x[0] = x0
        for step in range(num_steps):
            x[step+1] = x[step]+h*x[step]**(1./3.)
        
        data.append(([time for time in times], [x_i for x_i in x]))

    return x

x = forward_euler()


def plot_me():
    for (times, x) in data:
        matplotlib.pyplot.plot(times, x, linewidth = 3.)

plot_me()
matplotlib.pyplot.show()