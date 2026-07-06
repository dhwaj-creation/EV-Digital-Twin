import streamlit as st
import matplotlib.pyplot as plt
import time
st.set_page_config(page_title="EV Digital Twin", layout="wide")

st.set_page_config(
    page_title="EV Digital Twin",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 EV Digital Twin Dashboard")
st.subheader("Real-Time Electric Vehicle Simulation")


# ---------------- EV MODELS ----------------
ev_models = {
    "Tata Tiago EV (24 kWh)": {"battery": 24000, "mass": 1300},
    "Tata Punch EV (35 kWh)": {"battery": 35000, "mass": 1600},
    "Mahindra XUV400 (39 kWh)": {"battery": 39000, "mass": 1860},
    "Tata Nexon EV (40 kWh)": {"battery": 40000, "mass": 1700},
    "Tata Curvv EV (45 kWh)": {"battery": 45000, "mass": 1780},
    "MG ZS EV (50 kWh)": {"battery": 50000, "mass": 1850},
    "Tata Harrier EV (60 kWh est)": {"battery": 60000, "mass": 2200},
    "Mahindra BE.6 (60 kWh est)": {"battery": 60000, "mass": 2115},
    "Hyundai Kona EV (64 kWh)": {"battery": 64000, "mass": 1740}
}

st.sidebar.title("Control panel")
st.sidebar.subheader("Vehicle")
selected_ev = st.sidebar.selectbox("Choose EV Model", list(ev_models.keys()))
battery_capacity = ev_models[selected_ev]["battery"]
mass = ev_models[selected_ev]["mass"]

# ---------------- DRIVING MODE ----------------
st.sidebar.subheader("Driving")
driving_mode = st.sidebar.selectbox(
    "Driving Mode",
    ["India (City)", "Europe (Mixed)", "USA (Highway)"]
)

if driving_mode == "India (City)":
    acceleration = 1.5
    regen_efficiency = 0.4
elif driving_mode == "Europe (Mixed)":
    acceleration = 1.2
    regen_efficiency = 0.3
else:
    acceleration = 0.8
    regen_efficiency = 0.2

# ---------------- INPUT ----------------
st.sidebar.subheader("speed")
speed = st.sidebar.slider("Select Speed (km/h)", 10, 120, 60)

# ---------------- PARAMETERS ----------------
Cd = 0.3
A = 2.2
rho = 1.225
Cr = 0.012
g = 9.81

# ---------------- CALCULATIONS ----------------
velocity = speed * 1000 / 3600

force_drag = 0.5 * rho * Cd * A * velocity**2
force_roll = Cr * mass * g
total_force = force_drag + force_roll

power = total_force * velocity

energy = power / velocity * (1000 / 3600)
effective_energy = energy * (1 - regen_efficiency)

range_km = (battery_capacity / effective_energy) * 0.75

# ---------------- SPEED ANALYSIS ----------------
velocities_kmh = list(range(10, 121, 5))
velocities = [v * 1000 / 3600 for v in velocities_kmh]

powers = []
energies = []
ranges = []

for v in velocities:
    fd = 0.5 * rho * Cd * A * v**2
    fr = Cr * mass * g
    tf = fd + fr
    p = tf * v

    energy = p / v * (1000 / 3600)
    effective_energy = energy * (1 - regen_efficiency)
    r = battery_capacity / effective_energy

    powers.append(p)
    energies.append(effective_energy)
    ranges.append(r)

# ---------------- AI BEST SPEED ----------------
max_range = max(ranges)
best_speed = velocities_kmh[ranges.index(max_range)]

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

col1.metric("⚡ Power (W)", round(power, 2))
col2.metric("🔋 Energy (Wh/km)", round(effective_energy, 2))
col3.metric("📏 Range (km)", round(range_km, 2))

st.markdown("## ⚡ EV Digital Twin Dashboard")

st.divider()

st.subheader("🚗 Vehicle Details")
st.write("Model:", selected_ev)
st.write("Battery Capacity:", battery_capacity / 1000, "kWh")

st.subheader("🛣️ Driving Conditions")
st.write("Mode:", driving_mode)
st.write("Regeneration Efficiency:", regen_efficiency)

st.divider()

st.subheader("📊 Performance Output")

st.metric("🔋 Battery Capacity (kWh)", battery_capacity / 1000)
st.write("Driving Mode:", driving_mode)
st.write("Regen Efficiency:", regen_efficiency)

# ---------------- AI INSIGHT ----------------
st.subheader("🤖 Smart Recommendation")

st.success(f"Best Speed for Maximum Range: {best_speed} km/h")

if speed > best_speed:
    st.warning("⚠️ Driving faster than optimal reduces range.")
elif speed < best_speed:
    st.info("ℹ️ You can increase speed slightly without major loss.")
else:
    st.success("✅ You are driving at optimal efficiency!")

# ---------------- MODE INSIGHT ----------------
st.subheader("📊 Driving Insight")

if driving_mode == "India (City)":
    st.write("Higher regeneration improves efficiency and range.")
elif driving_mode == "USA (Highway)":
    st.write("Higher speeds increase drag, reducing range.")
else:
    st.write("Balanced driving gives moderate efficiency.")

# ---------------- GRAPHS ----------------
col4, col5 = st.columns(2)

with col4:
    fig1, ax1 = plt.subplots()
    ax1.plot(velocities_kmh, ranges, marker='o')
    ax1.set_title("Range vs Speed")
    ax1.set_xlabel("Speed (km/h)")
    ax1.set_ylabel("Range (km)")
    ax1.grid()
    fig1.tight_layout()
    st.pyplot(fig1)

with col5:
    fig2, ax2 = plt.subplots()
    ax2.plot(velocities_kmh, energies, marker='o')
    ax2.set_title("Energy vs Speed")
    ax2.set_xlabel("Speed (km/h)")
    ax2.set_ylabel("Energy (Wh/km)")
    ax2.grid()
    fig2.tight_layout()
    st.pyplot(fig2)

st.subheader("Insights")

if driving_mode == "India (City)":
    st.write("Higher regeneration improves efficiency and range.")
elif driving_mode == "USA (Highway)":
    st.write("Higher speeds increase drag, reducing range.")
else:
    st.write("Balanced driving gives moderate efficiency.")

# ---------------- SMART EV JOURNEY SIMULATION ----------------

import time

st.divider()
st.subheader("🚗 Live EV Journey Simulation")

# Journey settings
st.sidebar.subheader("Journey")
journey_distance = st.sidebar.slider(
    "🛣️ Select Journey Distance (km)",
    1,
    500,
    50
)

# Driving mode efficiency factor
mode_factor = {
    "Indian": 0.85,
    "European": 1.0,
    "American": 1.15
}

selected_factor = mode_factor.get(driving_mode, 1.0)

# Estimated energy usage
energy_per_km = effective_energy * selected_factor

# Total usable battery
usable_battery = battery_capacity * 0.9

# Initial battery %
battery_percent = 100

# UI placeholders
progress_bar = st.progress(0)
distance_text = st.empty()
battery_text = st.empty()

journey_completed = True

for km in range(journey_distance + 1):

    # Distance progress
    progress = int((km / journey_distance) * 100)
    progress_bar.progress(progress)

    # Energy used
    energy_used = km * energy_per_km

    # Battery left
    battery_left = usable_battery - energy_used

    battery_percent = (battery_left / usable_battery) * 100

    if battery_percent <= 0:
        battery_percent = 0
        journey_completed = False

        st.error("🔴 Vehicle Stopped - Battery Depleted")

        st.warning(
        f"Journey interrupted at {km} km. Recharge required."
    )

        break
    
    if battery_percent < 0:
        battery_percent = 0

    # Display updates
    distance_text.metric(
        "📍 Distance Travelled",
        f"{km} km"
    )

    battery_text.metric(
        "🔋 Battery Remaining",
        f"{round(battery_percent,1)} %"
    )

    time.sleep(0.15)

if journey_completed:
    st.success("✅ Journey Completed")

st.divider()
st.caption("Built by Dhwaj Jain | EV Digital Twin Project")
