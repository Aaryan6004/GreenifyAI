import streamlit as st
import time
import random

# 🌱 Page Setup
st.set_page_config(page_title="🌿 GreenifyAI", layout="centered")

# 🌳 Custom CSS for styling
st.markdown("""
    <style>
    body {
        background: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1650&q=80');
        background-size: cover;
        background-position: center;
        font-family: 'Poppins', sans-serif;
    }

    /* Chat container */
    .chat-bubble {
        padding: 12px 16px;
        border-radius: 18px;
        margin: 8px 0;
        max-width: 80%;
        word-wrap: break-word;
        animation: fadeIn 0.6s ease;
    }

    /* User message */
    .user {
        background: linear-gradient(145deg, #8d8d8d, #4e4e4e);
        color: white;
        align-self: flex-end;
        border: 1px solid #5e5e5e;
    }

    /* AI message */
    .ai {
        background: linear-gradient(145deg, #6d6d6d, #3a3a3a);
        color: #f0f0f0;
        border: 1px solid #555;
        box-shadow: 0 0 10px rgba(50, 255, 50, 0.2);
    }

    /* Text animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* "Thinking..." animation */
    .thinking {
        font-style: italic;
        color: #dcdcdc;
        animation: blink 1.4s infinite;
    }

    @keyframes blink {
        0%, 100% { opacity: 0.4; }
        50% { opacity: 1; }
    }

    /* Floating leaves animation */
    .leaf {
        position: absolute;
        width: 20px;
        height: 20px;
        background: url('https://cdn-icons-png.flaticon.com/512/765/765441.png');
        background-size: contain;
        opacity: 0.4;
        animation: float 10s infinite linear;
    }

    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        100% { transform: translateY(-800px) rotate(360deg); }
    }

    </style>
""", unsafe_allow_html=True)

# 🍃 Header
st.markdown("<h1 style='text-align:center; color:white;'>🌍 GreenifyAI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#f0f0f0;'>Your eco-friendly guide for recycling & sustainable habits ♻️</p>", unsafe_allow_html=True)

# 🌺 Floating leaves design
for i in range(8):
    st.markdown(f"<div class='leaf' style='left:{i*10+10}%; animation-delay:{i*1.5}s;'></div>", unsafe_allow_html=True)

# 🪴 Memory for conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🌸 Chat input
user_input = st.chat_input("Ask GreenifyAI about recycling, waste management, or eco habits 🌿")

# 🌾 Display chat
for msg in st.session_state.messages:
    role, text = msg
    bubble_class = "user" if role == "user" else "ai"
    st.markdown(f"<div class='chat-bubble {bubble_class}'>{text}</div>", unsafe_allow_html=True)

# 🍀 AI response system
if user_input:
    st.session_state.messages.append(("user", user_input))

    with st.spinner("🌱 Thinking..."):
        time.sleep(2)  # Simulate processing

    responses = [
        "🌎 That's a great question! Recycling helps reduce landfill waste and saves energy 🌱",
        "♻️ Try reusing materials like cardboard, bottles, or paper to make DIY crafts — just like we did in our comic project!",
        "🌿 Separate your wet and dry waste — it makes composting and recycling much easier!",
        "🌻 Did you know? Using vegetable dye pens like ours can help reduce chemical pollution 🖊️💧",
        "🍃 Always look for recyclable symbols on packaging — every small step counts toward a greener planet 🌏"
    ]
    ai_reply = random.choice(responses)

    st.session_state.messages.append(("ai", ai_reply))
    st.rerun()
