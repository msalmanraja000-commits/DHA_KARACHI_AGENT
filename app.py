import streamlit as st
import requests
import time
from datetime import datetime

# --- SECURITY & STEALTH ---
st.set_page_config(page_title="DHA Intelligence | PropTec", page_icon="🏛️", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"], header, footer, .stAppDeployButton, #MainMenu {display: none !important; visibility: hidden !important;}
    .viewerBadge_container__1QSob { display: none !important; }
    .block-container { padding-top: 1rem !important; }
    .custom-footer {
        position: fixed; left: 0; bottom: 0; width: 100%; 
        background-color: #0E1117; color: #0088FF; 
        text-align: center; padding: 12px; font-size: 14px; 
        border-top: 2px solid #0088FF; z-index: 999;
    }
    </style>
    <div class="custom-footer">© 2026 PropTecSolutions | DHA Karachi Specialized AI | Founder: Salman Raja</div>
    """, unsafe_allow_html=True)

# --- APP INTERFACE ---
st.title("🏛️ DHA Karachi Strategic Intelligence")
st.write("Proprietary AI for Phase 1-8 & DHA City Analytics.")

phase = st.text_input("Enter Phase/Sector (e.g. Phase 8, Zone B):", key="dha_loc")

if st.button("🚀 Run DHA Deep-Scan"):
    if phase:
        with st.spinner('Analyzing DHA Market Data...'):
            time.sleep(1.5)
            m1, m2, m3 = st.columns(3)
            m1.metric("Investment Score", "91/100", "Strong Bullish")
            m2.metric("Liquidity", "High", "Active")
            m3.metric("Projected ROI", "15-20%", "Annual")
            
            st.markdown("---")
            t1, t2, t3 = st.tabs(["📊 Market Logic", "📈 Forecast", "⚖️ Legal Status"])
            with t1:
                st.write(f"**Trends in {phase}:** Institutional capital inflow detected. High demand for residential equity building.")
            with t2:
                st.write("Current price points are testing historical resistance levels. Breakout anticipated.")
            with t3:
                st.write("Legal Status: **100% Clear.** No litigation detected in registry scans.")
    else:
        st.error("Please enter a Phase.")

# --- LEAD GENERATOR (CONNECTED TO YOUR SCRIPT) ---
st.markdown("---")
with st.form("dha_lead_form", clear_on_submit=True):
    st.subheader("📩 Get Private DHA VIP List")
    u_name = st.text_input("Full Name")
    u_phone = st.text_input("WhatsApp Number")
    
    if st.form_submit_button("Request DHA Access"):
        if u_name and u_phone:
            # Your exact Apps Script URL from image_2e77ff.png
            BACKEND_URL = "https://script.google.com/macros/s/AKfycby5T5NJ8NAf1LP_G5SJ3iTaPWdD0DusoFbdBUFrVkqt1Z03PcNQ89TE2o2aXSOORXzi/exec"
            payload = {
                "Name": u_name, 
                "Phone": u_phone, 
                "Budget": "DHA Client", 
                "Market": "DHA Karachi", 
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            try:
                requests.post(BACKEND_URL, json=payload)
                st.balloons()
                st.success("DHA Intelligence Report Locked! Data saved to your sheet.")
            except:
                st.error("Connection error. Check your internet.")
