import streamlit as st
import time
import random
import re

# 🌱 Page setup
st.set_page_config(page_title="🌿 GreenifyAI", layout="centered")

# 🌳 Ultra-Realistic Nature Background + Dynamic Glass UI
st.markdown("""
    <style>
    /* 🌲 Background setup */
    [data-testid="stAppViewContainer"] {
        background-image: url('https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1950&q=80');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        overflow: hidden;
        animation: bgZoom 40s ease-in-out infinite alternate;
    }

    @keyframes bgZoom {
        from { background-size: 100%; }
        to { background-size: 110%; }
    }

    [data-testid="stHeader"], [data-testid="stToolbar"] {
        background: rgba(0,0,0,0);
    }

    /* 🌟 Title Glow */
    h1 {
        text-align: center;
        color: #eaffea;
        font-size: 3.2em;
        text-shadow: 0 0 25px #00ff80, 0 0 40px #00cc66;
        animation: pulseGlow 2.5s ease-in-out infinite alternate;
    }

    @keyframes pulseGlow {
        from { text-shadow: 0 0 10px #00ff80; }
        to { text-shadow: 0 0 40px #00ff99, 0 0 70px #00ffaa; }
    }

    /* ✨ Main chat container */
    .main {
        background: rgba(0, 0, 0, 0.55);
        border-radius: 24px;
        padding: 32px;
        backdrop-filter: blur(8px);
        box-shadow: 0 0 25px rgba(0,255,140,0.15);
        animation: fadeIn 1s ease;
    }

    /* 💬 Chat bubbles */
    .chat-bubble {
        padding: 14px 18px;
        border-radius: 20px;
        margin: 8px 0;
        max-width: 80%;
        word-wrap: break-word;
        animation: fadeUp 0.7s ease;
        font-family: 'Poppins', sans-serif;
        line-height: 1.6;
        transition: transform 0.2s ease;
    }

    .chat-bubble:hover {
        transform: scale(1.02);
    }

    /* 👤 User bubble */
    .user {
        background: linear-gradient(145deg, #3b3b3b, #1c1c1c);
        color: white;
        align-self: flex-end;
        border: 1px solid #666;
        box-shadow: 0 0 15px rgba(200, 255, 200, 0.1);
    }

    /* 🤖 AI bubble */
    .ai {
        background: linear-gradient(145deg, #00b36b, #005533);
        color: #eaffea;
        border: 1px solid #44ff99;
        box-shadow: 0 0 18px rgba(0, 255, 140, 0.3);
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* 🌱 Typing indicator */
    .typing {
        color: #c6ffd0;
        font-style: italic;
        animation: blink 1.2s infinite;
    }
    @keyframes blink {
        50% { opacity: 0.4; }
    }

    /* 🍃 Floating emojis */
    .floaty {
        position: absolute;
        font-size: 26px;
        opacity: 0.6;
        animation: drift 15s infinite ease-in-out;
    }

    @keyframes drift {
        0% { transform: translateY(0) rotate(0); opacity: 0.8; }
        50% { transform: translateY(-700px) rotate(180deg); opacity: 0.4; }
        100% { transform: translateY(-1400px) rotate(360deg); opacity: 0.8; }
    }

    /* 🌍 Login Card */
    .login-card {
        background: rgba(0, 0, 0, 0.6);
        border-radius: 20px;
        padding: 35px;
        text-align: center;
        backdrop-filter: blur(10px);
        color: white;
        width: 360px;
        margin: auto;
        margin-top: 10%;
        box-shadow: 0 0 30px rgba(0, 255, 140, 0.2);
        animation: fadeIn 1.2s ease;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: scale(0.95); }
        to { opacity: 1; transform: scale(1); }
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

# 🍃 Add floating emojis
emojis = ["🌿", "🍃", "🌸", "🦋", "🌼", "🌺"]
for i, emoji in enumerate(emojis * 3):
    st.markdown(f"<div class='floaty' style='left:{i*8+5}%; animation-delay:{i*1.1}s;'>{emoji}</div>", unsafe_allow_html=True)

# -----------------------
# 🌾 Response Generator
# -----------------------
def generate_response(user_text: str, username: str) -> str:
    t = user_text.lower().strip()
    responses = {
        "hello": f"🌿 Hey {username}! How’s your eco day going?",
        "comic": "📖 Our comic *The Recycle Squad* spreads green lessons through fun eco adventures!",
        "recycle": "♻️ Separate wet and dry waste, clean plastics before recycling, and reuse glass jars 🌍",
        "plastic": "🧴 Ditch single-use plastic — reusable bottles and cloth bags are the way! 🌱",
        "compost": "🌱 Compost turns food waste into gold for your garden 🌼!",
    }
    for k in responses:
        if k in t:
            return responses[k]
    return f"🌎 Great thought, {username}! Every small act of care helps our planet thrive 🌳"

# -----------------------
# 🧍 Login System
# -----------------------
if "username" not in st.session_state:
    with st.container():
        st.markdown("""
            <div class="login-card">
                <h2>🌿 Welcome to <b>GreenifyAI</b></h2>
                <p>Enter your name to start your eco adventure 🌎</p>
            </div>
        """, unsafe_allow_html=True)
        username = st.text_input("👤 Your Name:")
        if st.button("Start Chat 🌱") and username.strip():
            st.session_state.username = username.strip().title()
            st.session_state.messages = [
                ("ai", f"🌍 Hello {st.session_state.username}! Welcome to GreenifyAI 🌿 Let’s make our world greener together 🌱")
            ]
            st.rerun()
        st.stop()

# -----------------------
# 🌍 Chat Header
# -----------------------
st.markdown("<h1>🌿 GreenifyAI</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#e0ffe5;'>Chatting with {st.session_state.username} 🌳</p>", unsafe_allow_html=True)

# -----------------------
# 💬 Chat Display
# -----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    role, text = msg
    bubble_class = "user" if role == "user" else "ai"
    st.markdown(f"<div class='chat-bubble {bubble_class}'>{text}</div>", unsafe_allow_html=True)

# -----------------------
# 🌸 User Input & Response
# -----------------------
user_input = st.chat_input("Ask me about recycling, composting, or green habits 🌱")

if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.spinner("🌱 GreenifyAI is thinking..."):
        time.sleep(random.uniform(1.3, 2.2))
    reply = generate_response(user_input, st.session_state.username)
    st.session_state.messages.append(("ai", reply))
    st.rerun()
