import streamlit as st
import random
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="🌿 GreenifyAI", page_icon="🌱", layout="wide")

# --- CSS STYLING ---
st.markdown("""
<style>
body {
    background: url('https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1950&q=80');
    background-size: cover;
    background-attachment: fixed;
    color: white;
    font-family: 'Poppins', sans-serif;
}

.chat-container {
    backdrop-filter: blur(8px);
    background: rgba(20, 20, 20, 0.6);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.6);
}

.user-msg {
    background: linear-gradient(135deg, #3a3a3a, #6e6e6e);
    color: white;
    padding: 12px 18px;
    border-radius: 18px;
    margin-bottom: 10px;
    animation: slideInRight 0.5s ease;
    width: fit-content;
    max-width: 70%;
    margin-left: auto;
}

.bot-msg {
    background: linear-gradient(135deg, #00b894, #55efc4);
    color: white;
    padding: 12px 18px;
    border-radius: 18px;
    margin-bottom: 10px;
    animation: slideInLeft 0.5s ease;
    width: fit-content;
    max-width: 70%;
    margin-right: auto;
}

@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-30px); }
    to { opacity: 1; transform: translateX(0); }
}

@keyframes slideInRight {
    from { opacity: 0; transform: translateX(30px); }
    to { opacity: 1; transform: translateX(0); }
}

@keyframes fadeIn {
    from { opacity: 0; transform: scale(0.95); }
    to { opacity: 1; transform: scale(1); }
}

h1 {
    text-align: center;
    color: #d4ffea;
    font-size: 3em;
    text-shadow: 0 0 15px #00ff99;
}
</style>
""", unsafe_allow_html=True)

# --- APP TITLE ---
st.markdown("<h1>🌿 GreenifyAI</h1>", unsafe_allow_html=True)

# --- USER LOGIN MOCK ---
if "username" not in st.session_state:
    with st.form("user_login"):
        username = st.text_input("🌱 Enter your name to begin:")
        submitted = st.form_submit_button("Enter the Green Zone 💚")
        if submitted and username.strip() != "":
            st.session_state.username = username.strip()
            st.session_state.chat_history = []
            st.experimental_rerun()

else:
    st.markdown(f"### 🌍 Welcome, **{st.session_state.username}**! Let's make the planet greener together 💫")

    # --- Initialize Chat ---
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Ask GreenifyAI about recycling, waste management, or the comic 🌱...")

    if user_input:
        st.session_state.chat_history.append({"user": user_input})

        # Simulate "thinking" animation
        with st.chat_message("assistant"):
            with st.spinner("🤔 Thinking..."):
                time.sleep(random.uniform(1, 2))
        
        # --- Generate Response ---
        eco_responses = [
            "♻️ That’s a great question! Always remember to **segregate waste** — dry and wet bins help a lot!",
            "🌍 Try **reusing plastic bottles** as planters! It’s fun, creative, and eco-friendly!",
            "🍃 Composting is a simple way to recycle food waste and enrich soil naturally.",
            "🌱 You can turn old cardboard into **DIY notebooks or comics**, just like your team did!",
            "💡 The 3Rs — **Reduce, Reuse, Recycle** — are the superheroes of sustainability!"
        ]

        response = random.choice(eco_responses)
        st.session_state.chat_history.append({"bot": response})

    # --- Display Chat History ---
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        if "user" in chat:
            st.markdown(f'<div class="user-msg">🧍‍♂️ {chat["user"]}</div>', unsafe_allow_html=True)
        if "bot" in chat:
            st.markdown(f'<div class="bot-msg">🌿 {chat["bot"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

