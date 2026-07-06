# ---------------- IMPORTS ----------------
import matplotlib.pyplot as plt

# ---------------- EV PARAMETERS ----------------
mass = 1500              # kg
acceleration = 1.2       # m/s^2
Cd = 0.3                 # drag coefficient
A = 2.2                  # frontal area (m^2)
rho = 1.225              # air density (kg/m^3)
Cr = 0.012               # rolling resistance
g = 9.81                 # gravity

battery_capacity = 50    # kWh

# ---------------- FORCES ----------------
force_acc = mass * acceleration
force_roll = Cr * mass * g

# ---------------- SPEED TEST ----------------
velocities = [10, 20, 30, 40, 50]   # m/s
powers = []

for velocity in velocities:
    force_drag = 0.5 * rho * Cd * A * velocity**2
    total_force = force_acc + force_drag + force_roll
    power = total_force * velocity
    powers.append(power)

# ---------------- GRAPH ----------------
plt.plot(velocities, powers, marker='o')
plt.title("EV Power vs Speed")
plt.xlabel("Speed (m/s)")
plt.ylabel("Power (W)")
plt.grid()
plt.tight_layout()
plt.show(block=False)

# ---------------- DRIVING CYCLES ----------------
city_cycle = [0, 20, 40, 30, 10, 0, 25, 35, 15, 0]
highway_cycle = [60, 70, 80, 90, 100, 90, 80, 70, 60]

# ---------------- FUNCTION ----------------
def simulate_cycle(speed_cycle):
    total_energy = 0   # Wh
    total_distance = 0 # km

    for speed in speed_cycle:
        v = speed * 1000 / 3600  # km/h → m/s

        force_drag = 0.5 * rho * Cd * A * v**2
        force_roll_local = Cr * mass * g
        total_force = force_drag + force_roll_local

        if v > 0:
            power = total_force * v   # Watts
            time_hours = 1 / 60       # 1 minute
            energy = power * time_hours   # Wh
        else:
            energy = 0

        distance = speed * (1/60)  # km

        total_energy += energy
        total_distance += distance

    efficiency = total_energy / total_distance if total_distance != 0 else 0
    return efficiency

# ---------------- RUN SIMULATION ----------------
city_eff = simulate_cycle(city_cycle)
highway_eff = simulate_cycle(highway_cycle)

print("\n--- Driving Cycle Analysis ---")
print("City Efficiency (Wh/km):", round(city_eff, 2))
print("Highway Efficiency (Wh/km):", round(highway_eff, 2))

# ---------------- RANGE CALCULATION ----------------
battery_wh = battery_capacity * 1000

city_range = battery_wh / city_eff
highway_range = battery_wh / highway_eff

print("\n--- Range ---")
print("City Range (km):", round(city_range, 2))
print("Highway Range (km):", round(highway_range, 2))
 
# ---------------- INSIGHT ----------------
if city_eff < highway_eff:
    improvement = ((highway_eff - city_eff) / highway_eff) * 100
    print("\nCity driving is more efficient by", round(improvement, 2), "% due to stop-go and lower speeds.")
else:
    print("\nHighway driving is more efficient due to steady speeds.")


# ---------------- EFFICIENCY COMPARISON GRAPH ----------------

modes = ["City", "Highway"]
efficiencies = [city_eff, highway_eff]

plt.figure(figsize=(6,5))
plt.bar(modes, efficiencies)

plt.title("EV Efficiency Comparison")
plt.ylabel("Efficiency (Wh/km)")
plt.xlabel("Driving Mode")

plt.grid(axis='y')

plt.show()


# ---------------- MULTI-EV COMPARISON ----------------

ev_data = {
    "Nexon EV": 465,
    "Tiago EV": 315,
    "Punch EV": 421,
    "Harrier EV": 600,
    "XUV400": 456,
    "BE.6": 550,
    "MG ZS EV": 461,
    "Kona EV": 490
}

names = list(ev_data.keys())
ranges = list(ev_data.values())

plt.figure(figsize=(10,5))

plt.bar(names, ranges)

plt.title("EV Claimed Range Comparison")
plt.xlabel("EV Models")
plt.ylabel("Range (km)")

plt.xticks(rotation=15)

plt.grid(axis='y')

plt.tight_layout()

plt.show()
