import os
import streamlit as st
import openai

# Configuring Openai - api key
openai.api_key = "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"

# Configuring streamlit page settings
st.set_page_config(
    page_title="💬" "GHD AI Energy Estimator Tool",
    page_icon="🤖",
    layout="centered"
)

# Initialize chat session in streamlit if not already present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Streamlit Page title
st.title("🤖" "GHD AI Energy Estimator Tool")

#display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# input field for user's message
user_prompt = st.chat_input("Ask me about anything related to Energy consumption.")

if user_prompt:

    # add user's message to chat and display it streamlit run src/main.py
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # send user's message to GPT-4o and get a response
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": ( "You are an expert consultant. Only answer questions strictly related to" 
                                            "energy consumption, usage, efficiency, HVAC, insulation, power costs, and related engineering."
                                            "If the user asks anything outside of these domains, in a funny way say you are only trained to respond"
                                            "to energy-related topics."
                                            )
            },
            *st.session_state.chat_history
        ]
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # display GPT-4o's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)



