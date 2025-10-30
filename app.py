import streamlit as st
import time
import random

# 🌱 Page setup
st.set_page_config(page_title="🌿 GreenifyAI", layout="centered")

# 🌳 Custom CSS for background and design
st.markdown("""
    <style>
    body {
        background: url('https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1650&q=80');
        background-size: cover;
        background-position: center;
        font-family: 'Poppins', sans-serif;
    }

    .main {
        background: rgba(0, 0, 0, 0.55);
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
        background: linear-gradient(145deg, #8c8c8c, #3b3b3b);
        color: white;
        align-self: flex-end;
        border: 1px solid #5a5a5a;
    }

    /* AI message */
    .ai {
        background: linear-gradient(145deg, #6a6a6a, #2f2f2f);
        color: #f0f0f0;
        border: 1px solid #555;
        box-shadow: 0 0 10px rgba(80, 255, 80, 0.3);
    }

    /* Text animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* "Thinking..." animation */
    .thinking {
        font-style: italic;
        color: #e0e0e0;
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

    .login-card {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        backdrop-filter: blur(8px);
        color: white;
        width: 360px;
        margin: auto;
        margin-top: 10%;
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.15);
    }

    input {
        border-radius: 10px;
        border: none;
        padding: 10px;
        width: 80%;
        text-align: center;
        margin-top: 10px;
    }

    </style>
""", unsafe_allow_html=True)

# 🌺 Floating leaves design
for i in range(6):
    st.markdown(f"<div class='leaf' style='left:{i*15+8}%; animation-delay:{i*1.4}s;'></div>", unsafe_allow_html=True)

# 🧍 Name Entry System
if "username" not in st.session_state:
    with st.container():
        st.markdown("""
            <div class="login-card">
                <h2>🌿 Welcome to <b>GreenifyAI</b></h2>
                <p>Enter your name to begin your eco journey 🌎</p>
            </div>
        """, unsafe_allow_html=True)
        username = st.text_input("👤 Your Name:")
        if st.button("Start Chat 🌱") and username.strip() != "":
            st.session_state.username = username.strip().title()
            st.session_state.messages = [("ai", f"🌍 Hello {st.session_state.username}! Welcome to GreenifyAI 🌿 I'm here to share eco-friendly habits, recycling tips, and sustainability ideas with you ♻️")]
            st.rerun()
        st.stop()

# 🌳 Header
st.markdown("<h1 style='text-align:center; color:white;'>🌍 GreenifyAI</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#f0f0f0;'>Chatting with {st.session_state.username} 🍃</p>", unsafe_allow_html=True)

# 🌾 Display chat
for msg in st.session_state.messages:
    role, text = msg
    bubble_class = "user" if role == "user" else "ai"
    st.markdown(f"<div class='chat-bubble {bubble_class}'>{text}</div>", unsafe_allow_html=True)

# 🌸 Chat input
user_input = st.chat_input("Ask GreenifyAI about recycling or eco habits 🌿")

# 🍀 Response system
if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.spinner("🌱 Thinking..."):
        time.sleep(2)

    responses = [
        f"🌳 Great question, {st.session_state.username}! Recycling reduces landfill waste and helps save natural energy 🌎",
        f"♻️ {st.session_state.username}, try reusing cardboard or bottles to make eco-friendly DIY projects — just like our comic idea!",
        f"🌿 Remember to separate wet and dry waste, {st.session_state.username}, it makes composting so much easier 🌻",
        f"🍃 Using vegetable-based ink pens is an awesome way to stay sustainable, {st.session_state.username}! 🖊️",
        f"🌼 Each time you recycle, {st.session_state.username}, you’re making the planet a little greener 💚"
    ]
    ai_reply = random.choice(responses)
    st.session_state.messages.append(("ai", ai_reply))
    st.rerun()
