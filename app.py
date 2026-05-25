import streamlit as st
import time
import random

# 1. Framework Configuration & Page Nodes
st.set_page_config(
    page_title="THE BLUETOOTH DASHBOARD PANEL",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session States for Devices to manage persistent states
if "devices" not in st.session_state:
    st.session_state.devices = {
        "DEV-8891 (Sony WH-1000XM4)": {"status": "Disconnected", "power": "OFF", "mac": "00:1A:7D:DA:71:11", "type": "Audio / Headset"},
        "DEV-4412 (Gesner iPhone 15 Pro)": {"status": "Connected", "power": "ON", "mac": "4C:56:9D:E1:2A:4F", "type": "Mobile Handset"},
        "DEV-1092 (Logitech MX Master 3S)": {"status": "Disconnected", "power": "ON", "mac": "74:5E:1C:89:B2:CC", "type": "Input / Mouse"},
        "DEV-3345 (Samsung Smart TV 4K)": {"status": "Disconnected", "power": "OFF", "mac": "A4:70:D6:11:90:BB", "type": "Display Screen"},
        "DEV-7762 (Garmin Fenix Pro Watch)": {"status": "Connected", "power": "ON", "mac": "38:C9:86:F2:44:A1", "type": "Wearable / IoT"}
    }
if "global_power" not in st.session_state:
    st.session_state.global_power = "ON"
if "logs" not in st.session_state:
    st.session_state.logs = ["💡 Panel Engine Online.", "📡 Core Bluetooth Scanning Protocols initialized..."]

# 2. Cyberpunk Technology Theme CSS Injection Layer
st.markdown(
    """
    <style>
    /* Neon Dark Control Panel Sheet */
    .stApp {
        background-color: #0b0f19;
        color: #e2e8f0;
    }
    
    /* Colorful Cyberpunk Gradients */
    .panel-title {
        text-align: center;
        font-weight: 900;
        font-size: 3rem;
        background: linear-gradient(135deg, #ff007f, #7928ca, #00dfd8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2px;
        letter-spacing: 2px;
        filter: drop-shadow(0px 2px 10px rgba(0, 223, 216, 0.3));
    }
    
    /* Vibrant Developer Credentials */
    .author-strip {
        text-align: center;
        font-size: 1.1rem;
        background: linear-gradient(90deg, #00dfd8, #00f260, #ff007f);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        margin-bottom: 30px;
        letter-spacing: 0.5px;
    }
    
    /* Device Cards Container Style */
    .device-card {
        background: #151f32;
        border: 1px solid #223452;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    
    /* Dynamic Power Badges */
    .badge-on {
        background-color: #059669;
        color: #ffffff !important;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.85rem;
        display: inline-block;
    }
    .badge-off {
        background-color: #dc2626;
        color: #ffffff !important;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.85rem;
        display: inline-block;
    }
    
    /* Strong White Explicit Targets for Metrics */
    div[data-testid="stMetricLabel"] > div {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1.1rem;
    }
    div[data-testid="stMetricValue"] > div {
        color: #ffffff !important;
        font-weight: 900 !important;
        font-size: 2.2rem;
    }
    
    /* Terminal Output Panel Box */
    .terminal-box {
        background-color: #05070c;
        border-left: 4px solid #00dfd8;
        padding: 15px;
        font-family: 'Courier New', Courier, monospace;
        color: #38bdf8;
        font-size: 0.9rem;
        border-radius: 0 8px 8px 0;
        max-height: 250px;
        overflow-y: auto;
    }
    
    /* Strong White Copyright Footer */
    .strong-white-footer {
        text-align: center; 
        margin-top: 50px; 
        font-size: 0.85rem; 
        color: #ffffff !important; 
        font-weight: 700 !important;
        border-top: 1px solid #223452; 
        padding-top: 20px;
        letter-spacing: 1px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================================
# 🎛️ CONTROL PANEL HEADER MARKS
# =========================================================================
st.markdown('<h1 class="panel-title">THE BLUETOOTH DASHBOARD PANEL</h1>', unsafe_allow_html=True)
st.markdown(
    '<div class="author-strip">'
    '⚡ Built by Gesner Deslandes &nbsp;|&nbsp; '
    '📥 Phone: (509)-47385663 &nbsp;|&nbsp; '
    '✉️ Email: deslandes78@gmail.com'
    '</div>', 
    unsafe_allow_html=True
)

# =========================================================================
# 📊 TOP GLOBAL MATRIX READOUT NODES (STRONG WHITE TEXT)
# =========================================================================
total_devs = len(st.session_state.devices)
active_conn = sum(1 for d in st.session_state.devices.values() if d["status"] == "Connected")
power_on_count = sum(1 for d in st.session_state.devices.values() if d["power"] == "ON")

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric(label="Global Antenna State", value=st.session_state.global_power)
with m2:
    st.metric(label="Total Tracked Hardware", value=str(total_devs))
with m3:
    st.metric(label="Active Linked Channels", value=str(active_conn))
with m4:
    st.metric(label="Radio Modules Online", value=str(power_on_count))

st.markdown("---")

# =========================================================================
# 🛠️ SIDEBAR MANAGEMENT HUB
# =========================================================================
st.sidebar.markdown("## ⚡ Master Transceiver System")
st.sidebar.markdown("---")

# Master system switch toggle
global_power_toggle = st.sidebar.toggle("Radio Frequency Power Transmitter", value=(st.session_state.global_power == "ON"))
st.session_state.global_power = "ON" if global_power_toggle else "OFF"

st.sidebar.markdown("---")
st.sidebar.markdown("### 📡 Manual Device Injector")
new_name = st.sidebar.text_input("Device Common Identifier:", placeholder="e.g. Beats Studio Buds")
new_type = st.sidebar.selectbox("Device Spectrum Bracket:", ["Audio / Headset", "Mobile Handset", "Input / Peripheral", "Wearable / IoT"])

if st.sidebar.button("⚡ Inject Device Into Matrix"):
    if new_name:
        generated_id = f"DEV-{random.randint(1000,9999)} ({new_name})"
        mac_fake = f"{random.randint(10,99)}:{random.randint(10,99)}:7D:DA:71:{random.randint(10,99)}"
        st.session_state.devices[generated_id] = {"status": "Disconnected", "power": "OFF", "mac": mac_fake, "type": new_type}
        st.session_state.logs.append(f"📥 New Target Registered: {generated_id} mapped to [{mac_fake}].")
        st.rerun()

# =========================================================================
# 🖥️ CENTRAL MATRIX CONTROL PIPELINE
# =========================================================================
if st.session_state.global_power == "OFF":
    st.error("🚨 CRITICAL WARNING: Global Radio Transmitter Module is powered down. Flip switch on sidebar to re-engage antenna array.")
else:
    st.markdown("### 📱 Active Wireless Interface Directory")
    
    # Iterate dynamically across active registered endpoints
    for name, metadata in list(st.session_state.devices.items()):
        # Draw structural interface card layout using columns
        c_info, c_status, c_power, c_actions = st.columns([3, 2, 2, 3])
        
        with c_info:
            st.markdown(f"📡 **{name}**")
            st.caption(f"MAC Address: `{metadata['mac']}` | Class Profile: *{metadata['type']}*")
            
        with c_status:
            if metadata["status"] == "Connected":
                st.markdown("🟢 **CONNECTED**")
            else:
                st.markdown("⚪ *Idle / Disconnected*")
                
        with c_power:
            if metadata["power"] == "ON":
                st.markdown('<span class="badge-on">POWER: ON</span>', unsafe_allow_html=True)
            else:
                st.markdown('<span class="badge-off">POWER: OFF</span>', unsafe_allow_html=True)
                
        with c_actions:
            # Action Execution Matrix
            col_act1, col_act2 = st.columns(2)
            
            with col_act1:
                if metadata["status"] == "Connected":
                    if st.button("🔌 Disconnect", key=f"disc_{name}"):
                        st.session_state.devices[name]["status"] = "Disconnected"
                        st.session_state.logs.append(f"✂️ Disconnected device connection link cleanly: {name}.")
                        st.rerun()
                else:
                    if st.button("🔗 Connect Link", key=f"conn_{name}"):
                        # FORCE POWER ACTION GATEWAY
                        if metadata["power"] == "OFF":
                            st.session_state.logs.append(f"⚠️ TARGET BLOCKED: {name} power radio is OFF. Initializing forced override stream...")
                            # Overriding power target variables dynamically
                            st.session_state.devices[name]["power"] = "ON"
                            st.session_state.logs.append(f"⚡ FORCE OVERRIDE INITIATED: Turning target radio hardware ON for {name}.")
                        
                        st.session_state.devices[name]["status"] = "Connected"
                        st.session_state.logs.append(f"✅ Secure network channel established with {name}.")
                        st.rerun()
                        
            with col_act2:
                if metadata["power"] == "ON":
                    if st.button("🛑 Kill Power", key=f"pwr_off_{name}"):
                        st.session_state.devices[name]["power"] = "OFF"
                        st.session_state.devices[name]["status"] = "Disconnected"
                        st.session_state.logs.append(f"🔻 Turned radio hardware off for: {name}.")
                        st.rerun()
                else:
                    if st.button("⚡ Force On", key=f"pwr_on_{name}"):
                        st.session_state.devices[name]["power"] = "ON"
                        st.session_state.logs.append(f"🔺 Forced radio hardware module on for: {name}.")
                        st.rerun()
        st.markdown('<hr style="margin: 8px 0; border-color: #1e293b;" />', unsafe_allow_html=True)

# =========================================================================
# 📟 LIVE TELEMETRY TERMINAL OUTPUT LOGS
# =========================================================================
st.markdown("### 📟 Live Hardware Telemetry Log Stream")
log_content = "<br>".join([f"&gt; {log}" for log in reversed(st.session_state.logs)])
st.markdown(f'<div class="terminal-box">{log_content}</div>', unsafe_allow_html=True)

# =========================================================================
# 📜 BRAND DESIGNATION FOOTER (STRONG WHITE)
# =========================================================================
st.markdown(
    """
    <div class="strong-white-footer">
        © 2026 GLOBALINTERNET.PY | Global Software Architectures & Technology Innovation.
    </div>
    """,
    unsafe_allow_html=True
)
