import streamlit as st
from ai_service import generate_response
from critique import analyze_business_idea
from profit import profitability_analysis
from partnerships import find_partnerships
from visual import display_business_model

st.title("SoundBoard: Your AI Business Advisor")

st.write("Get AI-powered insights to refine your business ideas.")

# User input for business idea
idea = st.text_area("Describe your business idea:", placeholder="Enter your business concept here...")

if st.button("Analyze My Idea"):
    if idea.strip() == "":
        st.warning("Please enter a business idea to analyze.")
    else:
        st.subheader("AI-Generated Critique:")
        critique_response = generate_response(f"Critique this business idea: {idea}")
        st.write(critique_response)

        st.subheader("Profitability Analysis:")
        profitability_response = generate_response(f"Analyze the profitability of this business: {idea}")
        st.write(profitability_response)

        st.subheader("Strategic Partnerships:")
        partnerships_response = generate_response(f"Suggest strategic partnerships for: {idea}")
        st.write(partnerships_response)

        st.subheader("Business Model Canvas:")
        display_business_model()

st.markdown("---")
st.info("Powered by DeepSeek AI")
