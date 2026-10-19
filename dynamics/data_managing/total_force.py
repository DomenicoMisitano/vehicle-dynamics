import numpy as np
from dynamics.resisting_forces.resistive_force import total_resistive_force
from dynamics.traction_managing.traction import traction_force

def tot_force(density, c_drag, area, relativevelocity, c_rr, mass, velocity, angle, gear, i_diff, eta, mu, radius):
    F_res = total_resistive_force(density, c_drag, area, relativevelocity, c_rr, mass, velocity, angle)

    F_t = traction_force(velocity, gear, i_diff, eta, radius, mu, mass)

    F_tot = F_t + F_res

    return F_tot, gear