import streamlit as st
import time
import random

# 🌱 Page Setup
st.set_page_config(page_title="🌿 GreenifyAI", layout="centered")

# 🌳 Custom CSS for Styling + Background
st.markdown("""
    <style>
    body {
        background: url('https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1650&q=80');
        background-size: cover;
        background-position: center;
        font-family: 'Poppins', sans-serif;
    }

    .main {
        background: rgba(0, 0, 0, 0.6);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(6px);
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
        background: linear-gradient(145deg, #8a8a8a, #3d3d3d);
        color: white;
        align-self: flex-end;
        border: 1px solid #5e5e5e;
    }

    /* AI message */
    .ai {
        background: linear-gradient(145deg, #707070, #2f2f2f);
        color: #f0f0f0;
        border: 1px solid #555;
        box-shadow: 0 0 10px rgba(50, 255, 50, 0.3);
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
        width: 22px;
        height: 22px;
        background: url('https://cdn-icons-png.flaticon.com/512/765/765441.png');
        background-size: contain;
        opacity: 0.5;
        animation: float 10s infinite linear;
    }

    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        100% { transform: translateY(-800px) rotate(360deg); }
    }

    /* Login screen */
    .login-card {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        backdrop-filter: blur(8px);
        color: white;
        width: 350px;
        margin: auto;
        margin-top: 10%;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.15);
    }

    .google-btn {
        background: white;
        color: #555;
        padding: 10px 20px;
        border-radius: 30px;
        border: none;
        font-weight: bold;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        cursor: pointer;
        transition: 0.3s;
    }

    .google-btn:hover {
        background: #e8e8e8;
    }

    </style>
""", unsafe_allow_html=True)

# 🌺 Floating leaves design
for i in range(8):
    st.markdown(f"<div class='leaf' style='left:{i*10+10}%; animation-delay:{i*1.5}s;'></div>", unsafe_allow_html=True)

# 🪴 Mock Login System
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("""
        <div class="login-card">
            <h2>🌿 Welcome to <b>GreenifyAI</b></h2>
            <p>Sign in to start your eco journey 🌎</p>
            <button class="google-btn" id="login-btn">
                <img src="https://www.svgrepo.com/show/475656/google-color.svg" width="20">
                Continue with Google
            </button>
        </div>
    """, unsafe_allow_html=True)

    # Simulate login button
    if st.button("Simulate Login ✅"):
        st.session_state.logged_in = True
        st.rerun()
    st.stop()

# 🌳 Header
st.markdown("<h1 style='text-align:center; color:white;'>🌍 GreenifyAI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#f0f0f0;'>Your eco-friendly guide for recycling & sustainable habits ♻️</p>", unsafe_allow_html=True)

# 🧠 Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🌸 Chat input
user_input = st.chat_input("Ask GreenifyAI about recycling, waste management, or eco habits 🌿")

# 🌾 Display chat
for msg in st.session_state.messages:
    role, text = msg
    bubble_class = "user" if role == "user" else "ai"
    st.markdown(f"<div class='chat-bubble {bubble_class}'>{text}</div>", unsafe_allow_html=True)

# 🌻 AI response system
if user_input:
    st.session_state.messages.append(("user", user_input))

    with st.spinner("🌱 Thinking..."):
        time.sleep(2)  # Simulated thinking delay

    responses = [
        "🌍 That’s a great question! Recycling helps reduce landfill waste and saves natural energy 🌿",
        "♻️ You can reuse old boxes, bottles, and paper to create eco-friendly art — just like we did for our comic!",
        "🌱 Separate wet and dry waste — it makes composting and recycling easier and cleaner 💧",
        "🖊️ Our vegetable-dye pens reduce chemical use — a small but powerful step for sustainability!",
        "🍃 Always check recycling symbols on packaging — every small habit adds up to a greener Earth 🌏"
    ]
    ai_reply = random.choice(responses)

    st.session_state.messages.append(("ai", ai_reply))
    st.rerun()
