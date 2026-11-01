EV Digital Twin

A Physics-Based Electric Vehicle Simulation and Range Estimation System

Developed by: Dhwaj Jain
Technologies: Python · Streamlit · Matplotlib
Project Type: Independent Engineering Project

Overview

EV Digital Twin is an interactive, Python-based simulation application designed to explore electric vehicle performance, energy consumption, and estimated driving range under different driving conditions.

The application combines simplified vehicle-dynamics calculations with an interactive dashboard and visualizations. Users can select an electric vehicle model, adjust driving parameters, explore estimated energy use, and simulate a journey while monitoring the remaining battery level.

The project is an independent exploration of electric mobility, engineering calculations, and software development.

Project Objectives

- Explore the relationship between vehicle speed, road resistance, and power demand.
- Estimate energy consumption and driving range using simplified physical models.
- Compare simulation behaviour across different vehicle configurations and driving modes.
- Visualize calculated results through an interactive dashboard.
- Simulate a journey and track the estimated battery state as distance increases.

Key Features

Vehicle Selection

Choose from a selection of electric vehicle models with configured battery capacities and vehicle masses.

Energy Consumption Analysis

Estimate road-load forces and energy use using vehicle parameters and simplified physical equations.

Driving Modes

Explore different driving-mode assumptions that affect the simulation's energy-use calculations.

Range Estimation

Calculate an indicative driving-range estimate based on battery capacity and modelled energy consumption.

Interactive Dashboard

Adjust inputs and view calculated performance metrics without manually editing the source code.

Data Visualization

View graphs illustrating relationships between speed, power demand, energy consumption, and estimated range.

Journey Simulation

Choose a journey distance and observe a simulated progression of distance travelled and battery remaining, including a battery-depletion condition.

Engineering Methodology

The simulation uses a simplified vehicle-dynamics model.

1. Aerodynamic Drag

The aerodynamic drag force is estimated using:

"F_drag = 0.5 × ρ × Cd × A × v²"

Where:

- "ρ" is air density.
- "Cd" is the aerodynamic drag coefficient.
- "A" is the vehicle's frontal area.
- "v" is vehicle speed in metres per second.

2. Rolling Resistance

Rolling resistance is estimated using:

"F_roll = Cr × m × g"

Where:

- "Cr" is the rolling-resistance coefficient.
- "m" is vehicle mass.
- "g" is gravitational acceleration.

3. Road-Load Force and Power

The total modelled road-load force is:

"F_total = F_drag + F_roll"

The corresponding power estimate is:

"P = F_total × v"

4. Energy and Range Estimation

The model uses road-load calculations and configured battery capacity to estimate energy use and driving range. The implementation also applies simplified regenerative-braking and driving-mode assumptions.

These calculations are intended for educational simulation. They do not represent a fully validated vehicle model or a guarantee of real-world driving range.

Technology Stack

- Python: Simulation logic and calculations.
- Streamlit: Interactive web application and dashboard.
- Matplotlib: Graphs and data visualization.

Running the Project Locally

Prerequisites

- Python installed on your computer.
- Git, if you want to clone the repository.

Installation

Clone the repository:

git clone https://github.com/dhwaj-creation/EV-Digital-Twin.git
cd EV-Digital-Twin

Install the dependencies:

python3 -m pip install -r requirements.txt

Run the application:

python3 -m streamlit run app.py

The terminal will display a local address that you can open in your browser.

Project Links

- Source code: https://github.com/dhwaj-creation/EV-Digital-Twin
- Live application: https://github.com/dhwaj-creation/EV-Digital-Twin/tree/main

Current Scope and Limitations

This project is a simplified, physics-based EV simulation prototype.

- Vehicle specifications are configured inputs and may not reflect every production variant.
- Real-world energy use depends on factors such as temperature, terrain, traffic, tyre condition, HVAC use, battery health, and driving behaviour.
- Regenerative braking and driving-mode effects use simplified assumptions.
- The application is not connected to a physical vehicle or live vehicle telemetry.
- Simulation outputs should not be treated as certified performance measurements.

Future Development

Potential improvements include:

- Validating estimates against published vehicle specifications and measured driving data.
- Adding more detailed driving cycles and road-gradient modelling.
- Improving battery-state and charging models.
- Comparing simulated results with real-world observations.
- Exploring data-driven or machine-learning methods after collecting suitable data.
- Adding automated tests and documenting model accuracy.

Learning Outcomes

This project provides an opportunity to explore:

- Python application development.
- Fundamental vehicle-dynamics equations.
- Energy consumption and range estimation.
- Interactive data visualization.
- Software deployment and technical documentation.
- The importance of assumptions, model validation, and engineering limitations.

Author

Dhwaj Jain

Independent engineering project exploring electric vehicles, simulation, and software development.
