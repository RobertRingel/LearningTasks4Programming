"""
Moon Landing Simulation (with intelligent braking)
A Python program to simulate a lunar landing, teaching core programming and physics concepts.

Author: Robert Ringel, Faculty Informatics/Mathematics, HTWD – University of Applied Sciences  
Version: 10/2026  
License: CC BY-SA 4.0
"""

# === Constants ===
GRAVITY = 1.622               # Lunar gravity in m/s²
FUEL_CONSUMPTION_RATE = 10.0  # Fuel used per second per unit of thrust [l/s]
MAX_ALTITUDE = 1000.0         # Maximum initial altitude [m]
FUEL_VOLUME = 1500.0          # Total fuel available [l]
DT = 2.0                      # Time step [s] (simulation interval)
MANUAL_MODE = True            # Whether to use manual or automatic braking

# === Helper Functions ===

def calcDistance(a, v0, t):
    """
    Calculate distance traveled under constant acceleration.
    Formula: s = 0.5 * a * t² + v0 * t
    Args:
        a (float): Acceleration [m/s²]
        v0 (float): Initial velocity [m/s]
        t (float): Time [s]
    Returns:
        float: Distance fallen [m]
    """
    return 0.5 * a * t * t + v0 * t


def simulateDescent(gravity, braking_force, initial_velocity, altitude, time_step):
    """
    Simulate one time step of the descent.
    Applies net acceleration (gravity - braking) to update velocity and altitude.
    Args:
        gravity (float): Gravitational acceleration [m/s²]
        braking_force (float): Thrust-based deceleration [m/s²])
        initial_velocity (float): Velocity at start of time step [m/s]
        altitude (float): Current altitude [m]
        time_step (float): Duration of time step [s]
    Returns:
        tuple: (new_velocity, new_alt, distance_fallen)
    """
    # Net acceleration: gravity pulls down, braking force pushes up
    net_acceleration = gravity - braking_force

    # Update velocity using: v = v0 + a * t
    new_velocity = initial_velocity + net_acceleration * time_step

    # Calculate distance fallen during this time step
    distance_fallen = calcDistance(net_acceleration, initial_velocity, time_step)

    # Update altitude
    new_altitude = altitude - distance_fallen

    return new_velocity, new_altitude, distance_fallen


def printDisplay(time, velocity, altitude, distance_fallen, fuel):
    """
    Print the current state of the simulation in a formatted line.
    Args:
        time (float): Current simulation time [s]
        velocity (float): Current velocity [m/s]
        altitude (float): Current altitude [m]
        distance_fallen (float): Distance fallen in this time step [m]
        fuel (float): Remaining fuel [l]
    """
    print(f"Sec:{time:>5g} | {altitude:>6.1f}m | {velocity:>5.1f}m/s | Fuel:{fuel:>4.0f}l ", end="")
    printAltIndicator(altitude, distance_fallen)


def printAltIndicator(altitude, distance_fallen, MAX_ALT=1000):
    """
    Print a visual altitude indicator showing the lander's position and descent.
    Uses a bar to represent altitude and a "falling" segment to show distance fallen.
    Args:
        altitude (float): Current altitude [m]
        distance_fallen (float): Distance fallen in this step [m]
        MAX_ALT (float): Maximum atitude for scaling [m]
    """
    WIDTH = 80  # Width of the visual bar
    # Position of the lander in the bar (0 = bottom, WIDTH = top)
    pos = int(WIDTH * altitude / MAX_ALT)

    # Scale distance fallen to fit in the bar (every 5m = 1 character)
    ds5 = int(distance_fallen / 5)
    # Limit to avoid overwriting the lander or going beyond the bar
    ds5 = min(ds5, WIDTH - pos - 1)

    # Build the visual bar: | + empty space + lander (<) + descent trail (-)
    line = "|" + " "*pos + "<" + "-"*ds5
    print(f"{line:<90}", end=".")


def enterDecelerationFuel():
    """
    Prompt the user to enter how much retro-rocket fuel to burn.
    Ensures input is non-negative.
    Returns:
        int: Fuel to use [l]
    """
    fuel = int(input("Retro-Rocket Fuel [l]: "))
    return max(0, fuel)  # Clamp to zero if negative


def calculateDecelerationForce(velocity, altitude, gravity):
    """
    Calculate the required braking force to land safely at low altitude.
    Uses kinematic equation: v² = u² + 2as   : solve for required deceleration.
    Assumes a safe landing speed of 0 m/s at altitude 0.
    Args:
        velocity (float): Current velocity [m/s]
        altitude (float): Current altitude [m]
        gravity (float): Gravitational acceleration [m/s²]
    Returns:
        float: Required braking force [m/s²], capped between 0 and 50
    """
    # Avoid division by zero or negative altitude
    if altitude <= 0.001:
        return 0.0

    # Required deceleration to stop in remaining distance (using v² = u² + 2as)
    # Rearranged: a = (v² - u²) / (2s), but here we want to stop from current velocity
    # So: a_needed = (0 - v²) / (2 * h) → but we must also counteract gravity
    # Thus: a_needed = v² / (2 * (h + 0.5)) + g  (adding 0.5 to avoid instability at very low h)
    a_needed = velocity * velocity / (2 * (altitude + 0.5)) + gravity

    # Clamp to realistic range: 0 to 50 m/s² (max thrust)
    return max(0, min(50, a_needed))


# === MAIN PROGRAM ===
print(">>>>> Apollo 27 Moon Landing Simulation <<<<<")
print()
print("Task: Land savely with a touch-down speed <10km/h and >700l fuel remaining for later flight home.")
print("Current system parameters: MANUAL_MODE :", MANUAL_MODE)
print("                           ALTITUDE [m]:", MAX_ALTITUDE)
print("                           FUEL [l]    :", FUEL_VOLUME)
print("                           TIME INT [s]:", DT)
print()
input("Hit ENTER to release Lunar Landing Module from Apollo 27 Lunar Orbiter!")
print()

# Initialize simulation state
altitude = MAX_ALTITUDE
fuel = FUEL_VOLUME
velocity = 0.0
time = 0.0
distance_fallen = 0.0

# Main simulation loop
while altitude > 0.0:
    # Display current state
    printDisplay(time, velocity, altitude, distance_fallen, fuel)

    # Initialize braking and fuel usage
    braking_force = 0.0
    fuel_used = 0.0

    # Check if fuel is available
    if fuel > 0:
        if MANUAL_MODE:
            # Manual input: user decides how much fuel to burn
            fuel_used = enterDecelerationFuel()
            # Convert fuel to braking force (thrust): force = fuel / (time_step * consumption_rate)
            braking_force = fuel_used / (DT * FUEL_CONSUMPTION_RATE)
        else:
            # Automatic mode: calculate required braking at low altitude
            if altitude < 400.0:
                braking_force = calculateDecelerationForce(velocity, altitude, GRAVITY)
                # Calculate fuel needed for this braking force
                fuel_used = braking_force * DT * FUEL_CONSUMPTION_RATE
                # print(f": {fuel_used:.1f}l fuel used")
            else:
                # No braking at high altitude in auto mode
                braking_force = 0.0
                fuel_used = 0.0
            
            print(f": {fuel_used:.1f}l fuel used")
        # Update fuel supply
        fuel -= fuel_used
    else:
        # Out of fuel
        print("\nOut of fuel!")
        braking_force = 0.0
        fuel = 0.0

    # Update physics state for next time step
    velocity, altitude, distance_fallen = simulateDescent(GRAVITY, braking_force, velocity, altitude, DT)
    
    time += DT

# Final state at landing
altitude = 0.0
printDisplay(time, velocity, altitude, distance_fallen, fuel)

# Convert landing speed to km/h
landing_speed_kmh = velocity * 3.6

print(f"\nLanding speed [km/h]: {landing_speed_kmh:.1f}")

# Evaluate landing outcome
if landing_speed_kmh <= 10.0:
    print("Landing successful! Safely landed.")
elif landing_speed_kmh <= 30.0:
    print("Landing achieved, but hard. Damage possible.")
else:
    print("CRASH! Landing failed. Severe damage.")
