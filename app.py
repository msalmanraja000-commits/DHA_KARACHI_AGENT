import streamlit as st
from groq import Groq
from tavily import TavilyClient

# 1. Professional Page Setup
st.set_page_config(page_title="DHA Karachi Advisor", page_icon="🏢", layout="wide")

# Custom CSS for Corporate Look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { background-color: #002b5b; color: white; border-radius: 5px; }
    .stChatMessage { border-radius: 15px; border: 1px solid #ddd; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Keys from Secrets
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]
    client = Groq(api_key=GROQ_API_KEY)
    tavily = TavilyClient(api_key=TAVILY_API_KEY)
except Exception as e:
    st.error("Secrets setup missing! Please check Streamlit dashboard.")
    st.stop()

# 3. Sidebar - Corporate Info
with st.sidebar:
    st.image("https://img.icons8.com/color/96/real-estate.png")
    st.title("DHA Elite Advisor")
    st.info("Directly connected to Live Karachi Property Markets.")
    st.markdown("---")
    st.write("📌 **Focus Areas:**\n- DHA Phase 1-8\n- DHA City Karachi\n- Current Market Tax Rates")

# 4. Search Function (The Superpower)
def get_live_market_data(query):
    search_query = f"DHA Karachi property rates news {query} February 2026"
    results = tavily.search(query=search_query, search_depth="advanced")
    context = ""
    for res in results['results']:
        context += f"\nSource: {res['url']}\nContent: {res['content']}\n"
    return context

# 5. Main Chat UI
st.title("🏢 DHA Karachi Real Estate Intelligence")
st.caption("Powered by PropTecSolutions")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your query (e.g., Phase 8 rates or Tax info)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.status("Searching live market data...", expanded=True):
            live_data = get_live_market_data(prompt)
            st.write("Analyzing latest trends...")
            
        # Corporate System Prompt
        system_msg = f"""
        You are a Senior Investment Consultant at DHA Karachi. 
        Your tone: Professional, formal, and data-driven.
        Use this LIVE DATA to answer: {live_data}
        If asked about prices, provide the most recent estimates from the search results.
        Always end with: 'Let me know if you need a detailed ROI analysis.'
        """
        
        response_container = st.empty()
        full_response = ""
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": system_msg}] + st.session_state.messages
        )
        
        full_response = completion.choices[0].message.content
        st.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
