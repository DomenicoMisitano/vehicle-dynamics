from dynamics.traction_managing.traction import traction_force
from dynamics.traction_managing.RPM_calculator import rpm_calculator
from dynamics.gear_management.clutch_engagement_sequence import run_clutch_engagement_sequence

def select_gear(velocity, gear, i_diff, mu, eta, radius, mass, clutch_traction, mu_gear, r_f, F_smax, time, dt, RPM, wheel_radius, relativevelocity, position, velocities, positions, times ):
    while rpm_calculator(velocity, gear, i_diff, radius, mu) > 7500 and gear < 5:
        gear = gear + 1

        F_t, time, velocity, relativevelocity, position = run_clutch_engagement_sequence(clutch_traction, mu_gear, r_f, F_smax, time, dt, RPM, wheel_radius, mass, velocity, relativevelocity, position, velocities, positions, times)

    if gear >= 5:
        return gear, time, velocity, relativevelocity, position

    F_ti = traction_force(velocity, gear, i_diff, eta, radius, mu, mass)

    F_tf = traction_force(velocity, gear + 1, i_diff, eta, radius, mu, mass)

    while F_tf > F_ti and gear < 5:
        gear = gear + 1

        F_t, time, velocity, relativevelocity, position = run_clutch_engagement_sequence(clutch_traction, mu_gear, r_f, F_smax, time, dt, RPM, wheel_radius, mass, velocity, relativevelocity, position, velocities, positions, times)

        if gear == 5:
            break

        F_ti = traction_force(velocity, gear, i_diff, eta, radius, mu, mass)

        F_tf = traction_force(velocity, gear + 1, i_diff, eta, radius, mu, mass)

    return gear, time, velocity, relativevelocity, position