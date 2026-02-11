import streamlit as st
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Plus Ultra Logic System", page_icon="🚀")

# --- CUSTOM CSS: CRISP DARK MODE ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    h1, h2, h3, p, label { color: #FFFFFF !important; }
    .stButton>button { 
        background-color: #FF4B4B; 
        color: white; 
        font-weight: bold; 
        border-radius: 10px;
        width: 100%;
    }
    .stTextInput>div>div>input { background-color: #262730; color: white; }
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
    st.session_state.start_time = time.time() # Start the clock for the first question

# --- THE CORE MODULES ---
modules = [
    {
        "type": "Verbal Logic",
        "question": "SPOKE : WHEEL :: STEP : ?",
        "options": ["Walk", "Staircase", "Shoe", "Run"],
        "keywords": ["form", "part", "piece", "staircase", "whole", "build"],
        "hint": "Think of building blocks. How does the first piece fit the second?"
    },
    {
        "type": "Figural Logic",
        "question": "Triangle flips from Bottom to Top. Circle 'D' on Right moves to...?",
        "options": ["Stay Right/Upside down", "Move to Left side", "Become a square"],
        "keywords": ["flip", "mirror", "left", "pancake", "opposite", "reflect"],
        "hint": "Is it spinning like a wheel or flipping like a pancake?"
    },
    {
        "type": "Numeric Logic",
        "question": "2, 6, 18, 54, ?",
        "options": ["108", "162", "200"],
        "keywords": ["multiply", "times", "x3", "3", "tripled", "growth"],
        "hint": "Is the bridge between numbers adding or multiplying?"
    },
    {
        "type": "Matrix Logic",
        "question": "Row 1: Circle -> Circle + Square. Row 2: Triangle -> ?",
        "options": ["Triangle + Square", "Just a Square", "Small Triangle"],
        "keywords": ["inside", "fill", "square", "triangle", "middle", "add"],
        "hint": "Look across the row. What 'filling' was added to the first shape?"
    }
]

# --- THE MENTOR INTERFACE ---
if st.session_state.step < len(modules):
    current = modules[st.session_state.step]
    
    # Progress Bar
    progress = st.session_state.step / len(modules)
    st.progress(progress)
    
    st.info(f"**Current Scan:** {current['type']}")
    st.write(f"### {current['question']}")
    
    # User Input
    choice = st.radio("Pick the best fit:", current['options'], key=f"r_{st.session_state.step}")
    thought = st.text_input("How does your 'Logic Lens' see this? (Describe the bridge):", key=f"t_{st.session_state.step}")

    if st.button("Submit Logic & Move Beyond"):
        if thought:
            # Calculate Time Taken
            end_time = time.time()
            duration = round(end_time - st.session_state.start_time, 2)
            
            # NLP KEYWORD CHECKING
            is_match = any(key in thought.lower() for key in current['keywords'])
            
            # Record Data
            entry = {
                "type": current['type'],
                "question": current['question'],
                "choice": choice,
                "reasoning": thought,
                "duration": duration,
                "status": "🌟 Success" if is_match else "🔧 Calibrated"
            }
            st.session_state.logs.append(entry)
            
            # Reset timer for next question
            st.session_state.start_time = time.time()
            st.session_state.step += 1
            st.rerun()
        else:
            st.error("The system needs to hear your logic before moving on!")

# --- FINAL RESEARCH REPORT ---
else:
    st.balloons()
    st.success("🏁 MISSION COMPLETE! PLUS ULTRA!")
    st.write("## 🧠 Final Logic Lens Analysis")
    
    for log in st.session_state.logs:
        with st.expander(f"🔍 {log['type']} - {log['status']} ({log['duration']}s)"):
            st.write(f"**Question:** {log['question']}")
            st.write(f"**Answer Picked:** {log['choice']}")
            st.write(f"**Learner's Logic:** {log['reasoning']}")
            st.write(f"**Time Spent:** {log['duration']} seconds")
            
    if st.button("Restart System"):
        st.session_state.step = 0
        st.session_state.logs = []
        st.session_state.start_time = time.time()
        st.rerun()