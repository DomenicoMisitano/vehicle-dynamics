import matplotlib.pyplot as plt
import numpy as np

def plot_data(times, velocities, positions):
    plt.plot(times, velocities)
    plt.xlabel("time [s]")
    plt.ylabel("velocity [m/s]")
    plt.title("velocity over time")
    plt.show()

    plt.plot(times, positions)
    plt.xlabel("time [s]")
    plt.ylabel("position [m]")
    plt.title("position over time")
    plt.show()
