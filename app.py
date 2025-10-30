import streamlit as st
import time
import random
import re

# 🌱 Page setup
st.set_page_config(page_title="🌿 GreenifyAI", layout="centered")

# 🌳 Ultra-Realistic Nature Background + Glassmorphism UI
st.markdown("""
    <style>
    /* Background */
    [data-testid="stAppViewContainer"] {
        background-image: url('https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1950&q=80');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        overflow: hidden;
    }

    [data-testid="stHeader"], [data-testid="stToolbar"] {
        background: rgba(0,0,0,0);
    }

    /* Glowing animated title */
    h1 {
        text-align: center;
        color: #eaffea;
        font-size: 3em;
        text-shadow: 0 0 15px #00ff80, 0 0 25px #00cc66;
        animation: glow 2s ease-in-out infinite alternate;
    }

    @keyframes glow {
        from { text-shadow: 0 0 15px #00ff80; }
        to { text-shadow: 0 0 25px #00cc66, 0 0 40px #00ff99; }
    }

    /* Chat container */
    .main {
        background: rgba(0, 0, 0, 0.55);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(6px);
        animation: fadeIn 0.8s ease;
    }

    /* Chat bubbles */
    .chat-bubble {
        padding: 12px 16px;
        border-radius: 18px;
        margin: 8px 0;
        max-width: 80%;
        word-wrap: break-word;
        animation: floatUp 0.6s ease;
        font-family: 'Poppins', sans-serif;
        line-height: 1.5;
    }

    /* User bubble */
    .user {
        background: linear-gradient(145deg, #4e4e4e, #222);
        color: white;
        align-self: flex-end;
        border: 1px solid #666;
        box-shadow: 0 0 15px rgba(200, 255, 200, 0.15);
    }

    /* AI bubble */
    .ai {
        background: linear-gradient(145deg, #009966, #004d26);
        color: #f0fff0;
        border: 1px solid #44ff99;
        box-shadow: 0 0 15px rgba(0, 255, 140, 0.3);
    }

    @keyframes floatUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Typing indicator */
    .typing {
        color: #d2ffd2;
        font-style: italic;
        animation: blink 1.5s infinite;
    }
    @keyframes blink {
        50% { opacity: 0.4; }
    }

    /* Floating leaves 🌿 */
    .leaf {
        position: absolute;
        width: 25px;
        height: 25px;
        background: url('https://cdn-icons-png.flaticon.com/512/765/765441.png');
        background-size: contain;
        opacity: 0.7;
        filter: drop-shadow(0 0 8px #00ff88);
        animation: float 14s infinite linear;
    }

    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); opacity: 0.8; }
        50% { opacity: 0.5; }
        100% { transform: translateY(-900px) rotate(360deg); opacity: 0.8; }
    }

    /* Login card */
    .login-card {
        background: rgba(0, 0, 0, 0.6);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        backdrop-filter: blur(8px);
        color: white;
        width: 360px;
        margin: auto;
        margin-top: 10%;
        box-shadow: 0 0 25px rgba(0, 255, 140, 0.2);
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

# 🌺 Floating leaves animation
for i in range(8):
    st.markdown(f"<div class='leaf' style='left:{i*12+5}%; animation-delay:{i*1.2}s;'></div>", unsafe_allow_html=True)

# -----------------------
# Response Generator
# -----------------------
def generate_response(user_text: str, username: str) -> str:
    t = user_text.lower().strip()
    responses = {
        "hello": f"🌿 Hey {username}! How’s your eco day going?",
        "comic": "📚 Our DIY comic ‘The Recycle Squad’ teaches recycling and waste management using fun stories made from cardboard and eco-materials!",
        "recycle": "♻️ Always separate dry and wet waste. Dry includes paper, plastic, and glass; wet includes food scraps. Keep them clean before recycling!",
        "plastic": "🧴 Reduce single-use plastics — reuse bottles, or switch to metal or glass containers.",
        "compost": "🌱 Composting converts food waste into natural fertilizer — perfect for gardens!",
    }
    for k in responses:
        if k in t:
            return responses[k]
    return f"🌍 Good thought, {username}! Remember: every small eco-action adds up. Want a tip on composting, recycling, or our comic?"

# -----------------------
# Name Entry
# -----------------------
if "username" not in st.session_state:
    with st.container():
        st.markdown("""
            <div class="login-card">
                <h2>🌿 Welcome to <b>GreenifyAI</b></h2>
                <p>Enter your name to begin your green journey 🌎</p>
            </div>
        """, unsafe_allow_html=True)
        username = st.text_input("👤 Your Name:")
        if st.button("Start Chat 🌱") and username.strip():
            st.session_state.username = username.strip().title()
            st.session_state.messages = [("ai", f"🌍 Hello {st.session_state.username}! Welcome to GreenifyAI 🌿 Let's build eco-friendly habits together ♻️")]
            st.rerun()
        st.stop()

# Header
st.markdown("<h1>🌿 GreenifyAI</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#cfead9;'>Chatting with {st.session_state.username} 🌱</p>", unsafe_allow_html=True)

# Show chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    role, text = msg
    bubble_class = "user" if role == "user" else "ai"
    st.markdown(f"<div class='chat-bubble {bubble_class}'>{text}</div>", unsafe_allow_html=True)

# Input box
user_input = st.chat_input("Type your question about recycling, composting, or our comic 🌿")

if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.spinner("🌱 GreenifyAI is thinking..."):
        time.sleep(random.uniform(1.5, 2.3))
    reply = generate_response(user_input, st.session_state.username)
    st.session_state.messages.append(("ai", reply))
    st.rerun()
