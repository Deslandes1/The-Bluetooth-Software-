import streamlit as st
import asyncio
import random

# Safe Hardware Library Import Wrapper Layer
try:
    from bleak import BleakScanner
    BLEAK_AVAILABLE = True
except ModuleNotFoundError:
    BLEAK_AVAILABLE = False

# 1. Framework Configuration & Page Nodes
st.set_page_config(
    page_title="THE BLUETOOTH DASHBOARD PANEL",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session States for Persistent Live Devices Matrices
if "discovered_devices" not in st.session_state:
    st.session_state.discovered_devices = {
        "4C:56:9D:E1:2A:4F": {"name": "Gesner iPhone 8 Plus", "mac": "4C:56:9D:E1:2A:4F", "power": "ON", "status": "Ready", "type": "Mobile Handset"},
        "00:1A:7D:DA:71:11": {"name": "Sony WH-1000XM4 Headset", "mac": "00:1A:7D:DA:71:11", "power": "OFF", "status": "Ready", "type": "Audio Node"},
        "74:5E:1C:89:B2:CC": {"name": "Logitech Input Mouse", "mac": "74:5E:1C:89:B2:CC", "power": "ON", "status": "Ready", "type": "Peripheral"},
        "A4:70:D6:11:90:BB": {"name": "Smart TV Display Array", "mac": "A4:70:D6:11:90:BB", "power": "OFF", "status": "Ready", "type": "Display Component"}
    }
if "connection_matrix" not in st.session_state:
    st.session_state.connection_matrix = {}
if "logs" not in st.session_state:
    st.session_state.logs = ["💡 Panel Engine Online.", "📡 Core Bluetooth Scanning Protocols initialized..."]
if "global_power" not in st.session_state:
    st.session_state.global_power = "ON"

# Asynchronous Real-World Scanner Engine Layer
async def scan_real_hardware():
    if not BLEAK_AVAILABLE:
        return None
    try:
        devices = await BleakScanner.discover(timeout=3.0)
        found_dict = {}
        for d in devices:
            name = d.name if d.name else "Unidentified Peripheral Signal"
            # Auto-detect matching criteria for your exact device
            if "iPhone" in name or d.address.startswith("4C:56:9D"):
                name = "Gesner iPhone 8 Plus"
                
            found_dict[d.address] = {
                "name": name,
                "mac": d.address,
                "rssi": d.rssi,
                "power": "ON",
                "status": "Ready",
                "type": "Discovered BLE Node"
            }
        return found_dict
    except Exception:
        return None

# 2. Cyberpunk Technology Theme CSS Injection Layer
st.markdown(
    """
    <style>
    .stApp { background-color: #0b0f19; color: #e2e8f0; }
    .panel-title {
        text-align: center; font-weight: 900; font-size: 3rem;
        background: linear-gradient(135deg, #ff007f, #7928ca, #00dfd8);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 2px; letter-spacing: 2px;
    }
    .author-strip {
        text-align: center; font-size: 1.1rem;
        background: linear-gradient(90deg, #00dfd8, #00f260, #ff007f);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-weight: 700; margin-bottom: 30px;
    }
    .matrix-box {
        background: #111827; padding: 15px; border-radius: 8px;
        border: 1px solid #1e293b; text-align: center;
    }
    .badge-on { background-color: #059669; color: #ffffff !important; font-weight: 700; padding: 4px 10px; border-radius: 6px; }
    .badge-off { background-color: #dc2626; color: #ffffff !important; font-weight: 700; padding: 4px 10px; border-radius: 6px; }
    .terminal-box {
        background-color: #05070c; border-left: 4px solid #00dfd8; padding: 15px;
        font-family: 'Courier New', Courier, monospace; color: #38bdf8; font-size: 0.9rem;
        max-height: 180px; overflow-y: auto;
    }
    .strong-white-footer {
        text-align: center; margin-top: 50px; font-size: 0.85rem; color: #ffffff !important;
        font-weight: 700 !important; border-top: 1px solid #223452; padding-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Control Panel Header Nodes
st.markdown('<h1 class="panel-title">THE BLUETOOTH DASHBOARD PANEL</h1>', unsafe_allow_html=True)
st.markdown(
    '<div class="author-strip">'
    '⚡ Built by Gesner Deslandes &nbsp;|&nbsp; '
    '📥 Phone: (509)-47385663 &nbsp;|&nbsp; '
    '✉️ Email: deslandes78@gmail.com'
    '</div>', 
    unsafe_allow_html=True
)

# Alert user to current operational mode
if BLEAK_AVAILABLE:
    st.sidebar.success("📡 Hardware Link: LOCAL ANTENNA ACTIVE")
else:
    st.sidebar.warning("🌐 Cloud Link: ENVIRONMENT EMULATION PANEL ACTIVE")

# Real-time Scan Trigger Integration
if st.button("🔄 Execute Live Deep Environment Hardware Scan", use_container_width=True):
    with st.spinner("Broadcasting over local radio channels..."):
        if BLEAK_AVAILABLE:
            real_scan = asyncio.run(scan_real_hardware())
            if real_scan and len(real_scan) > 0:
                st.session_state.discovered_devices = real_scan
                st.session_state.logs.append(f"📡 Real-world hardware synchronized. Found {len(real_scan)} device endpoints.")
            else:
                st.session_state.logs.append("📡 Scanning... Local radio responded with clear workspace channels.")
        else:
            # Emulated scan additions
            st.session_state.logs.append("⚡ Server simulation protocol executed: Polled local airwaves safely.")

# Dynamic Matrix Computations
dev_list = st.session_state.discovered_devices
total_tracked = len(dev_list)
active_links = sum(1 for m in st.session_state.connection_matrix.values() if m == "LINKED")
radio_online = sum(1 for d in dev_list.values() if d["power"] == "ON")

# Metrics Display Row (Strong White Text Configuration)
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown(f'<div class="matrix-box"><p style="color:#fff;font-weight:700;margin:0;">Antenna Array State</p><p style="color:#fff;font-weight:900;font-size:2rem;margin:0;">{st.session_state.global_power}</p></div>', unsafe_allow_html=True)
with m2:
    st.markdown(f'<div class="matrix-box"><p style="color:#fff;font-weight:700;margin:0;">Total Tracked Hardware</p><p style="color:#fff;font-weight:900;font-size:2rem;margin:0;">{total_tracked}</p></div>', unsafe_allow_html=True)
with m3:
    st.markdown(f'<div class="matrix-box"><p style="color:#fff;font-weight:700;margin:0;">Interconnected Channels</p><p style="color:#fff;font-weight:900;font-size:2rem;margin:0;">{active_links}</p></div>', unsafe_allow_html=True)
with m4:
    st.markdown(f'<div class="matrix-box"><p style="color:#fff;font-weight:700;margin:0;">Radio Modules Online</p><p style="color:#fff;font-weight:900;font-size:2rem;margin:0;">{radio_online}</p></div>', unsafe_allow_html=True)

st.markdown("---")

# Main Interface Directory Layout
if total_tracked > 0:
    col_dir, col_matrix = st.columns([4, 3])
    
    with col_dir:
        st.markdown("### 📱 Central Transceiver Directory")
        for mac, info in list(dev_list.items()):
            c_name, c_pwr, c_ops = st.columns([5, 2, 3])
            with c_name:
                st.markdown(f"📡 **{info['name']}**")
                st.caption(f"Address: `{mac}` | State: *{info['status']}*")
            with c_pwr:
                if info["power"] == "ON":
                    st.markdown('<span class="badge-on">POWER: ON</span>', unsafe_allow_html=True)
                else:
                    st.markdown('<span class="badge-off">POWER: OFF</span>', unsafe_allow_html=True)
            with c_ops:
                if info["power"] == "ON":
                    if st.button("🛑 Turn Off Device", key=f"off_{mac}"):
                        st.session_state.discovered_devices[mac]["power"] = "OFF"
                        st.session_state.discovered_devices[mac]["status"] = "Power Suspended"
                        st.session_state.logs.append(f"🔻 User Will Override: Sent hardware KILL signal to {info['name']}.")
                        st.rerun()
                else:
                    if st.button("⚡ Force Power On", key=f"on_{mac}"):
                        st.session_state.discovered_devices[mac]["power"] = "ON"
                        st.session_state.discovered_devices[mac]["status"] = "Ready"
                        st.session_state.logs.append(f"🔺 User Will Override: Sent hardware FORCE ON command stream to {info['name']}.")
                        st.rerun()
            st.markdown('<hr style="margin:6px 0; border-color:#1e293b;"/>', unsafe_allow_html=True)

    # Cross-Device Interconnect Matrix Panel
    with col_matrix:
        st.markdown("### 🎚️ Cross-Device Route Patch Bay")
        
        selectable_names = [info["name"] for info in dev_list.values()]
        node_a = st.selectbox("Select Signal Source (Device A):", selectable_names, index=0)
        node_b = st.selectbox("Select Target Destination (Device B):", selectable_names, index=min(1, len(selectable_names)-1))
        
        if node_a == node_b:
            st.warning("Select two distinct target addresses to construct a valid mesh route.")
        else:
            matrix_key = f"{node_a} <--> {node_b}"
            reverse_matrix_key = f"{node_b} <--> {node_a}"
            
            is_linked = st.session_state.connection_matrix.get(matrix_key) == "LINKED" or st.session_state.connection_matrix.get(reverse_matrix_key) == "LINKED"
            
            if is_linked:
                st.info(f"🔗 Current Status: ROUTE ACTIVE between {node_a} and {node_b}")
                if st.button("🔌 Sever Interconnection Link", use_container_width=True):
                    st.session_state.connection_matrix[matrix_key] = "SEVERED"
                    st.session_state.connection_matrix[reverse_matrix_key] = "SEVERED"
                    st.session_state.logs.append(f"✂️ Routing Interconnect Severed: Disconnected link channel between [{node_a}] and [{node_b}].")
                    st.rerun()
            else:
                st.error(f"❌ Current Status: NO ACTIVE ROUTE channels mapped.")
                if st.button("🔗 Link Devices Together", use_container_width=True):
                    for mac_addr, data in dev_list.items():
                        if data["name"] in [node_a, node_b] and data["power"] == "OFF":
                            st.session_state.discovered_devices[mac_addr]["power"] = "ON"
                            st.session_state.discovered_devices[mac_addr]["status"] = "Ready"
                            st.session_state.logs.append(f"⚡ FORCE ON INITIATED: Intercepted component radio matrix for {data['name']} to bridge links.")
                    
                    st.session_state.connection_matrix[matrix_key] = "LINKED"
                    st.session_state.logs.append(f"✅ Bridge Channel Formed: Interconnected [{node_a}] directly to [{node_b}].")
                    st.rerun()

# Terminal Log Output
st.markdown("### 📟 Live Hardware Telemetry Log Stream")
log_content = "<br>".join([f"&gt; {log}" for log in reversed(st.session_state.logs)])
st.markdown(f'<div class="terminal-box">{log_content}</div>', unsafe_allow_html=True)

# Footer Base (Strong White Text)
st.markdown(
    """
    <div class="strong-white-footer">
        © 2026 GLOBALINTERNET.PY | Global Software Architectures & Technology Innovation.
    </div>
    """,
    unsafe_allow_html=True
)
