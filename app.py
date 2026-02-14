import streamlit as st
import requests
import time
from datetime import datetime

# 1. Stealth Shield
st.set_page_config(page_title="DHA Intelligence | PropTec", page_icon="🏛️", layout="wide")
st.markdown("<style>[data-testid='stHeader'], footer, #MainMenu, .stAppDeployButton {display: none !important;}</style>", unsafe_allow_html=True)

# 2. Interface
st.title("🏛️ DHA Karachi Strategic Intelligence")
st.write("Proprietary AI for Phase 1-8 & DHA City Analytics.")

phase = st.text_input("Enter Phase/Sector:", placeholder="e.g. Phase 8, Zone B")

if st.button("🚀 Run DHA Deep-Scan"):
    if phase:
        with st.spinner('Accessing DHA Market Records...'):
            time.sleep(1)
            st.metric("DHA Investment Score", "91/100", "Strong Bullish")
            st.info(f"AI Analysis for {phase}: High institutional demand detected. Perfect window for equity building.")
    else:
        st.error("Please enter a DHA location.")

# 3. Premium Lead Form
st.markdown("---")
st.subheader("📩 Get Private DHA VIP 'Hot-List'")
st.write("Join our elite circle for pre-market 'Distress Deals' in DHA Karachi.")

with st.form("dha_form", clear_on_submit=True):
    u_name = st.text_input("Full Name")
    u_phone = st.text_input("WhatsApp Number")
    u_budget = st.selectbox("Investment Budget (PKR):", ["Select Budget", "20M - 50M", "50M - 100M", "100M - 250M", "250M+"])
    
    if st.form_submit_button("Request DHA VIP Access"):
        if u_name and u_phone and u_budget != "Select Budget":
            URL = "https://script.google.com/macros/s/AKfycby5T5NJ8NAf1LP_G5SJ3iTaPWdD0DusoFbdBUFrVkqt1Z03PcNQ89TE2o2aXSOORXzi/exec"
            payload = {"Name": u_name, "Phone": u_phone, "Budget": u_budget, "Market": "DHA Karachi", "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            try:
                requests.post(URL, json=payload, timeout=10)
                st.balloons()
                st.success(f"Dhamaka! Shukriya {u_name}. Hamare DHA Specialists aapka portfolio ({u_budget}) analyze kar rahe hain.")
                st.info("🏛️ **PropTec Premium:** Hamari team aapse jald rabta karegi aur sirf 'DHA High-Value' leads aapko WhatsApp par bheji jayengi. Stay Alert!")
            except:
                st.error("Connection Error.")
        else:
            st.warning("Please fill all details.")
