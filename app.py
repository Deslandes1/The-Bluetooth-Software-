# =========================================================================
# 📊 TOP GLOBAL MATRIX READOUT NODES (STRONG WHITE TEXT)
# =========================================================================
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(
        """
        <div style="background: #111827; padding: 15px; border-radius: 8px; border: 1px solid #1e293b; text-align: center;">
            <p style="color: #ffffff !important; font-weight: 700; font-size: 1.1rem; margin: 0; padding-bottom: 5px;">Global Antenna State</p>
            <p style="color: #ffffff !important; font-weight: 900; font-size: 2.2rem; margin: 0; text-shadow: 0 0 10px rgba(255,255,255,0.2);">ON</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

with m2:
    st.markdown(
        """
        <div style="background: #111827; padding: 15px; border-radius: 8px; border: 1px solid #1e293b; text-align: center;">
            <p style="color: #ffffff !important; font-weight: 700; font-size: 1.1rem; margin: 0; padding-bottom: 5px;">Total Tracked Hardware</p>
            <p style="color: #ffffff !important; font-weight: 900; font-size: 2.2rem; margin: 0; text-shadow: 0 0 10px rgba(255,255,255,0.2);">5</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

with m3:
    st.markdown(
        """
        <div style="background: #111827; padding: 15px; border-radius: 8px; border: 1px solid #1e293b; text-align: center;">
            <p style="color: #ffffff !important; font-weight: 700; font-size: 1.1rem; margin: 0; padding-bottom: 5px;">Active Linked Channels</p>
            <p style="color: #ffffff !important; font-weight: 900; font-size: 2.2rem; margin: 0; text-shadow: 0 0 10px rgba(255,255,255,0.2);">2</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

with m4:
    st.markdown(
        """
        <div style="background: #111827; padding: 15px; border-radius: 8px; border: 1px solid #1e293b; text-align: center;">
            <p style="color: #ffffff !important; font-weight: 700; font-size: 1.1rem; margin: 0; padding-bottom: 5px;">Radio Modules Online</p>
            <p style="color: #ffffff !important; font-weight: 900; font-size: 2.2rem; margin: 0; text-shadow: 0 0 10px rgba(255,255,255,0.2);">4</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

st.markdown("---")
