# EV Digital Twin - Phase 1 Upgrade

# Constants
mass = 1200            # kg
acceleration = 1.5     # m/s^2
velocity = 30          # m/s
g = 9.81

# Aerodynamics
rho = 1.225            # air density
Cd = 0.3               # drag coefficient
A = 2.2                # frontal area

# Rolling resistance
Cr = 0.015

# Calculations
force_acc = mass * acceleration

force_drag = 0.5 * rho * Cd * A * velocity**2

force_roll = Cr * mass * g

total_force = force_acc + force_drag + force_roll

power = total_force * velocity

# Output
print("Acceleration Force:", force_acc)
print("Drag Force:", force_drag)
print("Rolling Resistance:", force_roll)
print("Total Force:", total_force)
print("Power Required:", power)
