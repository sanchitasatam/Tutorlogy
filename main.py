import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Plus Ultra Logic System", page_icon="🚀")

# --- CUSTOM CSS FOR THE 'PLUS ULTRA' VIBE ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { background-color: #007bff; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER & WELCOME ---
st.title("🚀 Plus Ultra Logic System")
st.subheader("Your dreams are yours. They are built on belief and not pressure.")
st.write("---")

# --- INITIALIZE SESSION STATE (To remember his progress) ---
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'logs' not in st.session_state:
    st.session_state.logs = []

# --- THE MODULES ---
modules = [
    {
        "type": "Verbal Logic",
        "question": "SPOKE : WHEEL :: STEP : ?",
        "options": ["Walk", "Staircase", "Shoe", "Run"],
        "keywords": ["form", "part", "piece", "staircase", "whole"],
        "hint": "Think of building blocks. How does the first piece fit the second?"
    },
    {
        "type": "Figural Logic",
        "question": "If a triangle flips from Bottom to Top, and a circle has a 'D' on the Right... where does the 'D' move?",
        "options": ["Stay Right/Upside down", "Move to Left side", "Become a square"],
        "keywords": ["flip", "mirror", "left", "pancake", "opposite"],
        "hint": "Is it spinning like a wheel or flipping like a pancake?"
    }
]

# --- THE INTERACTIVE LOOP ---
if st.session_state.step < len(modules):
    current = modules[st.session_state.step]
    
    st.info(f"**Current Scan:** {current['type']}")
    st.write(f"### {current['question']}")
    
    choice = st.radio("Pick your answer:", current['options'])
    thought = st.text_input("How does your 'Logic Lens' see this? (Describe your bridge):")

    if st.button("Submit Logic"):
        # Adaptive Feedback Logic
        if any(key in thought.lower() for key in current['keywords']):
            st.success("🌟 LOGIC MATCHED! You found the Expert Bridge.")
            st.session_state.logs.append(f"{current['type']}: Success")
        else:
            st.warning(f"🔧 CALIBRATING... {current['hint']}")
            st.session_state.logs.append(f"{current['type']}: Calibrated")
        
        st.session_state.step += 1
        st.rerun()

else:
    st.balloons()
    st.success("🏁 MISSION COMPLETE! PLUS ULTRA!")
    st.write("### Final Logic Report for the Mentor:")
    for log in st.session_state.logs:
        st.write(f"- {log}")
    
    if st.button("Restart System"):
        st.session_state.step = 0
        st.session_state.logs = []
        st.rerun()