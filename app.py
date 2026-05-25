import streamlit as st
import asyncio
from bleak import BleakScanner

# 1. Page Configuration Architecture
st.set_page_config(
    page_title="REAL-TIME BLUETOOTH NODE MONITOR",
    page_icon="📡",
    layout="wide"
)

# Core styling injection for dark modern tracking interface
st.markdown(
    """
    <style>
    .stApp { background-color: #0b0f19; color: #e2e8f0; }
    .panel-title {
        text-align: center; font-weight: 900; font-size: 2.5rem;
        background: linear-gradient(135deg, #00dfd8, #7928ca, #ff007f);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .meta-strip {
        text-align: center; font-family: monospace; color: #00dfd8; font-weight: bold; margin-bottom: 25px;
    }
    .device-card {
        background-color: #111827; border: 1px solid #1e293b; padding: 15px; border-radius: 8px; margin-bottom: 10px;
    }
    .signal-badge {
        background-color: #1e293b; color: #38bdf8; padding: 4px 8px; border-radius: 4px; font-family: monospace; font-size: 0.85rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="panel-title">REAL-TIME BLUETOOTH METADATA MATRIX</h1>', unsafe_allow_html=True)
st.markdown('<div class="meta-strip">ENGINEER IN CHIEF: GESNER DESLANDES | GLOBALINTERNET.PY</div>', unsafe_allow_html=True)

# 2. Hardwired Scanning Coroutine
async def scan_live_airwaves():
    """Queries the physical Bluetooth host controller for current radio targets."""
    try:
        # Request a quick, responsive 2.5-second live window capture
        devices = await BleakScanner.discover(timeout=2.5)
        return devices
    except Exception as e:
        st.error(f"⚠️ Physical Hardware Interface Exception: {e}")
        st.info("💡 Note: Cloud servers do not have built-in antennas to see your room. For real hardware scanning, run this script locally using your computer's Bluetooth adapter.")
        return []

# 3. Main Interface Logic
st.markdown("### 🖥️ Live Airwave Monitor")
st.write("The engine uses asynchronous routines to parse raw BLE hardware advertisements directly from your local antenna array.")

auto_loop = st.checkbox("🔄 Enable Live Continuous Streaming Loop", value=True)

# Execute the asynchronous hardware capture loop
with st.spinner("Polling local physical adapter for radio waves..."):
    current_devices = asyncio.run(scan_live_airwaves())

# Parse results 
named_devices = [d for d in current_devices if d.name and d.name.strip() != ""]
unnamed_devices = [d for d in current_devices if not d.name or d.name.strip() == ""]

# UI Displays
st.markdown(f"#### 📱 Tracked Active Nodes ({len(current_devices)} total found)")

if not current_devices:
    st.info("No active Bluetooth devices captured in this cycle. Put your speaker into discovery/pairing mode so it shouts its name out loud.")
else:
    if named_devices:
        st.markdown("##### 🔊 Identified Devices")
        for dev in named_devices:
            name_lower = dev.name.lower()
            if "iphone" in name_lower or dev.address.startswith("4C:56:9D"):
                dev_class = "📱 Mobile Phone Asset"
            elif any(k in name_lower for k in ["speaker", "jbl", "bose", "sound", "audio", "sony", "wh-"]):
                dev_class = "🔊 Audio Output Node"
            else:
                dev_class = "📡 BLE Hardware Peripheral"

            st.markdown(
                f"""
                <div class="device-card">
                    <span class="signal-badge" style="float: right;">📶 {dev.rssi} dBm</span>
                    <strong style="color: #ffffff; font-size: 1.1rem;">📟 {dev.name}</strong><br>
                    <code style="color: #94a3b8; font-size: 0.85rem;">Hardware MAC Address: {dev.address}</code> | 
                    <span style="color: #00dfd8; font-size: 0.85rem; font-weight: bold;">{dev_class}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

    if unnamed_devices:
        with st.expander(f"🔍 Show Background Unnamed Hardware Signatures ({len(unnamed_devices)})"):
            for dev in unnamed_devices:
                st.markdown(f"📡 **MAC ID:** `{dev.address}` | **Signal Strength:** `{dev.rssi} dBm`")

# 4. Streamlit Direct Pipeline Loop Controller
if auto_loop:
    asyncio.run(asyncio.sleep(0.5))
    st.rerun()
