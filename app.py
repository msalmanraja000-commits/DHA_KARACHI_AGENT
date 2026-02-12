import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(page_title="DHA Karachi AI Advisor", page_icon="🏝️")

# 2. Secret API Key Setup (Professional Way)
# Salman bhai, yahan ab key nahi likhni, sirf ye line copy karein:
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=GROQ_API_KEY)

# 3. System Prompt
system_prompt = """
You are the 'DHA Karachi Elite Advisor'. 
Expertise: DHA Phases 1-8 and DHA City Karachi. 
Provide professional advice on property, lease types, and taxes.
"""

st.title("🏝️ DHA Karachi AI Advisor")
st.markdown("---")

# 4. Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. User Input & AI Response
if prompt := st.chat_input("DHA Karachi ke baare mein poochein..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Calling Groq with Llama 3.3
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                *st.session_state.messages
            ],
        )
        response = completion.choices[0].message.content
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
