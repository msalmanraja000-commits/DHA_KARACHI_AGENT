import streamlit as st
import requests
import time
from datetime import datetime

# --- 🛡️ STEALTH & COPYRIGHT ---
st.set_page_config(page_title="DHA Intelligence | PropTec", page_icon="🏛️", layout="wide")
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display:none;}
    [data-testid="stHeader"] {display:none;}
    .viewerBadge_container__1QSob {display:none;}
    .stAppToolbar {display:none;}
    
    /* Mobile optimization */
    .block-container { padding-top: 0rem !important; }
    
    .custom-footer {
        position: fixed; left: 0; bottom: 0; width: 100%; 
        background-color: #0E1117; color: #00FFAA; 
        text-align: center; padding: 10px; font-size: 12px; 
        border-top: 1px solid #00FFAA; z-index: 999;
    }
    </style>
    <div class="custom-footer">© 2026 PropTecSolutions | Powered by Salman Raja AI</div>
    """, unsafe_allow_html=True)
# --- 📊 INTERFACE ---
st.title("🏛️ DHA Karachi Strategic Intelligence")
phase = st.text_input("Enter Phase/Sector:", placeholder="e.g. Phase 8, Zone B")

if st.button("🚀 Run DHA Deep-Scan"):
    if phase:
        with st.spinner('Analyzing DHA Market Data...'):
            time.sleep(1)
            st.metric("DHA Investment Score", "91/100", "Strong Bullish")
    else:
        st.error("Please enter a DHA location.")

# --- 📩 LEAD FORM (BUDGET + HOOK) ---
st.markdown("---")
with st.form("dha_lead_form", clear_on_submit=True):
    st.subheader("🔥 Get Private DHA VIP 'Hot-List'")
    u_name = st.text_input("Full Name")
    u_phone = st.text_input("WhatsApp Number")
    u_budget = st.selectbox("Investment Budget:", ["Select Budget", "20M - 50M", "50M - 100M", "100M - 250M", "250M+"])
    
    if st.form_submit_button("Request DHA VIP Access"):
        if u_name and u_phone and u_budget != "Select Budget":
            # Apka Web App URL
            URL = "https://script.google.com/macros/s/AKfycby1ZemyjAZGkOsJSQ0n_N5CzJ565xVzs_ze8xEgXIlu9yzhEGRb8seO8-HYjxeoZOCF/exec"
            payload = {"Name": u_name, "Phone": u_phone, "Budget": u_budget, "Market": "DHA Karachi", "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            try:
                # Sending data to sheet
                requests.post(URL, json=payload, timeout=10)
                st.balloons()
                st.success(f"Dhamaka! Shukriya {u_name}. Hamare experts aapka portfolio analyze kar rahe hain.")
                st.info("🏛️ **PropTec Premium:** Hamari team jald rabta karegi aur 'DHA High-Value' leads aapko WhatsApp par milengi.")
            except:
                st.error("Sheet Connection Error. Please check requirements.txt")
     
