from dynamics.traction_managing.traction import traction_force
from dynamics.gear_management.gear_selection import select_gear

def traction_force_with_gear_selection(velocity, gear, i_diff, eta, mu, radius, mass, clutch_traction, mu_gear, r_f, F_smax, time, dt, RPM, wheel_radius, relativevelocity, position, velocities, positions, times):
    gear, time, velocity, relativevelocity, position = select_gear(velocity, gear, i_diff, mu, eta, radius, mass, clutch_traction, mu_gear, r_f, F_smax, time, dt, RPM, wheel_radius, relativevelocity, position, velocities, positions, times)

    return traction_force(velocity, gear, i_diff, eta, radius, mu, mass), gear

