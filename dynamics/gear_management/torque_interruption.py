from dynamics.data_managing.motion_step import update_motion_step
from dynamics.resisting_forces.resistive_force import total_resistive_force


def simulate_torque_interruption(times, velocities, positions, time, velocity, position, F_t, mass, dt, density, c_drag, area, relativevelocity, c_rr, angle):
    F_t = 0

    F_tot = F_t + total_resistive_force(density, c_drag, area, relativevelocity, c_rr, mass, velocity, angle)

    velocity, relativevelocity, time, position = update_motion_step(F_tot, mass, velocity, dt, position, time,
                                                                    velocities, positions, times)

    return velocity, relativevelocity, time, position