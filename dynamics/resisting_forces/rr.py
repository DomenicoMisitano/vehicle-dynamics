import numpy as np

def rr_force(c_rr, mass, velocity):
    weight = mass * 9.81
    return -c_rr * weight * np.sign(velocity)
