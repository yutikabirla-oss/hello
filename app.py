import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page Setup
st.set_page_config(page_title="Project Bhu-Kavach | SIH 2026", layout="wide", page_icon="🚨")

# Custom UI CSS Styling
st.markdown("""
    <style>
    .header-style { font-size:40px !important; font-weight: bold; color: #0F172A; text-align: center; margin-bottom: 5px; }
    .sub-header { font-size:18px; color: #475569; text-align: center; margin-bottom: 25px; }
    .status-card { padding: 22px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 26px; color: white; margin-bottom: 20px; }
    .green-zone { background-color: #059669; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
    .yellow-zone { background-color: #D97706; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
    .red-zone { background-color: #DC2626; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# Main Dashboard Title
st.markdown("<div class='header-style'>🛡️ PROJECT BHU-KAVACH: Control Room Center</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'><b>SIH Problem Statement: SIH26001</b> | Ministry of Development of North Eastern Region (MDoNER)</div>", unsafe_allow_html=True)
st.divider()

# Sidebar Layout (Live Simulation Controls for Presentation)
st.sidebar.header("🎛️ Live Mesh Node Simulation")
st.sidebar.write("Judges ke samne parameters change karke live alert generate karein:")

moisture = st.sidebar.slider("💦 Mitti ki Nami (Soil Moisture %)", 0, 100, 35)
tilt = st.sidebar.slider("📐 Slope Angle Displacement (Degrees)", 0, 90, 3)
acoustic = st.sidebar.slider("🔊 Subterranean Acoustic Activity (dB)", 10, 120, 20)

st.sidebar.divider()
st.sidebar.subheader("📡 Offline Resilience Status")
st.sidebar.success("LoRa Mesh Grid State: OPERATIONAL")
st.sidebar.error("Cellular Network Status: BLACKOUT / DOWN")

# Core Conditional Threshold Logic
if moisture > 75 and tilt > 15 and acoustic > 80:
    alert_status = "🚨 EMERGENCY RED ALERT: LANDSLIDE IMMINENT"
    css_class = "red-zone"
    barrier = "❌ CLOSED (Auto-Dropped via Decentralized LoRa Signal)"
    siren = "🔊 ACTIVE SIREN BROADCASTING"
    evac_sms = "⚡ SENT: Emergency Multilingual Evacuation Alerts Triggered"
elif moisture > 55 or tilt > 8 or acoustic > 50:
    alert_status = "⚠️ WARNING YELLOW ALERT: HIGH ACCELERATION RISK"
    css_class = "yellow-zone"
    barrier = "⚠️ STANDBY (Pre-Alert Active, Road Clear)"
    siren = "🔕 STANDBY MODE"
    evac_sms = "⏳ STANDBY: Pre-Alert Dispatched to Local Rescue Units"
else:
    alert_status = "🟢 SYSTEM STATUS: STABLE & SAFE"
    css_class = "green-zone"
    barrier = "✅ OPEN (Traffic Moving Normally)"
    siren = "🔕 OFF"
    evac_sms = "💤 INACTIVE"

# Display Alert System Block
st.markdown(f"<div class='status-card {css_class}'>{alert_status}</div>", unsafe_allow_html=True)

# Main Telemetry Columns
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Soil Water Saturation", value=f"{moisture} %", delta="Critical Levels" if moisture > 75 else "Stable")
with col2:
    st.metric(label="Sub-surface Rock Shift (Tilt)", value=f"{tilt}°", delta="Unstable Slope" if tilt > 15 else "Normal")
with col3:
    st.metric(label="Acoustic Bedrock Stress", value=f"{acoustic} dB", delta="Micro-Fractures Active" if acoustic > 80 else "Quiet")

st.divider()

# Infrastructure Mitigation Panel
st.subheader("🤖 Automated Hardware Mitigation Actions")
box1, box2, box3 = st.columns(3)
box1.warning(f"**Smart Highway Toll Gate Blockade:** \n\n {barrier}")
box2.warning(f"**Field Hardware Siren System:** \n\n {siren}")
box3.warning(f"**NDRF Emergency Broadcast Gateway:** \n\n {evac_sms}")

st.divider()

# Advanced Map and Simulation Visualizer
st.subheader("🗺️ Live Regional Hazard Mapping & Predictive Analytics")
map_col, graph_col = st.columns([1, 1])

with map_col:
    st.write("**Northeast Border Zone Area Coordinates (Inferred Mesh Nodes)**")
    # Coordinates for Northeast Highway Hotspot (Near Guwahati-Shillong Route Area)
    map_data = pd.DataFrame({
        'lat': [26.1445, 25.5788, 25.7281],
        'lon': [91.7362, 91.8931, 92.4258],
        'Risk Node Level': ['Zone A (Primary Spike)', 'Zone B (Smart Barrier Point)', 'Zone C (Highway Node)']
    })
    st.map(map_data, zoom=7)

with graph_col:
    st.write("**Pre-Crash Acoustic Burst Analysis Time-Series**")
    fig, ax = plt.subplots(figsize=(6, 3.8))
    time_axis = np.linspace(0, 50, 200)
    # Generate frequency curves based on user input stress levels
    noise_curve = np.sin(time_axis) * (acoustic / 8) + np.random.normal(0, 1, 200)
    ax.plot(time_axis, noise_curve, color='#DC2626' if acoustic > 80 else '#D97706' if acoustic > 50 else '#0F172A', lwd=1.5)
    ax.set_ylabel("Subterranean Rock Burst Amplitude")
    ax.set_xlabel("Time (T-Minus Minutes to Displacement)")
    st.pyplot(fig)
