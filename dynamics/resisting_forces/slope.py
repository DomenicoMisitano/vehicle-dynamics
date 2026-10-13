import numpy as np

def slope_force(mass, angle):
    return -9.81 * mass * np.sin(angle)

