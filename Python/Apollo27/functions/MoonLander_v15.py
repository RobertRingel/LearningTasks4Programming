"""
Moon Landing Simulation 
A Python program to simulate a lunar landing, teaching core programming and physics concepts.

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 11/2026  
License: CC BY-SA 4.0
"""

import lunar_physics_model as lpm

def print_alt_indicator(altitude, distance_fallen, max_alt=1000.0):
    """
    Print a visual altitude indicator showing the lander's position and descent.
    Uses a bar to represent altitude and a "falling" segment to show distance fallen.

    Args:
        altitude (float): Current altitude [m]
        distance_fallen (float): Distance fallen in this step [m]
        max_alt (float): Maximum altitude for scaling [m]
    """
    width = 80  # Width of the visual bar
    # Position of the lander in the bar (0 = bottom, width = top)
    pos = int(width * altitude / max_alt)
    if pos > width:
        pos = width

    # Scale distance fallen to fit in the bar (every 5m = 1 character)
    ds5 = int(distance_fallen / 5)
    # Limit to avoid overwriting the lander or going beyond the bar
    ds5 = min(ds5, width - pos - 1)

    # Build the visual bar: | + empty space + lander (<) + descent trail (-)
    line = "|" + " " * pos + "<" + "-" * ds5
    print(f"{line:<90}", end=".")


# -------------- main program --------------------------

print(">>> Moon landing with braking: <<< ")
print("    task 15")
print()

g = 1.622     # Moon gravity (m/s²)
f = 1500.0    # Initial volume of braking fuel [l]
fbr = 10.0    # Fuel burn rate per second [l/s]
h = 1000.0    # Initial altitude: 1000 m above the Moon
v = 0.0       # Initial falling velocity (m/s)
ds = 0.0      # Distance fallen in the current step [m]
b = 0.0       # Braking acceleration (m/s²)
t = 0.0       # Elapsed time [s]
dT = 1.0      # Time increment (1 s)

while h > 0.0:  # One loop per second until touch down
    print(f"Sec:{t:>5g} | {h:>6.1f}m | {v:>5.1f}m/s | Fuel:{f:>4.0f}l ", end=":")
    print_alt_indicator(h, ds)

    if f > 0.0:
        fb = input("Braking fuel (0–50): ")
        fb = float(fb)
    else:
        fb = 0.0
        print()

    f = f - fb       # Fuel consumption
    b = lpm.calc_deceleration_force(fb, dT, fbr)
    v, h, ds = lpm.simulate_descent_step(g, b, v, h, dT)
    t = t + dT

    if f < 0.0:
        print("Fuel exhausted!!!")
        f = 0.0

print("Touch down.")
v = 3.6 * v
print("    ... speed:", v, "km/h")
scr = lpm.calc_landing_score(v, f)  
print("Landing score:", scr)