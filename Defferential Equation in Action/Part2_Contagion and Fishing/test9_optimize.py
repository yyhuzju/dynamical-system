import math
import numpy
import matplotlib.pyplot
import math

def total_harvest():
    maximum_growth_rate = 0.5 # 1 / year
    carrying_capacity = 2e6 # tons
    maximum_harvest_rate = 0.8 * 2.5e5 # tons / year

    end_time = 10. # years
    h = 0.1 # years
    num_steps = int(end_time / h)
    #times = h * numpy.array(range(num_steps + 1))

    fish = numpy.zeros(num_steps + 1) # tons
    fish[0] = 2e5

    results = []

    for ramp_start in numpy.arange(0., 10.01, 0.5): # 10.01 to prevent issues with roundoff errors
        for ramp_end in numpy.arange(ramp_start, 10.01, 0.5): # 10.01 to prevent issues with roundoff errors
            ### Modify the below code to calculate total_harvest
            total_harvest = 0.0
            is_extinct = False
            for step in range(num_steps):
                time = h * step # years
                harvest_factor = 0.0
                if time > ramp_end:
                    harvest_factor = 1.0
                elif time > ramp_start:
                    harvest_factor = (time - ramp_start) / (ramp_end - ramp_start)    
                harvest_rate = harvest_factor * maximum_harvest_rate
                
                if is_extinct:
                    current_harvest = 0.
                    fish_next_step = 0.
                else:
                    current_harvest = h*harvest_rate
                    fish_next_step = fish[step] + h * (maximum_growth_rate * (1. - fish[step] / carrying_capacity) * fish[step] - harvest_rate)
                    if fish_next_step <= 0.:
                        is_extinct = True
                        fish_next_step = 0.
                        current_harvest = fish[step]               
                fish[step + 1] = fish_next_step
                total_harvest += current_harvest
            results.append([ramp_start, ramp_end, total_harvest])
            ### End code to modify

    return results

results = total_harvest()
def plot_me():
    # This adjusts the size of the dots to compare them easily. 
    matplotlib.pyplot.scatter([r[0] for r in results], [r[1] for r in results], [5e-11 * r[2] ** 2. for r in results], edgecolor = 'none')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Ramp start in years')
    axes.set_ylabel('Ramp end in years')

plot_me()
matplotlib.pyplot.show()