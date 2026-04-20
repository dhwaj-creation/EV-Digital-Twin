import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="EV Digital Twin", layout="wide")

st.title("⚡ EV Digital Twin - Advanced Dashboard")

ev_models = {
    # Tata
    "Tata Nexon EV (40 kWh)": 40000,
    "Tata Curvv EV (45 kWh)": 45000,
    "Tata Tiago EV (24 kWh)": 24000,
    "Tata Punch EV (35 kWh)": 35000,
    "Tata Harrier EV (60 kWh - est)": 60000,

    # Mahindra
    "Mahindra BE.6 (39 kWh)": 39000,
    "Mahindra XEV.9E (34.5 kWh)": 34500,
    "Mahindra XEV.9S (60 kWh - est)": 60000,

    # Others
    "MG ZS EV (50 kWh)": 50000,
    "Hyundai CRETA EV (64 kWh)": 64000
}

selected_ev = st.selectbox("Choose EV Model", list(ev_models.keys()))
battery_capacity = ev_models[selected_ev]

# ---------------- INPUT ----------------
speed = st.slider("Select Speed (km/h)", 10, 120, 60)

# ---------------- PARAMETERS ----------------
mass = 1500
Cd = 0.3
A = 2.2
rho = 1.225
Cr = 0.012
g = 9.81
battery_capacity = 50000

# ---------------- CALCULATIONS ----------------
velocity = speed * 1000 / 3600

force_drag = 0.5 * rho * Cd * A * velocity**2
force_roll = Cr * mass * g
total_force = force_drag + force_roll

power = total_force * velocity
energy = power / velocity * (1000 / 3600)
range_km = battery_capacity / energy

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
    e = p / v * (1000 / 3600)
    r = battery_capacity / e

    powers.append(p)
    energies.append(e)
    ranges.append(r)

max_range = max(ranges)
best_speed = velocities_kmh[ranges.index(max_range)]

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

col1.metric("⚡ Power (W)", round(power, 2))
col2.metric("🔋 Energy (Wh/km)", round(energy, 2))
col3.metric("📏 Range (km)", round(range_km, 2))

st.write("Battery Capacity (Wh):", battery_capacity)

# ---------------- AI INSIGHT ----------------
st.subheader("🤖 Smart Recommendation")

st.success(f"Best Speed for Maximum Range: {best_speed} km/h")

if speed > best_speed:
    st.warning("⚠️ You are driving faster than optimal. Range is decreasing.")
elif speed < best_speed:
    st.info("ℹ️ You can increase speed slightly without losing much efficiency.")
else:
    st.success("✅ You are driving at optimal efficiency!")

# ---------------- GRAPHS ----------------
col4, col5 = st.columns(2)

with col4:
    fig1, ax1 = plt.subplots()
    ax1.plot(velocities_kmh, ranges, marker='o')
    ax1.set_title("Range vs Speed")
    ax1.set_xlabel("Speed (km/h)")
    ax1.set_ylabel("Range (km)")
    ax1.grid()
    st.pyplot(fig1)

with col5:
    fig2, ax2 = plt.subplots()
    ax2.plot(velocities_kmh, energies, marker='o')
    ax2.set_title("Energy vs Speed")
    ax2.set_xlabel("Speed (km/h)")
    ax2.set_ylabel("Energy (Wh/km)")
    ax2.grid()
    st.pyplot(fig2)