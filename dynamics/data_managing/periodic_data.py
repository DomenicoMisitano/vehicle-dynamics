import numpy as np

def show_data(time, F_t, gear, RPM, i):
    if i % 100 == 0:
        print("t:", round(time, 1), "F_t:", round(F_t, 1), "gear:", gear, "RPM:", RPM)