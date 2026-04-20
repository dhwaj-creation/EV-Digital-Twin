import matplotlib.pyplot as plt

# EV Digital Twin - Phase 1 Upgrade

# Vehicle parameters
mass = 1500
acceleration = 1.2
Cd = 0.3
A = 2.2
rho = 1.225
Cr = 0.012
g = 9.81

# Battery
battery_capacity = 50000  # in Wh(50 kWh battery)
regen_efficiency = 0.3   # 30% energy recovery

time_minutes = list(range(0, 61, 5))  # 0 to 60 minutes

chosen_speed_kmh = 60
chosen_speed = chosen_speed_kmh * 1000 / 3600

# Forces
force_acc = mass * acceleration
force_roll = Cr * mass * g

# Speeds (real-world)
velocities_kmh = list(range(10, 121, 5))
velocities = [v * 1000 / 3600 for v in velocities_kmh]

# Power calculation
powers = []

for velocity in velocities:
    force_drag = 0.5 * rho * Cd * A * velocity**2
    total_force = force_acc + force_drag + force_roll
    power = total_force * velocity
    powers.append(power)

# Energy consumption (Wh/km)
energy_per_km = []

for power, velocity in zip(powers, velocities):
    energy = power / velocity  # W / (m/s) = J/m
    energy_Wh_km = energy * (1000 / 3600)  # convert to Wh/km
    energy_per_km.append(energy_Wh_km)

# Regenerative braking
recovered_energy = []

for energy in energy_per_km:
    recovered = energy * regen_efficiency
    recovered_energy.append(recovered)

# Effective energy after regen
effective_energy = []

for energy, recovered in zip(energy_per_km, recovered_energy):
    net = energy - recovered
    effective_energy.append(net)

# Range calculation
ranges = []

for energy in energy_per_km:
    range_km = battery_capacity / energy
    ranges.append(range_km)

# Find best speed for maximum range
max_range = max(ranges)
best_index = ranges.index(max_range)
best_speed = velocities_kmh[best_index]
print("Best Speed for Maximum Range:", best_speed, "km/h")
print("Maximum Range:", round(max_range, 2), "km")

# Find energy at chosen speed
index = velocities_kmh.index(chosen_speed_kmh)
energy_use = effective_energy[index]

# Simulate battery SOC over time
soc = []
battery_remaining = battery_capacity

for t in time_minutes:
    distance = chosen_speed_kmh * (t / 60)  # km travelled
    energy_used = distance * energy_use     # Wh used
    remaining = battery_capacity - energy_used
    soc_percent = (remaining / battery_capacity) * 100
    soc.append(max(soc_percent, 0))


# Power vs Speed graph
plt.plot(velocities_kmh, powers, marker='o')
plt.title("EV Power vs Speed")
plt.xlabel("Speed (km/h)")
plt.ylabel("Power Required (W)")
plt.grid(True)


# Energy vs Speed graph
plt.figure()
plt.plot(velocities_kmh, energy_per_km, marker='o')
plt.title("EV Energy Consumption vs Speed")
plt.xlabel("Speed (km/h)")
plt.ylabel("Energy Consumption (Wh/km)")
plt.grid()

# Range vs Speed graph (with regen)
plt.figure()
plt.plot(velocities_kmh, ranges, marker='o')
plt.title("EV Range vs Speed")
plt.xlabel("Speed (km/h)")
plt.ylabel("Range (km)")
plt.grid()

# Battery State of Charge graph
plt.figure()
plt.plot(time_minutes, soc, marker='o')
plt.title("Battery State of Charge vs Time")
plt.xlabel("Time (minutes)")
plt.ylabel("Battery (%)")
plt.grid()

# Show al graphs
plt.show()