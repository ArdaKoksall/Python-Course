# Constants
DELTA_T = 0.01  # Time interval in seconds
g = 9.81  # Acceleration due to gravity in m/s^2

# Initial conditions
initial_velocity = float(input("Enter the initial velocity (m/s): "))
v = initial_velocity
s = 0.0
t = 0.0

# Simulation loop
while s >= 0:
    # Update position and velocity
    s = s + v * DELTA_T
    v = v - g * DELTA_T
    t = t + DELTA_T

    # Output the position and exact formula value every second
    if int(t / DELTA_T) % int(1 / DELTA_T) == 0:
        exact_position = -0.5 * g * t**2 + initial_velocity * t
        print(f"Time: {int(t)}s, Simulated Position: {s:.2f}m, Exact Position: {exact_position:.2f}m")