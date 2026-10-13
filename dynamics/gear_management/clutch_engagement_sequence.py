import numpy as np
from dynamics.gear_management.clutch_engagement import simulate_clutch_engagement
def run_clutch_engagement_sequence(clutch_traction, mu, eta, r_f, F_smax, time, dt, RPM, wheel_radius, mass, velocity, relativevelocity, position, velocities, positions, times):
    RPM_wheel = 0

    while RPM != RPM_wheel:
       F_t, time, velocity, relativevelocity, position, RPM, RPM_transmission = simulate_clutch_engagement(clutch_traction, mu, r_f, F_smax, time, dt, RPM, wheel_radius, mass, velocity, relativevelocity, position, velocities, positions, times)

    return F_t, time, velocity, relativevelocity, position