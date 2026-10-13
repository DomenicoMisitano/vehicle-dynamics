import numpy as np

from dynamics.data_managing.motion_step import update_motion_step
from modello import i_gear, i_diff


def simulate_clutch_engagement(clutch_traction, mu, eta, r_f, F_smax, time, dt, RPM, v, wheel_radius, mass, velocity, relativevelocity, position, velocities, positions, times):
    t_ramp = 0.25

    F_s = F_smax * (0.5 * np.sin(np.pi * (time / t_ramp) - np.pi/2) + 0.5)

    T_t = (2 / 3) * np.pi * mu * (F_s / ((r_f ** 2) * np.pi)) * r_f ** 3

    F_t = T_t * i_gear * i_diff * eta / wheel_radius

    velocity, relativevelocity, time, position = update_motion_step(F_t, mass, velocity, dt, position, time, velocities, positions, times)

    RPM_transimission = (velocity / r_f) * (60 / 2*np.pi)

    return F_t, time, velocity, relativevelocity, position, RPM, RPM_transimission

## per il momento ho solo simulato una trasmissione della trazione realistica, la quale mi ha permesso di determinare gli RPM della trasmissione (con un approssimazione seppur non eccessivamente grossolana)  ma ora devo capire quelli motore come variano