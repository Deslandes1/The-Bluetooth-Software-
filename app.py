import streamlit as st
import random

# 1. Framework Configuration & Page Nodes
st.set_page_config(
    page_title="THE BLUETOOTH DASHBOARD PANEL",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session States first to prevent calculation NameErrors
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
if "active_remote" not in st.session_state:
    st.session_state.active_remote = "DEV-4412 (Gesner iPhone 15 Pro)"

# Calculate live matrix states dynamically
total_devs = len(st.session_state.devices)
active_conn = sum(1 for d in st.session_state.devices.values() if d["status"] == "Connected")
power_on_count = sum(1 for d in st.session_state.devices.values() if d["power"] == "ON")
global_antenna = st.session_state.global_power

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
    
    /* Remote Interface Box Decoration */
    .remote-hull {
        background: radial-gradient(circle at top left, #1e1b4b, #0f172a);
        border: 2px solid #7928ca;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 0 20px rgba(121, 40, 202, 0.4);
        text-align: center;
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
        max-height: 200px;
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
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(
        f"""
        <div style="background: #111827; padding: 15px; border-radius: 8px; border: 1px solid #1e293b; text-align: center;">
            <p style="color: #ffffff !important; font-weight: 700; font-size: 1.1rem; margin: 0; padding-bottom: 5px;">Global Antenna State</p>
            <p style="color: #ffffff !important; font-weight: 900; font-size: 2.2rem; margin: 0; text-shadow: 0 0 10px rgba(255,255,255,0.2);">{global_antenna}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

with m2:
    st.markdown(
        f"""
        <div style="background: #111827; padding: 15px; border-radius: 8px; border: 1px solid #1e293b; text-align: center;">
            <p style="color: #ffffff !important; font-weight: 700; font-size: 1.1rem; margin: 0; padding-bottom: 5px;">Total Tracked Hardware</p>
            <p style="color: #ffffff !important; font-weight: 900; font-size: 2.2rem; margin: 0; text-shadow: 0 0 10px rgba(255,255,255,0.2);">{total_devs}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

with m3:
    st.markdown(
        f"""
        <div style="background: #111827; padding: 15px; border-radius: 8px; border: 1px solid #1e293b; text-align: center;">
            <p style="color: #ffffff !important; font-weight: 700; font-size: 1.1rem; margin: 0; padding-bottom: 5px;">Active Linked Channels</p>
            <p style="color: #ffffff !important; font-weight: 900; font-size: 2.2rem; margin: 0; text-shadow: 0 0 10px rgba(255,255,255,0.2);">{active_conn}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

with m4:
    st.markdown(
        f"""
        <div style="background: #111827; padding: 15px; border-radius: 8px; border: 1px solid #1e293b; text-align: center;">
            <p style="color: #ffffff !important; font-weight: 700; font-size: 1.1rem; margin: 0; padding-bottom: 5px;">Radio Modules Online</p>
            <p style="color: #ffffff !important; font-weight: 900; font-size: 2.2rem; margin: 0; text-shadow: 0 0 10px rgba(255,255,255,0.2);">{power_on_count}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

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
    # Splitting the app dashboard structure into Directory layout and Remote Emulation Panel layout
    directory_col, remote_col = st.columns([3, 2])
    
    with directory_col:
        st.markdown("### 📱 Active Wireless Interface Directory")
        
        # Iterate dynamically across active registered endpoints
        for name, metadata in list(st.session_state.devices.items()):
            c_info, c_status, c_power = st.columns([4, 3, 3])
            
            with c_info:
                st.markdown(f"📡 **{name}**")
                st.caption(f"`{metadata['mac']}` | *{metadata['type']}*")
                
            with c_status:
                if metadata["status"] == "Connected":
                    st.markdown("🟢 **CONNECTED**")
                else:
                    st.markdown("⚪ *Disconnected*")
                    
            with c_power:
                if metadata["power"] == "ON":
                    st.markdown('<span class="badge-on">POWER: ON</span>', unsafe_allow_html=True)
                else:
                    st.markdown('<span class="badge-off">POWER: OFF</span>', unsafe_allow_html=True)
            
            # Action Execution Matrix
            col_act1, col_act2, col_act3 = st.columns(3)
            with col_act1:
                if metadata["status"] == "Connected":
                    if st.button("🔌 Disconnect", key=f"disc_{name}"):
                        st.session_state.devices[name]["status"] = "Disconnected"
                        st.session_state.logs.append(f"✂️ Disconnected device connection link cleanly: {name}.")
                        st.rerun()
                else:
                    if st.button("🔗 Connect Link", key=f"conn_{name}"):
                        # FORCE POWER ON IF DISCONNECTED
                        if metadata["power"] == "OFF":
                            st.session_state.logs.append(f"⚠️ TARGET BLOCKED: {name} power radio is OFF. Initializing forced override stream...")
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
                        
            with col_act3:
                if st.button("🎮 Map Remote", key=f"rem_{name}"):
                    # FORCE MODE TACTICAL STEP
                    if st.session_state.devices[name]["power"] == "OFF" or st.session_state.devices[name]["status"] == "Disconnected":
                        st.session_state.logs.append(f"🚨 REMOTE INITIALIZATION FORCE: {name} is restricted. Forcing power ON & establishing connection stream...")
                        st.session_state.devices[name]["power"] = "ON"
                        st.session_state.devices[name]["status"] = "Connected"
                    
                    st.session_state.active_remote = name
                    st.session_state.logs.append(f"🎮 Target remote control active: {name}.")
                    st.rerun()
                    
            st.markdown('<hr style="margin: 8px 0; border-color: #1e293b;" />', unsafe_allow_html=True)

    # =========================================================================
    # 🎮 REMOTE CONTROL PANEL SURFACE
    # =========================================================================
    with remote_col:
        st.markdown("### 🕹️ Remote Emulation Deck")
        target_device = st.session_state.active_remote
        
        if target_device in st.session_state.devices:
            dev_data = st.session_state.devices[target_device]
            
            st.markdown(
                f"""
                <div class="remote-hull">
                    <h4 style="color: #00dfd8; margin: 0;">REMOTE CORE: ACTIVE</h4>
                    <p style="color: #ffffff; font-weight: 600; font-size: 1.1rem; margin-top: 5px; margin-bottom: 2px;">{target_device}</p>
                    <span class="badge-on" style="font-size: 0.75rem;">CHANNEL LINKED TO PORT 1</span>
                    <div style="margin-top: 20px; margin-bottom: 20px; border-top: 1px dashed #7928ca;"></div>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # Interactive Input Remote Pad Toggles
            pad_up, pad_down = st.columns(2)
            with pad_up:
                if st.button("🔼 Volume Up / Increase Frequency", use_container_width=True, key="r_vup"):
                    st.session_state.logs.append(f"🎮 [{target_device}] Remote Signal Sent: VOLUME_UP (+1)")
            with pad_down:
                if st.button("🔽 Volume Down / Decrease Frequency", use_container_width=True, key="r_vdown"):
                    st.session_state.logs.append(f"🎮 [{target_device}] Remote Signal Sent: VOLUME_DOWN (-1)")
            
            media_prev, media_play, media_next = st.columns(3)
            with media_prev:
                if st.button("⏮️ Prev Channel", use_container_width=True, key="r_prev"):
                    st.session_state.logs.append(f"🎮 [{target_device}] Remote Command Executed: PREV_TRACK")
            with media_play:
                if st.button("⏸️ Pause / Play", use_container_width=True, key="r_play"):
                    st.session_state.logs.append(f"🎮 [{target_device}] Remote Command Executed: TOGGLE_PLAYBACK")
            with media_next:
                if st.button("⏭️ Next Channel", use_container_width=True, key="r_next"):
                    st.session_state.logs.append(f"🎮 [{target_device}] Remote Command Executed: NEXT_TRACK")
                    
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🚨 Emergency Connection Kill", use_container_width=True, key="r_kill"):
                st.session_state.devices[target_device]["power"] = "OFF"
                st.session_state.devices[target_device]["status"] = "Disconnected"
                st.session_state.logs.append(f"💥 EMERGENCY SHUTDOWN SENT: Terminated radio power string for {target_device}.")
                st.rerun()
        else:
            st.info("Select a device in the interface directory and click 'Map Remote' to bind control vectors.")

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
