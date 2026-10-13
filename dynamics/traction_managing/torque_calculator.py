import numpy as np
from dynamics.traction_managing.RPM_calculator import rpm_calculator


def calculate_torque( velocity, gear, i_diff, radius, mu):
    torque_curve = [(1000, 145),(1500, 165),(2000, 180),(2500, 190),(3000, 197),(3500, 202),(4000, 205),(4500, 203),(5000, 200),(5500, 197),(6000, 193),(6500, 189),(7000, 184),(7500, 170)]

    rpm_points, torque_points = zip(*torque_curve)

    RPM = rpm_calculator(velocity, gear,  i_diff, radius, mu)

    torque = np.interp(RPM, rpm_points, torque_points)

    return torque, gear

