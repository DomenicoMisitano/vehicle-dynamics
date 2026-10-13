import numpy as np

def update_motion_step(F_tot, mass, velocity, dt, position, time, velocities, positions, times):
    a = F_tot / mass

    velocity = velocity + (a * dt)

    relativevelocity = velocity + 10

    position = position + (velocity * dt)

    time = time + dt

    velocities.append(velocity)
    positions.append(position)
    times.append(time)

    return velocity, relativevelocity, time, position