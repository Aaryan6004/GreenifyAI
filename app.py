import streamlit as st

# 🌿 GreenifyAI - The Recycle Squad Chatbot
# This app helps users learn about recycling, waste management, and eco-friendly habits.

st.set_page_config(page_title="🌿 GreenifyAI", page_icon=♻️", layout="centered")

# Header
st.markdown("<h1 style='text-align:center; color:green;'>🌿 GreenifyAI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Your friendly recycling and waste management assistant</p>", unsafe_allow_html=True)
st.write("---")

# User input
user_input = st.text_input("💬 Ask GreenifyAI about recycling, solid waste, or eco-friendly materials:")

# Chatbot logic
if user_input:
    response = ""

    # Simple rule-based responses
    if "plastic" in user_input.lower():
        response = "Plastic should be cleaned, sorted, and sent to a recycling center. Try to reduce single-use plastic whenever possible ♻️."
    elif "compost" in user_input.lower():
        response = "Composting helps turn organic waste into fertilizer! You can compost fruit peels, leaves, and food scraps 🌱."
    elif "paper" in user_input.lower():
        response = "Paper can be reused or recycled into new sheets. Avoid wasting paper and recycle your notebooks and packaging 📘."
    elif "metal" in user_input.lower():
        response = "Metal waste like cans can be melted and reused endlessly. Rinse and recycle them at collection centers 🥫."
    elif "recycle" in user_input.lower():
        response = "Recycling means converting waste into new materials. Separate dry and wet waste to make it easier 🌍."
    elif "waste" in user_input.lower():
        response = "Solid waste management involves segregation, composting, recycling, and reducing waste production 🚮."
    elif "book" in user_input.lower() or "comic" in user_input.lower():
        response = "Our DIY comic teaches young adults about recycling habits and waste management, made with eco-friendly materials 📚."
    else:
        response = "I'm GreenifyAI 🌿 — I can help you learn about recycling, composting, and waste reduction. Try asking about plastic, compost, or solid waste!"

    # Display bot response
    st.success(response)
else:
    st.info("Type your question above to chat with GreenifyAI 🌿")
