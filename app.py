import streamlit as st

# 🌿 GreenifyAI - Eco-Friendly Chatbot
# A nature-themed chatbot that teaches recycling and waste management

st.set_page_config(page_title="🌿 GreenifyAI", page_icon="♻️", layout="centered")

# --- Custom Page Styling ---
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(180deg, #e9f5e1, #f7fff3);
            font-family: 'Comic Sans MS', sans-serif;
        }
        .chat-bubble {
            padding: 10px 15px;
            border-radius: 20px;
            margin: 8px 0;
            width: fit-content;
            max-width: 80%;
            word-wrap: break-word;
        }
        .user-bubble {
            background-color: #d1ffd1;
            margin-left: auto;
            color: #004400;
        }
        .bot-bubble {
            background-color: #f0fff0;
            color: #1a4d1a;
            border: 1px solid #b3e6b3;
        }
        .header {
            text-align: center;
            color: green;
            font-size: 32px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header ---
st.markdown("<h1 class='header'>🌿 GreenifyAI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Your Eco-Friendly Chat Assistant — here to talk about recycling and sustainable living ♻️</p>", unsafe_allow_html=True)
st.write("---")

# --- Initialize chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "content": "Hi! I'm GreenifyAI 🌿 — I’m here to help you learn about recycling, composting, and waste management. What would you like to know today?"}
    ]

# --- Display chat history ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble bot-bubble'>{msg['content']}</div>", unsafe_allow_html=True)

# --- User input ---
user_input = st.chat_input("Type your message here...")

# --- Chatbot response system ---
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    user_text = user_input.lower()
    response = ""

    # --- Smart eco responses ---
    if "plastic" in user_text:
        response = "Plastic pollution is a huge problem 🌎. Try to reuse bottles, avoid single-use plastics, and recycle cleaned containers properly."
    elif "recycle" in user_text or "recycling" in user_text:
        response = "Recycling means converting waste into reusable material ♻️. Always separate dry and wet waste before disposal!"
    elif "compost" in user_text:
        response = "Composting is awesome 🌱! Collect food scraps, peels, and leaves — let them decompose to make natural fertilizer."
    elif "metal" in user_text:
        response = "Metals like aluminum and steel can be melted down infinitely 🔁. Rinse and sort them before sending to recycling centers."
    elif "paper" in user_text:
        response = "Paper can be reused or recycled into new sheets 📘. Save trees by minimizing waste and reusing notebooks!"
    elif "waste" in user_text or "garbage" in user_text:
        response = "Good waste management means reducing, reusing, and recycling 🪴. Sort biodegradable and non-biodegradable items separately."
    elif "comic" in user_text or "book" in user_text:
        response = "Our DIY comic teaches young adults and teens about eco-habits using recycled cardboard and vegetable-dye pens 📚."
    elif "hi" in user_text or "hello" in user_text:
        response = "Hey there 🌿! I'm GreenifyAI, your friendly recycling buddy. How can I help you today?"
    else:
        response = "I'm still learning 🌍 — but I can tell you about recycling, composting, eco-friendly materials, or waste management tips!"

    # --- Add bot response ---
    st.session_state.messages.append({"role": "bot", "content": response})

    # --- Refresh chat ---
    st.rerun()
