import numpy as np
from numpy.ma.core import less_equal

from dynamics.traction_managing.torque_calculator import calculate_torque


def traction_force( velocity, gear, i_diff, eta, radius, mu, mass):
    gear_ratios = [5.087, 2.991, 2.035, 1.594, 1.286, 1.000]

    i_gear = gear_ratios[gear]

    if mass <= 0:
        raise ValueError("mass deve essere maggiore di 0")

    if radius <= 0:
        raise ValueError("wheel_radius deve essere maggiore di 0")

    if i_gear <= 0 or i_diff <= 0:
        raise ValueError("i rapporti di trasmissione devono essere maggiori di 0")

    if eta < 0 or eta > 1:
        raise ValueError("eta deve essere compreso tra 0 e 1")

    if mu < 0:
        raise ValueError("mu non può essere negativo")

    torque, gear = calculate_torque(velocity, gear, i_diff, radius, mu)

    i_gear = gear_ratios[gear]

    t_wheel = torque * i_gear * i_diff * eta

    F_t = t_wheel / radius

    friction_max = mu * (9.81 * mass)

    return min(F_t, friction_max)




