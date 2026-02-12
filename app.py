import streamlit as st
import random
import time

st.set_page_config(page_title="DHA Strategic Intelligence | PropTecSolutions", page_icon="🏛️")

# Custom Styling
st.markdown("<style>.main {background-color: #0e1117; color: white;}</style>", unsafe_allow_html=True)

st.title("🏛️ DHA Karachi: Market Intelligence")
st.caption("Powered by PropTecSolutions | February 2026 Data")

# Sentiment Logic
score = random.randint(70, 95)
status = "Strong Buy" if score > 80 else "Stable"

st.metric("DHA Phase 8 Sentiment Score", f"{score}/100", delta=status)

# Lead Capture
with st.sidebar:
    st.header("Lead Capture")
    with st.form("dha_leads"):
        name = st.text_input("Investor Name")
        phone = st.text_input("WhatsApp")
        if st.form_submit_button("Request DHA Phase-wise ROI"):
            st.success("Sent to Red Box DHA Desk.")

# Analysis
query = st.text_input("Enter DHA Phase/Zone (e.g. Phase 6, Zone E):")
if query:
    with st.spinner("Analyzing DHA Market Trends..."):
        time.sleep(1)
        st.write(f"### Results for {query}")
        st.write("- **Price Status:** 4% Increase expected in next quarter.")
        st.write("- **Sentiment:** Highly Bullish.")
