import streamlit as st
from groq import Groq
from tavily import TavilyClient
import pandas as pd
import plotly.express as px

# 1. Ultra-Premium Page Config
st.set_page_config(page_title="DHA Karachi Pro-Intelligence", page_icon="⚖️", layout="wide")

# Custom CSS for Full Maxout White Font & Professional Look
st.markdown("""
    <style>
    /* Main Background and Global Font Color */
    .stApp { 
        background-color: #0e1117; 
        color: #ffffff !important; 
    }
    
    /* Ensuring all text, labels, and subheaders are White */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #ffffff !important;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    [data-testid="stSidebar"] .css-17l2qt2 { 
        color: #ffffff !important; 
    }

    /* Chat Message Bubbles */
    .stChatMessage {
        background-color: #1e2129;
        border: 1px solid #3d4450;
        border-radius: 10px;
        color: #ffffff !important;
    }

    /* Input Box Styling */
    .stChatInputContainer {
        background-color: #161b22 !important;
    }
    
    /* Metrics Box */
    [data-testid="stMetricValue"] {
        color: #00ffcc !important; /* Professional Teal color for numbers */
    }
    </style>
    """, unsafe_allow_html=True)
# 2. Secure API Initialization
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    tavily = TavilyClient(api_key=st.secrets["TAVILY_API_KEY"])
except:
    st.error("API Keys missing in Streamlit Secrets!")
    st.stop()

# 3. Sidebar: Market Dashboard
with st.sidebar:
    st.header("📈 Market Pulse")
    st.metric(label="DHA Index Status", value="Bullish", delta="+2.4%")
    
    # Mock Data for Graph (Professional Touch)
    df = pd.DataFrame({
        'Phase': ['Ph 5', 'Ph 6', 'Ph 8', 'DHA City'],
        'Demand': [85, 92, 98, 70]
    })
    fig = px.bar(df, x='Phase', y='Demand', title="Investor Interest Index", color='Demand', color_continuous_scale='Bluered_r')
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    st.write("📞 **Priority Support:**\nLevel 3 Enterprise Access")

# 4. Search Logic
def get_enterprise_data(query):
    search_query = f"DHA Karachi latest price analysis {query} February 2026 commercial residential"
    results = tavily.search(query=search_query, search_depth="advanced")
    return "\n".join([f"Source: {res['url']}\nData: {res['content']}" for res in results['results']])

# 5. Main UI
st.title("⚖️ DHA Karachi Enterprise Intelligence")
st.subheader("Advanced Real Estate Advisory System")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask for market analysis, tax implications, or plot valuations..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("Fetching Live Market Intelligence...", expanded=False):
            market_data = get_enterprise_data(prompt)
        
        # Expert Prompting
        system_prompt = f"""
        You are the 'DHA Karachi Strategic Advisor'. 
        Tone: Highly sophisticated, objective, and analytical.
        Data Source: {market_data}
        Task: Provide a deep-dive analysis. Use bullet points for clarity. 
        Include a 'Risk vs Reward' section for every property query.
        """
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": system_prompt}] + st.session_state.messages
        )
        
        response = completion.choices[0].message.content
        st.markdown(response)
        
        # Maxout: Add Action Buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Generate Investment Report"):
                st.toast("Generating PDF Report... Done!")
        with col2:
            if st.button("Compare with DHA City"):
                st.info("Directing to Comparative Analytics module...")

    st.session_state.messages.append({"role": "assistant", "content": response})
  
     
