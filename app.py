import streamlit as st

# 🌿 GreenifyAI - Nature Chatbot 2.5
# Realistic nature background + ChatGPT-style conversation

st.set_page_config(page_title="🌿 GreenifyAI", page_icon="♻️", layout="centered")

# --- Realistic Background ---
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

        [data-testid="stToolbar"] {
            right: 2rem;
        }

        .main {
            background: rgba(255, 255, 255, 0.4);
            backdrop-filter: blur(12px);
            border-radius: 20px;
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
        }

        .user-bubble {
            background-color: rgba(150, 255, 150, 0.85);
            margin-left: auto;
            color: #003300;
        }

        .bot-bubble {
            background-color: rgba(240, 255, 240, 0.85);
            color: #1a4d1a;
            border: 1px solid #b3e6b3;
        }

        .header {
            text-align: center;
            color: white;
            font-size: 36px;
            font-weight: bold;
            text-shadow: 2px 2px 5px #004400;
            margin-bottom: 5px;
        }

        .subheader {
            text-align: center;
            color: #e8ffe8;
            font-size: 18px;
            text-shadow: 1px 1px 3px #003300;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header ---
st.markdown("<h1 class='header'>🌿 GreenifyAI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Your Eco-Friendly Chat Assistant — here to talk about recycling, nature, and sustainable living ♻️</p>", unsafe_allow_html=True)
st.write("")

# --- Initialize chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "content": "Hi there 🌱! I'm GreenifyAI — your friendly chatbot that teaches about recycling, composting, and eco habits. How can I help you today?"}
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
        response = "Plastic pollution is a huge issue 🌎. Try to reuse bottles, avoid single-use plastics, and recycle clean containers properly."
    elif "recycle" in user_text or "recycling" in user_text:
        response = "Recycling is turning waste into something reusable ♻️. Always sort dry and wet waste before disposal!"
    elif "compost" in user_text:
        response = "Composting is nature’s recycling 🌱! Collect food scraps and leaves — let them decompose into natural fertilizer."
    elif "metal" in user_text:
        response = "Metals like aluminum can be melted down infinitely 🔁. Rinse and sort them before sending to recycling centers."
    elif "paper" in user_text:
        response = "Paper can be reused or recycled 📘. Save trees by minimizing waste and reusing sheets!"
    elif "waste" in user_text or "garbage" in user_text:
        response = "Proper waste management means reduce, reuse, and recycle 🪴. Sort biodegradable and non-biodegradable items separately."
    elif "comic" in user_text or "book" in user_text:
        response = "Our eco-comic teaches sustainability with recycled cardboard and plant-based inks 🌿📚."
    elif "hi" in user_text or "hello" in user_text:
        response = "Hey there 🌿! I'm GreenifyAI, your eco friend. Want to learn a recycling fact today?"
    elif "fact" in user_text:
        response = "🌍 Fun Fact: Recycling one aluminum can saves enough energy to power a TV for 3 hours!"
    else:
        response = "I'm still growing 🌳 — but I can share eco-friendly tips, recycling advice, and sustainability facts!"

    st.session_state.messages.append({"role": "bot", "content": response})
    st.rerun()
