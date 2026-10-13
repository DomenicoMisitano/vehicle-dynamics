import numpy as np

def rpm_calculator(velocity, gear, i_diff, radius,  mu):
    gear_ratios = [5.087, 2.991, 2.035, 1.594, 1.286, 1.000]

    i_gear = gear_ratios[gear]

    angular_velocity = velocity / radius

    engine_angular_velocity = angular_velocity * i_gear * i_diff

    RPM = (engine_angular_velocity / (2*np.pi)) * 60

    return RPM