import streamlit as st
import time
import random
from datetime import datetime

# 🌿 GREENIFYAI — ECO EVOLUTION v3

st.set_page_config(page_title="🌿 GreenifyAI", layout="wide")

# ---------- CSS STYLING ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

[data-testid="stAppViewContainer"] {
    background-image: url('https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=2000&q=80');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.main {
    background: rgba(0, 0, 0, 0.45);
    border-radius: 20px;
    padding: 20px 40px;
    backdrop-filter: blur(10px);
    box-shadow: 0 0 40px rgba(0, 255, 120, 0.15);
    max-width: 850px;
    margin: auto;
}

h1, h2, h3, p, div {
    font-family: 'Poppins', sans-serif;
}

.chat-bubble {
    padding: 14px 18px;
    border-radius: 18px;
    margin: 8px 0;
    max-width: 75%;
    word-wrap: break-word;
    animation: fadeIn 0.6s ease-in-out;
    font-size: 16px;
}

.user {
    background: linear-gradient(135deg, #4e4e4e, #1c1c1c);
    color: white;
    align-self: flex-end;
    border: 1px solid #6f6f6f;
    margin-left: auto;
}

.ai {
    background: linear-gradient(135deg, #6f6f6f, #2f2f2f);
    color: #f4f4f4;
    border: 1px solid #55ff99;
    box-shadow: 0 0 15px rgba(80, 255, 150, 0.35);
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}

.thinking {
    font-style: italic;
    color: #b8ffcf;
    font-size: 15px;
    animation: blink 1.5s infinite;
}
@keyframes blink {
    0%,100% {opacity: 0.3;}
    50% {opacity: 1;}
}

/* Floating animated leaves */
.leaf {
    position: absolute;
    width: 25px;
    height: 25px;
    background: url('https://cdn-icons-png.flaticon.com/512/765/765441.png');
    background-size: contain;
    opacity: 0.7;
    animation: float 15s infinite linear;
}
@keyframes float {
    0% { transform: translateY(0px) rotate(0deg); }
    100% { transform: translateY(-1200px) rotate(360deg); }
}

/* Download button style */
.stDownloadButton button {
    background: linear-gradient(90deg, #00ff99, #009966);
    color: white !important;
    font-weight: 600;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- FLOATING LEAVES ----------
for i in range(8):
    st.markdown(f"<div class='leaf' style='left:{i*12+5}%; animation-delay:{i*2}s;'></div>", unsafe_allow_html=True)

# ---------- LOGIN SYSTEM ----------
if "username" not in st.session_state:
    st.markdown("""
        <div style="text-align:center; margin-top:15%;">
            <h2 style="color:white;">🌿 Welcome to <b>GreenifyAI</b></h2>
            <p style="color:#d9ffd9;">Enter your name to begin your eco adventure 🌏</p>
        </div>
    """, unsafe_allow_html=True)
    username = st.text_input("👤 Your Name:")
    if st.button("Start Chat 🌱") and username.strip():
        st.session_state.username = username.strip().title()
        st.session_state.messages = [
            ("ai", f"🌍 Hello {st.session_state.username}! Welcome to GreenifyAI 🌿 Let's make the planet greener together 💚. Ask me anything about recycling, sustainability, or waste management ♻️")
        ]
        st.rerun()
    st.stop()

# ---------- HEADER ----------
st.markdown(f"<h1 style='text-align:center; color:white;'>🌎 GreenifyAI</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#b3ffcc;'>Chatting with {st.session_state.username} 🍃</p>", unsafe_allow_html=True)

# ---------- CHAT AREA ----------
chat_container = st.container()
with chat_container:
    for role, text in st.session_state.messages:
        bubble_class = "user" if role == "user" else "ai"
        st.markdown(f"<div class='chat-bubble {bubble_class}'>{text}</div>", unsafe_allow_html=True)

# ---------- CHAT INPUT ----------
user_input = st.chat_input("Ask GreenifyAI something 🌿")

# ---------- SMART AI SYSTEM ----------
if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.spinner("🌱 Thinking..."):
        st.markdown("<div class='thinking'>🌿 Thinking...</div>", unsafe_allow_html=True)
        time.sleep(2)

    text = user_input.lower()
    reply = ""

    # 🧠 Keyword-based intelligent responses
    if "plastic" in text:
        reply = "🚯 Plastic takes hundreds of years to decompose. Try using reusable bottles and cloth bags 🌿."
    elif "recycle" in text or "recycling" in text:
        reply = "♻️ Recycling transforms waste into valuable materials! Separate paper, plastic, and metal before disposal 🌍."
    elif "compost" in text:
        reply = "🌱 Composting is nature’s magic! Collect food scraps and dry leaves — they’ll turn into natural fertilizer 🍂."
    elif "water" in text:
        reply = "💧 Conserve water by turning off taps and reusing rainwater when possible 🌦️."
    elif "metal" in text:
        reply = "🪙 Metals like aluminum can be recycled infinitely without losing quality! Rinse cans before disposal."
    elif "paper" in text:
        reply = "📄 Each ton of recycled paper saves about 17 trees 🌳 — reuse sheets before discarding!"
    elif "waste" in text or "garbage" in text:
        reply = "🚮 Sort your waste: biodegradable and non-biodegradable. It helps the recycling process immensely ♻️."
    elif "energy" in text:
        reply = "⚡ Switching to renewable energy sources like solar can drastically reduce your carbon footprint 🌞."
    elif "hello" in text or "hi" in text:
        reply = f"🌿 Hey {st.session_state.username}! How are you today? Want to learn a new eco tip? 🍀"
    elif "fact" in text:
        eco_facts = [
            "🌍 Recycling one glass bottle saves enough energy to power a computer for 30 minutes!",
            "🍃 One recycled tin can saves enough energy to power a TV for 3 hours!",
            "🌳 Every ton of recycled paper saves 7,000 gallons of water 💧!",
        ]
        reply = random.choice(eco_facts)
    else:
        reply = "🌾 I may not know that yet, but I'm learning! Try asking about composting, recycling, or energy-saving tips 🌱."

    st.session_state.messages.append(("ai", reply))
    st.rerun()

# ---------- SAVE CHAT ----------
if st.button("💾 Download Chat History"):
    chat_text = "\n".join(
        [f"[{datetime.now().strftime('%H:%M')}] {role.upper()}: {msg}" for role, msg in st.session_state.messages]
    )
    st.download_button(
        label="⬇️ Save Chat as Text",
        data=chat_text,
        file_name=f"GreenifyAI_Chat_{st.session_state.username}.txt",
        mime="text/plain"
    )
