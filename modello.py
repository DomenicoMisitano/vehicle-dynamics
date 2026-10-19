from dynamics.data_managing.motion_step import update_motion_step
from dynamics.traction_managing.traction import traction_force
from dynamics.data_managing.data_plotting import plot_data
from dynamics.data_managing.periodic_data import show_data
from dynamics.data_managing.total_force import tot_force
from dynamics.gear_management.gear_selection import select_gear
from dynamics.gear_management.torque_interruption import simulate_torque_interruption
from dynamics.traction_managing.RPM_calculator import rpm_calculator
from dynamics.gear_management.clutch_engagement_sequence import run_clutch_engagement_sequence

density = 1.225
c_drag = 0.3
area = 2.2
velocity = 20
c_rr = 0.01
mass = 1500
relativevelocity = velocity + 10
angle = 5
t_engine = 250
i_gear = 3.2
i_diff = 3.5
eta = 0.9
wheel_radius = 0.32
mu =  0.9
gear = 0
r_f = 0.11
mu_gear = 0.35
F_smax = 9750


dt = 0.001
t_tot = 10
time = 0
position = 0

positions = []
times = []
velocities = []
gear_ratios = [5.087, 2.991, 2.035, 1.594, 1.286, 1.000]


for i in range(int(t_tot / dt)):
    if time >= t_tot:
        break

    previous_gear = gear

    RPM = rpm_calculator(velocity, gear, i_diff, wheel_radius, mu)

    gear, time, velocity, relativevelocity, position = select_gear(
        velocity, gear, mu, eta, mass,
        traction_force(velocity, gear, i_diff, eta, wheel_radius, mu, mass),
        mu_gear, r_f, F_smax, time, dt, RPM, wheel_radius,
        relativevelocity, position, velocities, positions, times,
        i_gear, i_diff
    )

    if gear == previous_gear:
        F_t = traction_force(velocity, gear, i_diff, eta, wheel_radius, mu, mass)

        F_tot, gear = tot_force(density, c_drag, area, relativevelocity, c_rr, mass, velocity, angle, gear, i_diff, eta, mu, wheel_radius)

        velocity, relativevelocity, time, position = update_motion_step(F_tot, mass, velocity, dt, position, time,
                                                                        velocities, positions, times)

        RPM = rpm_calculator(velocity, gear, i_diff, wheel_radius, mu)

        show_data(time, F_t, gear, RPM, i)

    else:
        counter = time

        F_t = traction_force(velocity, gear, i_diff, eta, wheel_radius, mu, mass)

        while time < counter + 0.7:
            velocity, relativevelocity, time, position = simulate_torque_interruption(times, velocities, positions, time, velocity, position, F_t, mass, dt, density, c_drag,
                                area, relativevelocity, c_rr, angle)

        F_t, time, velocity, relativevelocity, position = run_clutch_engagement_sequence(
            traction_force( velocity, gear, i_diff, eta, wheel_radius, mu, mass), mu_gear, eta, r_f, F_smax, time, dt, RPM,
            wheel_radius, mass, velocity, relativevelocity, position,
            velocities, positions, times, gear_ratios[gear], i_diff)

        RPM = rpm_calculator(velocity, gear, i_diff, wheel_radius, mu)

        show_data(time, F_t, gear, RPM, i)

plot_data(times, velocities, positions)
