import numpy as np
from dynamics.resisting_forces.drag import drag_force
from dynamics.resisting_forces.rr import rr_force
from dynamics.resisting_forces.slope import slope_force

def total_resistive_force(density, c_drag, area, relativevelocity, c_rr, mass, velocity, angle):
    drag = drag_force(density, c_drag, area, relativevelocity)

    rr = rr_force(c_rr, mass, velocity)

    slope = slope_force(mass, np.deg2rad(angle))

    F_res = drag + rr + slope

    return F_res