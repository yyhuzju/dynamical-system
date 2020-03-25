import numpy

earth_mass = 5.97e24
moon_mass = 7.35e22
gravitational_constant = 6.67e-11

def acceleration(moon_position,spaceship_position):
    vector_to_moon = moon_position-spaceship_position
    vector_to_earth = -spaceship_position
    return gravitational_constant*(earth_mass/numpy.linalg.norm(vector_to_earth)**3 *vector_to_earth
    +moon_mass/numpy.linalg.norm(vector_to_moon)**3 *vector_to_moon)
