import streamlit as st
import openai
import os

# OpenAI API key 
openai.api_key = "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"  # Replace with your actual API key

# Function to ask GPT a question, strictly limited to energy consumption topics
def ask_energy_question(question):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert energy consultant. Only answer questions strictly related to "
                        "energy consumption, usage, efficiency, HVAC, insulation, power costs, and related engineering. "
                        "If the user asks anything outside of these domains, in a funny way say you are only trained to respond "
                        "to energy-related topics."
                    )
                },
                {"role": "user", "content": question}
            ],
            temperature=0.3,
            max_tokens=300
        )
        return response.choices[0].message.content

    except openai.APIError as e:
        return f"OpenAI API Error: {e}"
    except Exception as ex:
        return f"Unexpected error: {ex}"

# Streamlit UI Setup
st.set_page_config(page_title="Energy Estimator", page_icon="🔋")

# --- Header Section ---
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color: #2c3e50;'>🔋 AI Energy Estimation Assistant</h1>
        <p style='font-size:18px;'>Here to answer questions related to energy consumption, usage, and efficiency.</p>
    </div>
    """, unsafe_allow_html=True
)

# --- Input Section ---
with st.container():
    st.subheader("💡 Ask Your Energy-Related Question")
    st.markdown("*Examples:*\n- How much energy is needed to cool a 1200 sq ft house?\n- What's the power usage of an AC running for 6 hours a day?\n- How can I improve insulation to reduce heating costs?")
    
    question = st.text_input("Enter your question below:", placeholder="e.g., energy required to cool a 1200 sq ft house")

    if st.button("🔍 Get Estimate"):
        if question.strip():
            with st.spinner("Calculating energy insights..."):
                answer = ask_energy_question(question)
                st.success("✅ Estimate:")
                st.write(answer)
        else:
            st.warning("Please enter a question.")

# --- Footer ---
st.markdown(
    """
    <hr style="margin-top: 2em;">
    <div style='text-align: center; font-size: 14px; color: gray;'>
        Built using GPT-4o by IntuiNext Inc. | Restricted to energy usage topics only.
    </div>
    """, unsafe_allow_html=True
)
