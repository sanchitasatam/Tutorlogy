import streamlit as st
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Plus Ultra Logic System", page_icon="🚀")

# --- CUSTOM CSS: MHA HERO ACADEMY THEME ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0b0e14 0%, #1c2538 100%);
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #e63946;
        color: white;
        font-weight: bold;
        border: 2px solid #f1faee;
        border-radius: 8px;
        box-shadow: 0px 0px 15px rgba(230, 57, 70, 0.3);
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #f1faee;
        color: #e63946;
    }
    .stTextInput>div>div>input {
        background-color: #262730;
        color: #4cc9f0;
        border: 1px solid #4cc9f0;
    }
    h1, h2, h3 { color: #f1faee !important; }
    .streamlit-expanderHeader {
        background-color: #161b22;
        color: #4cc9f0 !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🚀 Plus Ultra Logic System")
st.markdown("### *'Your dreams are yours. They are built on belief and not pressure.Go beyond Plus Ultra!'*")
st.write("---")

# --- INITIALIZE SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# --- THE 4 CORE MODULES ---
modules = [
    {
        "type": "Verbal Logic",
        "question": "SPOKE : WHEEL :: STEP : ?",
        "options": ["Walk", "Staircase", "Shoe", "Run"],
        "keywords": ["form", "part", "piece", "staircase", "whole", "build"],
        "solution": "STAIRCASE. Bridge: 'Part-to-Whole'. A spoke is a piece of a wheel; a step is a piece of a staircase."
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
        "keywords": ["multiply", "times", "x3", "3", "growth"],
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

# --- THE MENTOR INTERFACE ---
if st.session_state.step < len(modules):
    current = modules[st.session_state.step]
    st.progress(st.session_state.step / len(modules))
    
    st.info(f"⚡ **QUIRK ANALYSIS:** {current['type']}")
    st.write(f"### {current['question']}")
    
    choice = st.radio("Select your answer:", current['options'], key=f"r_{st.session_state.step}")
    thought = st.text_input("Describe your 'Logic Lens':", key=f"t_{st.session_state.step}", placeholder="How did you find the bridge?")

    if st.button("GO BEYOND!"):
        if thought:
            duration = round(time.time() - st.session_state.start_time, 2)
            is_match = any(key in thought.lower() for key in current['keywords'])
            
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
            st.write(f"**Your Answer:** {log['choice']}")
            st.divider()
            st.info(f"🔑 **The Expert Bridge:**\n\n{log['solution']}")
            
    if st.button("Restart Mission"):
        st.session_state.step = 0
        st.session_state.logs = []
        st.rerun()