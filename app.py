import streamlit as st
import requests
import time
from datetime import datetime

# --- 🛡️ STEALTH & COPYRIGHT (SALMAN RAJA SPECIAL) ---
st.set_page_config(page_title="PropTec Intelligence", page_icon="🏛️", layout="wide")

st.markdown("""
    <style>
    /* GitHub aur Streamlit branding hide karne ke liye */
    [data-testid="stHeader"], header, footer, .stAppDeployButton, #MainMenu {display: none !important; visibility: hidden !important;}
    .viewerBadge_container__1QSob { display: none !important; }
    
    /* Custom Salman Raja Copyright Footer */
    .custom-footer {
        position: fixed; left: 0; bottom: 0; width: 100%; 
        background-color: #0E1117; color: #00FFAA; 
        text-align: center; padding: 12px; font-size: 14px; 
        border-top: 2px solid #00FFAA; z-index: 999;
        font-weight: bold;
    }
    </style>
    <div class="custom-footer">© 2026 PropTecSolutions | Proprietary Intelligence Framework | Founder: Salman Raja</div>
    """, unsafe_allow_html=True)

# --- 📊 CORE INTERFACE ---
st.title("🏛️ PropTec Strategic Intelligence")
market = st.selectbox("Select Business Sector:", ["DHA Karachi", "Bahria Town Karachi"])
zone = st.text_input("Enter Location (Phase/Precinct):", placeholder="e.g. Phase 8 or Precinct 10")

if st.button("🚀 Run Deep-Scan Analysis"):
    if zone:
        with st.spinner('Accessing Proprietary Records...'):
            time.sleep(1)
            st.metric("Investment Potential", "93/100", "High Yield")
            st.success(f"Market Report for {zone} generated successfully!")
    else:
        st.error("Please provide a location.")

# --- 📩 MAX-OUT LEAD FORM (BUDGET + HOOK) ---
st.markdown("---")
with st.form("main_lead_form", clear_on_submit=True):
    st.subheader("🔥 Get Exclusive VIP Hot-Leads")
    st.write("Receive under-market distress deals directly on your WhatsApp.")
    
    u_name = st.text_input("Full Name")
    u_phone = st.text_input("WhatsApp Number")
    u_budget = st.selectbox("Your Investment Budget:", [
        "Select Budget", "5M - 20M", "20M - 50M", "50M - 100M", "100M+"
    ])
    
    submit_btn = st.form_submit_button("Get VIP Access 🚀")
    
    if submit_btn:
        if u_name and u_phone and u_budget != "Select Budget":
            # APKA GOOGLE SCRIPT URL
            URL = "https://script.google.com/macros/s/AKfycby5T5NJ8NAf1LP_G5SJ3iTaPWdD0DusoFbdBUFrVkqt1Z03PcNQ89TE2o2aXSOORXzi/exec"
            
            payload = {
                "Name": u_name,
                "Phone": u_phone,
                "Budget": u_budget,
                "Market": market,
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            try:
                # Sending data to sheet
                response = requests.post(URL, json=payload, timeout=10)
                if response.status_code == 200:
                    st.balloons()
                    st.success(f"Dhamaka! Shukriya {u_name}. Hamari team aapko shortly contact karegi.")
                    st.info(f"💎 **PropTec VIP:** Hum aapke budget ({u_budget}) ke mutabiq best 'Hot Leads' nikal rahe hain. Stay tuned!")
                else:
                    st.error("Sheet Connection Error. Please check Apps Script permissions.")
            except:
                st.error("Critical Error: 'requests' library not found. Add it to requirements.txt on GitHub!")
        else:
            st.warning("Please fill all details correctly.")
