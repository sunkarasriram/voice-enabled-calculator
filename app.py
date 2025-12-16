import streamlit as st
import numpy as np

st.set_page_config(page_title="Voice Enabled Calculator", layout="centered")

st.title("🎙️ Voice Enabled Calculator")

st.write("Speak or type a mathematical expression")

expression = st.text_input("Enter expression (example: 5 + 6 * 2)")

if st.button("Calculate"):
    try:
        result = eval(expression)
        st.success(f"Result: {result}")
    except:
        st.error("Invalid Expression")

st.markdown("---")
st.caption("Python | NLP | NumPy | Streamlit")
