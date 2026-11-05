"""
Moon Landing Simulation Module

This module provides a set of functions for simulating the descent and landing of a spacecraft on the Moon.
It models the physics of descent including gravitational acceleration, thrust-based deceleration,
velocity and altitude updates over time steps, and a scoring system for evaluating landing performance.

The simulation assumes:
- Constant gravitational acceleration on the Moon (~1.62 m/s²)
- Thrust is applied in discrete time steps based on fuel consumption
- Fuel flow rate and burn duration determine the deceleration force
- The spacecraft's motion is governed by Newtonian mechanics

This module is designed for use in educational simulations, game development, or physics demonstrations
of lunar landing scenarios.

Author: Robert Ringel   License: CC-BY-SA 4.0  version: November 2026
"""


def calc_decel_force(fuel_volume, duration, fuel_flow_rate):
    """
    Calculate the deceleration force [m/s²] produced by burning a given volume
    of fuel over a specified duration at a given fuel flow rate.

    Args:
        fuel_volume (float): Volume of fuel burned in the current time step [l]
        duration (float): Duration of the burn [s]
        fuel_flow_rate (float): Fuel burn rate [l/s]

    Returns:
        float: Deceleration force [m/s²] produced by the fuel burn
    """
    decel_force = fuel_volume / (duration * fuel_flow_rate)
    return decel_force


def calc_fall_distance(acceleration, velocity, duration):
    """
    Calculate the distance fallen during a time interval given initial velocity
    and constant acceleration (e.g., net gravity minus braking).

    Args:
        acceleration (float): Net acceleration acting on the spacecraft [m/s²]
        velocity (float): Initial velocity at start of the time interval [m/s]
        duration (float): Time interval over which the motion occurs [s]

    Returns:
        float: Distance fallen during the time interval [m]
    """
    distance = 0.5 * acceleration * duration ** 2 + velocity * duration
    return distance


def simulate_descent_step(gravity, braking_force, initial_velocity, altitude, time_step):
    """
    Simulate one time step of the descent.
    Applies net acceleration (gravity - braking) to update velocity and altitude.

    Args:
        gravity (float): Gravitational acceleration [m/s²]
        braking_force (float): Thrust-based deceleration [m/s²]
        initial_velocity (float): Velocity at start of time step [m/s]
        altitude (float): Current altitude [m]
        time_step (float): Duration of time step [s]

    Returns:
        tuple: (new_velocity, new_altitude, distance_fallen)
    """
    # Net acceleration: gravity pulls down, braking force pushes up
    net_acceleration = gravity - braking_force

    # Update velocity using: v = v0 + a * t
    new_velocity = initial_velocity + net_acceleration * time_step

    # Calculate distance fallen during this time step
    distance_fallen = calc_fall_distance(net_acceleration, initial_velocity, time_step)

    # Update altitude
    new_altitude = altitude - distance_fallen

    return new_velocity, new_altitude, distance_fallen


def calc_landing_score(velocity, rem_fuel):
    """
    Calculate a landing score based on the final velocity and remaining fuel.
    The score is proportional to remaining fuel and inversely proportional to velocity.
    If no fuel remains, the score is zero.

    Args:
        velocity (float): Final landing velocity [m/s]
        rem_fuel (float): Remaining fuel after landing [kg]

    Returns:
        float: Landing score (higher is better). Returns 0.0 if no fuel remains.
    """
    factor = 10.0
    if rem_fuel <= 0.0:
        return 0.0
    score = factor * rem_fuel / velocity
    return score

