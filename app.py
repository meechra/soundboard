import streamlit as st
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
        with st.spinner("Analyzing your business idea..."):
            st.subheader("AI-Generated Critique:")
            critique_response = analyze_business_idea(idea)
            st.write(critique_response)

            st.subheader("Profitability Analysis:")
            profitability_response = profitability_analysis(idea)
            st.write(profitability_response)

            st.subheader("Strategic Partnerships:")
            partnerships_response = find_partnerships(idea)
            st.write(partnerships_response)

            st.subheader("Business Model Canvas:")
            display_business_model()

st.markdown("---")
st.info("Powered by DeepSeek AI")
