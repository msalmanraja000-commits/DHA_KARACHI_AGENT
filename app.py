import streamlit as st
from groq import Groq

# 1. Page Config
st.set_page_config(page_title="DHA Karachi AI", page_icon="🏝️")

# 2. API Key from Streamlit Secrets
# Salman bhai, ensure "GROQ_API_KEY" is saved in Streamlit Settings!
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception as e:
    st.error("API Key nahi mili! Streamlit Settings -> Secrets check karein.")
    st.stop()

st.title("🏝️ DHA Karachi AI Advisor")

# 3. Chat Session Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Main Logic
if prompt := st.chat_input("DHA Karachi ke baare mein poochein..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # AI Response Generation
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a DHA Karachi property expert."},
                *st.session_state.messages
            ]
        )
        # Yahan 'response' ko define kiya gaya hai sahi line par
        response = completion.choices[0].message.content
        st.markdown(response)
    
    # Save response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
