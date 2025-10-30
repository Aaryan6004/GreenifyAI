import streamlit as st
import time
import random
import re

# 🌱 Page setup
st.set_page_config(page_title="🌿 GreenifyAI", layout="centered")

# 🌳 Ultra-Realistic Nature Background + Styling
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://images.unsplash.com/photo-1502082553048-f009c37129b9?auto=format&fit=crop&w=1950&q=80');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    [data-testid="stHeader"], [data-testid="stToolbar"] {
        background: rgba(0,0,0,0);
    }

    .main {
        background: rgba(0, 0, 0, 0.55);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(6px);
    }

    /* Chat bubbles */
    .chat-bubble {
        padding: 12px 16px;
        border-radius: 18px;
        margin: 8px 0;
        max-width: 80%;
        word-wrap: break-word;
        animation: fadeIn 0.6s ease;
        font-family: 'Poppins', sans-serif;
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

    /* Fade-in animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Thinking animation */
    .thinking {
        font-style: italic;
        color: #e0e0e0;
        animation: blink 1.4s infinite;
    }

    @keyframes blink {
        0%, 100% { opacity: 0.4; }
        50% { opacity: 1; }
    }

    /* Floating leaves */
    .leaf {
        position: absolute;
        width: 22px;
        height: 22px;
        background: url('https://cdn-icons-png.flaticon.com/512/765/765441.png');
        background-size: contain;
        opacity: 0.5;
        animation: float 12s infinite linear;
    }

    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        100% { transform: translateY(-900px) rotate(360deg); }
    }

    /* Login card */
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

# 🌺 Floating leaves animation
for i in range(6):
    st.markdown(f"<div class='leaf' style='left:{i*15+6}%; animation-delay:{i*1.6}s;'></div>", unsafe_allow_html=True)

# -----------------------
# Utility: Response Generator
# -----------------------
def generate_response(user_text: str, username: str) -> str:
    t = user_text.lower().strip()

    # greetings
    if re.search(r"\b(hi|hello|hey|hiya|good morning|good afternoon|good evening)\b", t):
        return f"🌿 Hey {username}! Hello — how can I help you with recycling or our comic today?"

    # thanks
    if re.search(r"\b(thank|thanks|thx|thank you)\b", t):
        return f"🙂 You're welcome, {username}! Glad to help. Want another tip or a DIY idea?"

    # ask about the comic / project
    if re.search(r"\b(comic|book|recycle squad|our comic|project|prototype)\b", t):
        return ("📚 Our DIY comic 'The Recycle Squad' teaches recycling and solid waste management to teens. "
                "It was made from cardboard and recyclable materials, includes a vegetable-dye pen and a free recyclable bookmark — perfect for fun eco-lessons!")

    # materials & how it's made
    if re.search(r"\b(material|cardboard|vegetable dye|bookmark|pen|how (you|we) made|how to make)\b", t):
        return ("🛠️ Materials & making: We used recycled cardboard, glue, and plant-based (vegetable) dyes for color. "
                "Bookmarks were cut from leftover cardboard and decorated with natural pigments. For a pen, we used a recycled body and natural ink made from beet/carrot tea + binder.")

    # recycling basics
    if re.search(r"\b(recycle|recycling|how to recycle|what is recycling)\b", t):
        return ("♻️ Recycling basics: Rinse and dry recyclable containers, separate dry (paper, plastic, metal, glass) from wet waste, check local rules for sorting, and drop items at a recycling center or curbside collection.")

    # plastic-specific
    if "plastic" in t:
        if re.search(r"\b(bottle|how to recycle.*plastic|single-use|plastic bag|plastic wrap)\b", t):
            return ("🧴 Plastic tips: Remove caps, rinse bottles, squash to save space, and keep plastics dry. Avoid single-use plastics — switch to reusable bottles and cloth bags.")
        return ("🧴 Plastic note: Clean plastics that have recycling symbols and follow your local facility's sorting rules. Reduce use where possible.")

    # composting
    if "compost" in t or "composting" in t:
        return ("🌱 Composting steps: 1) Collect kitchen scraps (vegetable peels, fruit scraps, eggshells) and yard waste. "
                "2) Keep a balance of 'greens' and 'browns' (greens = food scraps, browns = dry leaves/paper). 3) Turn occasionally and keep moist — in weeks you'll have compost.")

    # paper
    if "paper" in t:
        return ("📄 Paper recycling: Remove tape/staples if possible, flatten cardboard boxes, reuse scrap paper for notes, and recycle clean paper, newspapers, and cardboard.")

    # metal
    if "metal" in t or "can" in t:
        return ("🥫 Metal recycling: Rinse cans, keep labels on (OK usually), and place in the metal recycling stream. Aluminum and steel are infinitely recyclable — great to reuse!")

    # glass
    if "glass" in t:
        return ("🍾 Glass tip: Rinse jars and bottles, remove lids (recycle lids separately if required), and don't mix broken glass with regular glass recycling in some areas — check local guidance.")

    # hazardous / battery / e-waste
    if re.search(r"\b(battery|e-?waste|electronic|bulb|light bulb|chemicals)\b", t):
        return ("⚠️ Hazardous waste: Batteries, electronics, and chemicals must go to special drop-off points — do NOT put them in regular trash or recycling. Check your local e-waste collection days.")

    # disposal of food waste
    if re.search(r"\b(food waste|kitchen waste|leftovers)\b", t):
        return ("🍽️ Food waste: Compost food scraps if possible. For non-compostable kitchen waste, use municipal organic waste services. Avoid pouring oil down drains — recycle cooking oil through collection centers if available.")

    # step-by-step instructions for DIY bookmark/pen (helpful)
    if re.search(r"\b(make.*bookmark|how to make bookmark|make bookmark)\b", t):
        return ("✂️ DIY Recyclable Bookmark: Cut a rectangle from cardboard, sand edges, decorate with vegetable dye or markers, and laminate with a thin strip of clear recycled plastic if you want it durable. Add a hole and string from leftover yarn if desired.")
    if re.search(r"\b(make.*pen|how to make pen|vegetable dye pen|make pen)\b", t):
        return ("🖊️ Simple veggie-ink pen: Steep beet/carrot peel in hot water for color, reduce to a concentrated dye. Use a felt-tip refill or dip-pen nib and coat with a small amount of binder (gum arabic solution) to help ink flow. Use a recycled pen body for the casing.")

    # solid waste management definition
    if re.search(r"\b(solid waste management|what is solid waste management|swm)\b", t):
        return ("🏙️ Solid waste management includes collecting, sorting, recycling, composting, and safe disposal of waste. Effective SWM reduces pollution, protects health, and recovers resources.")

    # tips request
    if re.search(r"\b(tip|tips|advice|how can i|how to reduce|ways to reduce)\b", t):
        return ("💡 Quick tips: 1) Carry a reusable bottle & bag. 2) Separate wet/dry waste. 3) Compost food scraps. 4) Buy products with less packaging. 5) Repair instead of replace.")

    # facts
    if "fact" in t or "did you know" in t:
        facts = [
            "🌍 Fun fact: Recycling one aluminum can saves enough energy to power a TV for about 3 hours!",
            "🌱 Compost fact: Food waste in landfills produces methane, a powerful greenhouse gas — composting prevents this.",
            "♻️ Glass fact: Glass can be recycled forever without losing quality."
        ]
        return random.choice(facts)

    # authors / team info
    if re.search(r"\b(author|team|who made|who are|recycle squad|members)\b", t):
        return ("👥 Team: The Recycle Squad — Aaryan (Counterpart Writer), Riya (Illustrator), Karan (Material Collector), Meera (Designer), Tanish (Researcher). We built the comic from recycled materials and vegetable dyes.")

    # location or where to recycle
    if re.search(r"\b(where.*recycle|where can i recycle|recycling center|drop off)\b", t):
        return ("📍 Where to recycle: Check your local municipality website for collection points and recycling centers. Many cities have curbside pickup for sorted recyclables; others have drop-off hubs for electronics and hazardous waste.")

    # if user asks "how to start"
    if re.search(r"\b(how do i start|how to start|where to begin|i want to start)\b", t):
        return ("🌱 Start small: Begin by separating dry/wet at home, carry a reusable bottle, and pick one item to reduce (like single-use plastic). Build habits week by week.")

    # fallback: try to answer with general guidance, personalized
    if len(t) > 0:
        # provide a useful, specific-sounding fallback
        return (f"🌿 Good question, {username}! Here's a practical tip: try separating wet and dry waste right now — put all food scraps in one container (for compost) "
                "and keep bottles/paper separate to be rinsed and recycled. Ask me about a specific item (like 'how to recycle a plastic bottle' or 'how to compost banana peels').")

    # default
    return f"🌿 Hi {username}! I can answer questions about recycling, composting, materials we used in the comic, and DIY eco projects."

# -----------------------
# UI: Name Entry + Chat
# -----------------------
# Name Entry System
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
            st.session_state.messages = [
                ("ai", f"🌍 Hello {st.session_state.username}! Welcome to GreenifyAI 🌿 I'm here to share eco-friendly habits, recycling tips, and sustainability ideas with you ♻️")
            ]
            st.rerun()
        st.stop()

# header
st.markdown("<h1 style='text-align:center; color:white;'>🌍 GreenifyAI</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#f0f0f0;'>Chatting with {st.session_state.username} 🍃</p>", unsafe_allow_html=True)

# show existing messages
if "messages" not in st.session_state:
    st.session_state.messages = [("ai", f"🌍 Hello {st.session_state.username}! Welcome to GreenifyAI 🌿 I'm here to share eco-friendly habits, recycling tips, and sustainability ideas with you ♻️")]

for msg in st.session_state.messages:
    role, text = msg
    bubble_class = "user" if role == "user" else "ai"
    st.markdown(f"<div class='chat-bubble {bubble_class}'>{text}</div>", unsafe_allow_html=True)

# chat input
user_input = st.chat_input("Ask GreenifyAI about recycling or eco habits 🌿")

if user_input:
    # append user message
    st.session_state.messages.append(("user", user_input))

    # thinking animation + small dynamic delay
    with st.spinner("🌱 Thinking..."):
        # small variable delay to feel natural
        delay = 1.5 + min(len(user_input) / 50.0, 2.0)
        time.sleep(delay)

    # generate direct, tailored response
    reply = generate_response(user_input, st.session_state.username)

    # append and rerun (to show the new chat bubble)
    st.session_state.messages.append(("ai", reply))
    st.rerun()
