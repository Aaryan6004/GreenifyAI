import streamlit as st
import time
from random import choice

# 🌿 GreenifyAI 3.0 — Dynamic Chatbot with gradient bubbles + Thinking animation + mock Google login

st.set_page_config(page_title="🌿 GreenifyAI", page_icon="♻️", layout="centered")

# --- Custom Styling ---
st.markdown(
    """
    <style>
        [data-testid="stAppViewContainer"] {
            background-image: url('https://images.unsplash.com/photo-1502082553048-f009c37129b9?auto=format&fit=crop&w=1950&q=80');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        [data-testid="stHeader"] {
            background: rgba(0, 0, 0, 0);
        }

        .main {
            background: rgba(255, 255, 255, 0.35);
            backdrop-filter: blur(12px);
            border-radius: 25px;
            padding: 25px;
        }

        .chat-bubble {
            padding: 12px 18px;
            border-radius: 20px;
            margin: 8px 0;
            width: fit-content;
            max-width: 80%;
            word-wrap: break-word;
            font-family: 'Comic Sans MS', sans-serif;
            color: white;
        }

        .user-bubble {
            background: linear-gradient(135deg, #555, #777);
            margin-left: auto;
        }

        .bot-bubble {
            background: linear-gradient(135deg, #666, #999);
            border: 1px solid rgba(255,255,255,0.2);
        }

        .header {
            text-align: center;
            color: white;
            font-size: 36px;
            font-weight: bold;
            text-shadow: 2px 2px 5px #003300;
            margin-bottom: 5px;
        }

        .subheader {
            text-align: center;
            color: #e8ffe8;
            font-size: 18px;
            text-shadow: 1px 1px 3px #003300;
        }

        .login-box {
            background: rgba(255,255,255,0.3);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            color: white;
        }

        button[kind="primary"] {
            background: linear-gradient(135deg, #3c763d, #6fb76f);
            color: white !important;
            border-radius: 10px !important;
            border: none !important;
        }

    </style>
    """,
    unsafe_allow_html=True
)

# --- Title and Subtitle ---
st.markdown("<h1 class='header'>🌿 GreenifyAI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Your Eco-Friendly Chatbot — Learn, Recycle, and Greenify the Future 🌍</p>", unsafe_allow_html=True)
st.write("")

# --- Mock Google Login System ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("<div class='login-box'><h3>🔐 Sign in to GreenifyAI</h3></div>", unsafe_allow_html=True)
    google_name = st.text_input("Enter your Google Name (mock login)")
    if st.button("Login with Google 🌐"):
        if google_name.strip() != "":
            st.session_state.logged_in = True
            st.session_state.username = google_name.strip()
            st.success(f"Welcome, {google_name}! 🌿")
            time.sleep(1)
            st.rerun()
        else:
            st.warning("Please enter your Google name to continue.")
    st.stop()

# --- Initialize Chat ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "content": f"Hello {st.session_state.username} 🌱! I'm GreenifyAI — your eco-friendly companion. Ask me anything about recycling, composting, or sustainability!"}
    ]

# --- Display Messages ---
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble user-bubble'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble bot-bubble'>{msg['content']}</div>", unsafe_allow_html=True)

# --- User Input ---
user_input = st.chat_input("Ask me about recycling or waste management...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("🌿 GreenifyAI is thinking..."):
        thinking_phrases = ["Thinking...", "Processing your question...", "Recycling some thoughts...", "Analyzing eco-data..."]
        thinking_msg = st.empty()
        for i in range(3):
            thinking_msg.text(choice(thinking_phrases))
            time.sleep(0.8)
        thinking_msg.empty()

    user_text = user_input.lower()
    response = ""

    # --- Eco Response Logic ---
    if "plastic" in user_text:
        response = "Plastic takes centuries to decompose 🌎. Always reuse or recycle clean plastic containers and avoid single-use plastics!"
    elif "recycle" in user_text or "recycling" in user_text:
        response = "Recycling gives waste a new life ♻️. Separate dry and wet waste at home before sending it out!"
    elif "compost" in user_text:
        response = "Composting is nature’s own recycling system 🌱. Keep food scraps and leaves in a compost bin to make rich soil."
    elif "metal" in user_text:
        response = "Metals like aluminum and steel are endlessly recyclable 🔁. Rinse and sort them before sending to your recycling center."
    elif "paper" in user_text:
        response = "Paper can be recycled 5-7 times! 📘 Reduce printing, reuse scraps, and recycle properly."
    elif "waste" in user_text or "garbage" in user_text:
        response = "Proper waste management means reducing, reusing, and recycling 🪴. Sort biodegradable and non-biodegradable waste separately."
    elif "comic" in user_text or "book" in user_text:
        response = "Our eco-comic was made using recycled cardboard and vegetable dyes 🌿 — it’s storytelling that helps save the planet!"
    elif "fact" in user_text:
        response = choice([
            "🌍 Fun Fact: Recycling one aluminum can saves enough energy to power a TV for 3 hours!",
            "♻️ Fact: Glass can be recycled endlessly without losing quality.",
            "🌱 Fact: Composting food waste can reduce landfill garbage by up to 30%!"
        ])
    else:
        response = "I'm growing my eco-knowledge 🌳! Try asking about recycling, composting, paper, metal, or our eco-comic!"

    st.session_state.messages.append({"role": "bot", "content": response})
    st.rerun()
