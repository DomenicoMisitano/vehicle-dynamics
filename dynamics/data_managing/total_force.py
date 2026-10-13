import numpy as np
from dynamics.resisting_forces.resistive_force import total_resistive_force
from dynamics.traction_managing.traction_with_gear_selection import traction_force_with_gear_selection

def tot_force(density, c_drag, area, relativevelocity, c_rr, mass, velocity, angle, gear, i_diff, eta, mu, radius):
    F_res = total_resistive_force(density, c_drag, area, relativevelocity, c_rr, mass, velocity, angle)

    F_t, gear = traction_force_with_gear_selection(velocity, gear, i_diff, eta, mu, radius, mass)

    F_tot = F_t + F_res

    return F_tot, gear