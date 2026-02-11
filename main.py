import streamlit as st
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Plus Ultra Logic System", page_icon="🚀", layout="centered")

# --- BLENDED & FADED UI DESIGN ---
st.markdown("""
    <style>
    /* 1. The Background Image */
    .stApp {
        background-image: url(" https://images6.alphacoders.com/997/thumb-1920-997829.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* 2. The Blending Layer (Faded Scrim) */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(15, 23, 42, 0.85); /* Dark blue/black fade */
        backdrop-filter: blur(8px); /* This blurs the background slightly */
        z-index: -1;
    }

    /* 3. The Logic Card (Makes options visible) */
    .stMarkdown, .stRadio, .stTextInput, .stAlert {
        background: rgba(255, 255, 255, 0.07) !important;
        backdrop-filter: blur(10px);
        padding: 25px !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        margin-bottom: 20px !important;
    }

    /* 4. Text & Radio Button Clarity */
    h1, h2, h3, p, span, label {
        color: #f1faee !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    
    /* Ensuring Radio button text is bright */
    .stWidget label p {
        font-size: 1.1rem !important;
        font-weight: 500 !important;
    }

    /* Hero Red Button */
    div.stButton > button {
        background-color: #e63946 !important;
        color: white !important;
        height: 3em;
        width: 100%;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        box-shadow: 0px 4px 15px rgba(230, 57, 70, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🚀 Plus Ultra Logic System")
st.markdown("### *'Your dreams are yours. They are built on belief and not pressure.Go Beyond! Plus Ultra!'*")
st.write("---")

# --- INITIALIZE SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# --- MODULES ---
modules = [
    {
        "type": "Verbal Logic",
        "question": "SPOKE : WHEEL :: STEP : ?",
        "options": ["Walk", "Staircase", "Shoe", "Run"],
        "keywords": ["part", "whole", "staircase"],
        "solution": "STAIRCASE. Bridge: 'Part-to-Whole'."
    },
    {
        "type": "Figural Logic",
        "question": "Triangle flips Bottom to Top. Circle 'D' on Right moves to...?",
        "options": ["Stay Right", "Move to Left side", "Become a square"],
        "keywords": ["left", "mirror", "flip"],
        "solution": "MOVE TO LEFT SIDE. Bridge: 'Reflection'."
    }
    {
        "type": "Numeric Logic",
        "question": "2, 6, 18, 54, ?",
        "options": ["108", "162", "200"],
        "keywords": ["multiply", "times", "x3", "3"],
        "solution": "162. Bridge: 'Multiplication'. Each number is multiplied by 3."
    },
    {
        "type": "Matrix Logic",
        "question": "Row 1: Circle -> Circle + Square. Row 2: Triangle -> ?",
        "options": ["Triangle + Square", "Just a Square", "Small Triangle"],
        "keywords": ["inside", "fill", "square", "triangle", "add"],
        "solution": "TRIANGLE + SQUARE. Bridge: 'Addition'. The rule is to add a square inside the primary shape."
    }
]

# --- INTERFACE ---
if st.session_state.step < len(modules):
    current = modules[st.session_state.step]
    
    # Progress Display
    st.write(f"🏷️ **Question {st.session_state.step + 1} of {len(modules)}**")
    
    with st.container():
        st.info(f"⚡ **QUIRK ANALYSIS:** {current['type']}")
        st.write(f"### {current['question']}")
        
        choice = st.radio("Select your answer:", current['options'], key=f"r_{st.session_state.step}")
        thought = st.text_input("Describe your 'Logic Lens' (The Bridge):", key=f"t_{st.session_state.step}", placeholder="How are these related?")

        if st.button("GO BEYOND!"):
            if thought:
                st.session_state.logs.append({"type": current['type'], "choice": choice, "reasoning": thought})
                st.session_state.step += 1
                st.rerun()
            else:
                st.warning("Logic is the hero's greatest weapon. Please explain yours!")

else:
    st.balloons()
    st.success("🏁 MISSION COMPLETE!")
    for log in st.session_state.logs:
        with st.expander(f"🔍 {log['type']} Result"):
            st.write(f"**Your Logic:** {log['reasoning']}")
    if st.button("Restart"):
        st.session_state.step = 0
        st.session_state.logs = []
        st.rerun()