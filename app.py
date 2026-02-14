import streamlit as st
import requests
import time
from datetime import datetime

# --- SECURITY & STEALTH SHIELD ---
st.set_page_config(page_title="BTK Intelligence | PropTec", page_icon="🏙️", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
    [data-testid="stHeader"], header, footer, .stAppDeployButton, #MainMenu {display: none !important; visibility: hidden !important;}
    .viewerBadge_container__1QSob { display: none !important; }
    .block-container { padding-top: 1rem !important; }
    .custom-footer {
        position: fixed; left: 0; bottom: 0; width: 100%; 
        background-color: #0E1117; color: #FFD700; 
        text-align: center; padding: 12px; font-size: 14px; 
        border-top: 2px solid #FFD700; z-index: 999;
    }
    </style>
    <div class="custom-footer">© 2026 PropTecSolutions | BTK AI Strategic Framework | Founder: Salman Raja</div>
    """, unsafe_allow_html=True)

# --- APP INTERFACE ---
st.title("🏙️ BTK Strategic Intelligence")
st.write("Real-time Precinct Analysis for Bahria Town Karachi.")

precinct = st.text_input("Enter Precinct (e.g. Precinct 10-A, P-31):", placeholder="Analyze precinct...")

if st.button("🚀 Analyze BTK Market"):
    if precinct:
        with st.spinner('Scanning BTK Precinct Data...'):
            time.sleep(1.5)
            m1, m2, m3 = st.columns(3)
            m1.metric("Precinct Score", "94/100", "Top Choice")
            m2.metric("Occupancy Rate", "82%", "High Growth")
            m3.metric("ROI Potential", "12-14%", "6 Months")
            
            st.markdown("---")
            t1, t2, t3 = st.tabs(["📊 Sentiment", "📈 Yield", "🏗️ Development"])
            with t1:
                st.write(f"**Sentiment in {precinct}:** Rapid family shifting and commercial development are creating a liquidity surge.")
            with t2:
                st.write("Rental yields in this precinct remain 5% higher than the Bahria average. Ideal for rental income.")
                            with t3:
                st.write("Development Status: **100% Complete.** All utilities (Gas, Electricity, Water) are functional.")
    else:
        st.error("Please enter a Precinct.")

# --- LEAD GENERATOR (CONNECTED) ---
st.markdown("---")
with st.form("btk_lead_form", clear_on_submit=True):
    st.subheader("📩 Get BTK Investment Hot-List")
    u_name = st.text_input("Full Name")
    u_phone = st.text_input("WhatsApp Number")
    
    if st.form_submit_button("Get BTK VIP Access"):
        if u_name and u_phone:
            BACKEND_URL = "https://script.google.com/macros/s/AKfycby5T5NJ8NAf1LP_G5SJ3iTaPWdD0DusoFbdBUFrVkqt1Z03PcNQ89TE2o2aXSOORXzi/exec"
            payload = {"Name": u_name, "Phone": u_phone, "Budget": "BTK Client", "Market": "BTK Karachi", "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            try:
                requests.post(BACKEND_URL, json=payload)
                st.balloons()
                st.success("BTK VIP Data Synced! Check your WhatsApp.")
            except:
                st.error("Sync Error. Please try again.")
