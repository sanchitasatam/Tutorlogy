import streamlit as st
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Plus Ultra Logic System", page_icon="🚀", layout="centered")

# --- CUSTOM CSS: MHA BACKGROUND CLASH ---
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://wallpaperaccess.com/full/1126131.jpg");
        background-size: cover;
        background-attachment: fixed;
    }

    /* Dark Overlay to make text readable */
    .stApp::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.7); /* Darkens the image */
        z-index: -1;
    }
    
    /* Hero Red Buttons */
    div.stButton > button {
        background-color: #e63946 !important;
        color: white !important;
        font-weight: bold !important;
        border: 2px solid #f1faee !important;
        border-radius: 8px !important;
        box-shadow: 0px 0px 15px rgba(230, 57, 70, 0.5) !important;
    }

    /* White text for visibility */
    h1, h2, h3, p, span, label {
        color: #f1faee !important;
        text-shadow: 1px 1px 2px #000000;
    }

    /* Transparent Content Box */
    .stMarkdown, .stRadio, .stTextInput {
        background: rgba(0, 0, 0, 0.4);
        padding: 15px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🚀 Plus Ultra Logic System")
st.markdown("### *'Your dreams are yours. They are built on belief and not pressure.'*")
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
        "keywords": ["form", "part", "piece", "staircase", "whole"],
        "solution": "STAIRCASE. Bridge: 'Part-to-Whole'. A spoke is a part of a wheel; a step is a part of a staircase."
    },
    {
        "type": "Figural Logic",
        "question": "Triangle flips from Bottom to Top. Circle 'D' on Right moves to...?",
        "options": ["Stay Right", "Move to Left side", "Become a square"],
        "keywords": ["flip", "mirror", "left", "opposite", "reflect"],
        "solution": "MOVE TO LEFT SIDE. Bridge: 'Reflection'. When you flip an image, right becomes left."
    },
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
    st.progress(st.session_state.step / len(modules))
    
    st.info(f"⚡ **QUIRK ANALYSIS:** {current['type']}")
    st.write(f"### {current['question']}")
    
    choice = st.radio("Select your answer:", current['options'], key=f"r_{st.session_state.step}")
    thought = st.text_input("Describe your 'Logic Lens':", key=f"t_{st.session_state.step}")

    if st.button("GO BEYOND!"):
        if thought:
            duration = round(time.time() - st.session_state.start_time, 2)
            is_match = any(k in thought.lower() for k in current['keywords'])
            
            st.session_state.logs.append({
                "type": current['type'],
                "choice": choice,
                "reasoning": thought,
                "duration": duration,
                "status": "🌟 Success" if is_match else "🔧 Calibrated",
                "solution": current['solution']
            })
            st.session_state.start_time = time.time()
            st.session_state.step += 1
            st.rerun()
        else:
            st.error("Please provide your logic first!")

else:
    st.balloons()
    st.success("🏁 MISSION COMPLETE! PLUS ULTRA!")
    st.write("## 🧠 Final Logic Lens Analysis")
    for log in st.session_state.logs:
        with st.expander(f"🔍 {log['type']} - {log['status']} ({log['duration']}s)"):
            st.write(f"**Your Logic:** {log['reasoning']}")
            st.divider()
            st.info(f"🔑 **The Expert Bridge:**\n\n{log['solution']}")
    if st.button("Restart Mission"):
        st.session_state.step = 0
        st.session_state.logs = []
        st.rerun()