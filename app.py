import streamlit as st
from critique import analyze_business_idea
from profit import profitability_analysis
from partnerships import find_partnerships
from visual import display_business_model

st.title("SoundBoard: Your AI Business Advisor")

idea = st.text_area("Describe your business idea:")

if st.button("Analyze"):
    st.subheader("Critique:")
    st.write(analyze_business_idea(idea))

    st.subheader("Profitability:")
    st.write(profitability_analysis(idea))

    st.subheader("Partnerships:")
    st.write(find_partnerships(idea))

    st.subheader("Business Model Canvas:")
    display_business_model()
