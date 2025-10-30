import streamlit as st
import time
import random
import re

# 🌱 Page setup
st.set_page_config(page_title="🌿 GreenifyAI", layout="centered")

# 🌳 Ultra-Realistic Nature Background + Dynamic Glass UI (unchanged style)
st.markdown("""
    <style>
    /* Background */
    [data-testid="stAppViewContainer"] {
        background-image: url('https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=1950&q=80');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        overflow: hidden;
        animation: bgZoom 40s ease-in-out infinite alternate;
    }
    @keyframes bgZoom { from { background-size: 100%; } to { background-size: 110%; } }
    [data-testid="stHeader"], [data-testid="stToolbar"] { background: rgba(0,0,0,0); }

    /* Title glow */
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

    /* Main container */
    .main {
        background: rgba(0, 0, 0, 0.55);
        border-radius: 24px;
        padding: 32px;
        backdrop-filter: blur(8px);
        box-shadow: 0 0 25px rgba(0,255,140,0.15);
        animation: fadeIn 1s ease;
    }

    /* Chat bubble */
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
    .chat-bubble:hover { transform: scale(1.02); }

    .user { background: linear-gradient(145deg, #3b3b3b, #1c1c1c); color: white; align-self: flex-end; border: 1px solid #666; box-shadow: 0 0 15px rgba(200,255,200,0.1); }
    .ai   { background: linear-gradient(145deg, #00b36b, #005533); color: #eaffea; border: 1px solid #44ff99; box-shadow: 0 0 18px rgba(0,255,140,0.3); }

    @keyframes fadeUp { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }

    /* Typing indicator */
    .typing { color: #c6ffd0; font-style: italic; animation: blink 1.2s infinite; }
    @keyframes blink { 50% { opacity: 0.4; } }

    /* Login card */
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
        box-shadow: 0 0 30px rgba(0,255,140,0.2);
        animation: fadeIn 1.2s ease;
    }

    @keyframes fadeIn { from { opacity: 0; transform: scale(0.95); } to { opacity: 1; transform: scale(1); } }

    input { border-radius: 10px; border: none; padding: 10px; width: 80%; text-align: center; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

# -----------------------
# Dynamic Response Engine (simulates 3000+ variations)
# -----------------------

# Core intent categories and keyword triggers (extendable)
INTENTS = {
    "greeting": ["hi", "hello", "hey", "hiya", "good morning", "good afternoon", "good evening"],
    "thanks": ["thanks", "thank you", "thx", "ty"],
    "comic": ["comic", "book", "recycle squad", "our comic", "project", "prototype"],
    "materials": ["material", "cardboard", "vegetable dye", "bookmark", "pen", "how made", "how to make"],
    "recycle": ["recycle", "recycling", "how to recycle", "what is recycling"],
    "plastic": ["plastic", "bottle", "single-use", "plastic bag"],
    "compost": ["compost", "composting"],
    "paper": ["paper", "cardboard", "notebook"],
    "metal": ["metal", "can", "aluminum", "steel"],
    "glass": ["glass", "bottle", "jar"],
    "hazard": ["battery", "e-waste", "electronic", "bulb", "chemicals"],
    "food": ["food waste", "kitchen waste", "leftovers"],
    "tips": ["tip", "tips", "advice", "how to reduce", "ways to reduce"],
    "facts": ["fact", "did you know"],
    "authors": ["author", "team", "who made", "members", "recycle squad"]
}

# A set of core templates per intent (kept concise; combinatorials produce many unique outputs)
TEMPLATES = {
    "greeting": [
        "🌿 Hey {user}! Great to see you — how can I help on your eco journey today?",
        "Hi {user}! 👋 I’m GreenifyAI — ready with tips about recycling, composting, or our comic."
    ],
    "thanks": [
        "🙂 You’re welcome, {user}! Happy to help — want another tip?",
        "Glad to help, {user}! 🌱 Tell me if you want DIY steps or quick tips."
    ],
    "comic": [
        "📚 Our DIY comic 'The Recycle Squad' teaches recycling and waste management through fun, action-packed stories — made from cardboard and veggie dyes!",
        "The Recycle Squad comic is a prototype storytelling tool: recycled materials, vegetable-dye pens, and an eco message for teens."
    ],
    "materials": [
        "🛠️ We used recycled cardboard, glue, and vegetable dyes. Bookmarks made from leftover cardboard and colored with plant pigments.",
        "Materials included cardboard, eco-friendly ink (vegetable based), and reused scraps — all kept low-waste."
    ],
    "recycle": [
        "♻️ Recycling essentials: rinse, sort (dry vs wet), and follow local sorting rules — then drop at collection points or curbside.",
        "To recycle well: separate materials, keep them clean and dry, and consult local guidelines for special items."
    ],
    "plastic": [
        "🧴 Plastic tips: avoid single-use, rinse bottles, remove caps if your recycler asks, and reuse when possible.",
        "For plastic: reuse, clean before recycling, and prefer alternatives (glass, metal, cloth) whenever you can."
    ],
    "compost": [
        "🌱 Composting steps: collect kitchen scraps, balance greens and browns, keep it moist and aerated — in weeks you’ll have compost!",
        "Composting turns food and yard waste into rich soil. Use a bin or pile, add brown leaves, and turn occasionally."
    ],
    "paper": [
        "📄 Paper: reuse scraps, flatten boxes, remove tape, and recycle clean paper with local services.",
        "Paper can be recycled several times — save it, reuse as notes, and recycle when it's ready."
    ],
    "metal": [
        "🥫 Metal (cans): rinse, squish if allowed, and recycle — aluminum and steel are highly recyclable.",
        "Metals are endlessly recyclable — rinse and put them in your metal recycling stream."
    ],
    "glass": [
        "🍾 Glass jars/bottles: rinse, remove lids (recycle separately if asked), and recycle in glass bins.",
        "Glass can be recycled without losing quality — keep it clean and sorted."
    ],
    "hazard": [
        "⚠️ Hazardous waste (batteries, electronics): take them to special drop-off centers — never in normal trash.",
        "E-waste must be handled by designated collection centers. Check municipal schedules for safe disposal."
    ],
    "food": [
        "🍽️ Food waste: compost it if possible. For non-compostable scraps, follow municipal organic-waste rules.",
        "Avoid throwing food in regular trash when you can compost or use food-waste collection."
    ],
    "tips": [
        "💡 Quick tips: carry a reusable bottle, avoid disposable cutlery, separate wet/dry waste, and repair before replacing.",
        "Small steps: say no to single-use plastics, buy less packaged goods, and compost scraps."
    ],
    "facts": [
        "🌍 Fun fact: Recycling one aluminum can save enough energy to power a TV for ~3 hours!",
        "🌱 Did you know? Composting prevents methane emissions from landfills."
    ],
    "authors": [
        "👥 The Recycle Squad: Aaryan (Counterpart Writer), Riya (Illustrator), Karan (Material Collector), Meera (Designer), Tanish (Researcher).",
        "Team behind the comic: Aaryan, Riya, Karan, Meera, and Tanish — they made the comic from recyclable materials."
    ]
}

# Tone modifiers — these change phrasing and emoji usage
TONES = [
    {"name": "friendly", "prefix": "", "suffixes": [" 😊", " 🌿", ""]},
    {"name": "playful", "prefix": "Heck yes! ", "suffixes": [" 😄", " ✨", ""]},
    {"name": "informative", "prefix": "", "suffixes": [" 📘", " 🔎", ""]},
    {"name": "inspiring", "prefix": "Imagine this: ", "suffixes": [" 🌎", " 🌱", ""]},
    {"name": "brief", "prefix": "", "suffixes": [" ✅", ""]}
]

# Extra detail fragments (can be appended randomly)
DETAILS = [
    "You can also try local swap groups.",
    "Many cities run free recycling workshops.",
    "Label bins at home to help family members sort.",
    "Try DIY upcycling — it's creative and useful!",
    "Small habits compound into big change."
]

# Variation helpers to produce many combinations
def compose_response(core_template: str, username: str) -> str:
    """Compose final answer by applying tone, detail, and suffix variations."""
    tone = random.choice(TONES)
    detail_chance = random.random()
    # Build base
    resp = core_template.format(user=username)
    # optionally prefix
    if tone["prefix"]:
        resp = tone["prefix"] + resp[0].lower() + resp[1:] if resp else tone["prefix"] + resp
    # optionally add a detail fragment
    if detail_chance < 0.35:
        resp = resp + " " + random.choice(DETAILS)
    # add tone suffix
    suffix = random.choice(tone["suffixes"])
    resp = resp + suffix
    # small punctuation/phrase tweaks
    if random.random() < 0.12:
        resp = resp.replace("!", ".").replace("  ", " ")
    if random.random() < 0.08:
        resp = resp + " — " + random.choice(["Keep going!", "Small steps!", "You got this!"])
    return resp

# Master generate function: selects intent, template, composes.
def generate_dynamic_response(user_text: str, username: str) -> str:
    t = user_text.lower()
    # detect intent by keywords
    matched_intent = None
    for intent, keys in INTENTS.items():
        for k in keys:
            if k in t:
                matched_intent = intent
                break
        if matched_intent:
            break
    # fallback mapping: if none matched, choose from general tips or fallback templates
    if not matched_intent:
        # check more specific words
        if re.search(r"how to make|make.*bookmark|make bookmark|how to make pen", t):
            matched_intent = "materials"
        else:
            matched_intent = "tips"

    # choose a core template for that intent
    templates = TEMPLATES.get(matched_intent, TEMPLATES["tips"])
    core = random.choice(templates)

    # compose with tone and details — many combinations possible
    reply = compose_response(core, username)

    # further tweak based on question complexity: if question seems long, add detail
    if len(user_text.split()) > 8 and random.random() < 0.6:
        extra = random.choice(DETAILS)
        reply = reply + " " + extra

    # Occasionally offer follow-up suggestion
    if random.random() < 0.25:
        follow = random.choice([
            "Would you like step-by-step instructions?",
            "Want a DIY step list for this?",
            "I can give a 3-step plan if you want."
        ])
        reply = reply + " " + follow

    return reply

# -----------------------
# UI: Name Entry + Chat
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
            # seed initial message
            st.session_state.messages = [
                ("ai", f"🌍 Hello {st.session_state.username}! Welcome to GreenifyAI 🌿 I'm here to share eco-friendly habits, recycling tips, and sustainability ideas with you ♻️")
            ]
            st.rerun()
        st.stop()

# header
st.markdown("<h1>🌿 GreenifyAI</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#e0ffe5;'>Chatting with {st.session_state.username} 🌳</p>", unsafe_allow_html=True)

# ensure messages exist
if "messages" not in st.session_state:
    st.session_state.messages = [("ai", f"🌍 Hello {st.session_state.username}! Welcome to GreenifyAI 🌿 I'm here to share eco-friendly habits, recycling tips, and sustainability ideas with you ♻️")]

# render chat messages
for role, text in st.session_state.messages:
    cls = "user" if role == "user" else "ai"
    st.markdown(f"<div class='chat-bubble {cls}'>{text}</div>", unsafe_allow_html=True)

# input box
user_input = st.chat_input("Ask GreenifyAI about recycling, composting, making the comic, or eco tips 🌱")

if user_input:
    st.session_state.messages.append(("user", user_input))
    # thinking
    with st.spinner("🌱 GreenifyAI is thinking..."):
        # a tiny dynamic delay based on length
        delay = 1.2 + min(len(user_input) / 60.0, 2.0) + random.uniform(0, 0.6)
        time.sleep(delay)
    # generate dynamic reply (simulates thousands of unique outputs)
    reply = generate_dynamic_response(user_input, st.session_state.username)
    st.session_state.messages.append(("ai", reply))
    st.rerun()
