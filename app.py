import streamlit as st
import time
import json
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Plus Ultra Logic System", page_icon="🚀", layout="centered")

# --- UI DESIGN (Your Custom Style) ---
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images6.alphacoders.com/997/thumb-1920-997829.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(15, 23, 42, 0.88);
        backdrop-filter: blur(5px);
        z-index: -1;
    }
    .stMarkdown, .stRadio, .stTextInput, .stAlert, .stExpander {
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(10px);
        padding: 20px !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        margin-bottom: 15px !important;
    }
    h1, h2, h3, p, span, label {
        color: #f1faee !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
    }
    div.stButton > button {
        background-color: #e63946 !important;
        color: white !important;
        font-weight: bold !important;
        border: 2px solid #f1faee !important;
        box-shadow: 0px 0px 15px rgba(230, 57, 70, 0.5) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- JSON LOADER LOGIC ---
def load_questions():
    # If the file exists, load it; otherwise, use a fallback to prevent crashing
    if os.path.exists('questions.json'):
        with open('questions.json', 'r') as f:
            return json.load(f)
    else:
        st.error("Missing 'questions.json' file! Please ensure it is in the same folder.")
        return []

# --- INITIALIZE SESSION STATE ---
if 'modules' not in st.session_state:
    st.session_state.modules = load_questions()
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# --- THE MENTOR INTERFACE ---
st.title("🚀 Plus Ultra Logic System")
st.markdown("### *'Your dreams are yours. They are built on belief and not pressure. Go Beyond! Plus Ultra!🦸‍♂️'*")
st.write("---")

# Use modules from session state
modules = st.session_state.modules

if st.session_state.step < len(modules):
    current = modules[st.session_state.step]
    
    # Track Progress
    st.write(f"📝 **Mission Progress: {st.session_state.step + 1} / {len(modules)}**")
    
    # Mapping JSON keys to your UI labels
    st.info(f"⚡ **QUIRK ANALYSIS:** {current.get('type', 'General Logic')}")
    st.write(f"### {current['question']}")
    
    choice = st.radio("Select your answer:", current['options'], key=f"r_{st.session_state.step}")
    thought = st.text_input("Describe your 'Logic Lens' (The Bridge):", key=f"t_{st.session_state.step}")

    if st.button("GO BEYOND!"):
        if thought:
            # --- SAVE DATA BEFORE MOVING TO NEXT STEP ---
            duration = round(time.time() - st.session_state.start_time, 2)
            
            # NLP-style keyword check
            keywords = current.get('keywords', [])
            is_match = any(k.lower() in thought.lower() for k in keywords)
            
            st.session_state.logs.append({
                "type": current.get('type', 'General Logic'),
                "choice": choice,
                "reasoning": thought,
                "duration": duration,
                "status": "🌟 Success" if is_match else "🔧 Calibrated",
                "solution": current.get('explanation', 'Review logic for this pattern.')
            })
            
            # Update state for next question
            st.session_state.start_time = time.time()
            st.session_state.step += 1
            st.rerun()
        else:
            st.warning("Explain your logic to finalize this step!")

elif len(modules) > 0:
    st.balloons()
    st.success("🏁 MISSION COMPLETE! FINAL ANALYSIS READY.")
    
    # --- DISPLAY THE COMPLETE LOGS ---
    for log in st.session_state.logs:
        with st.expander(f"🔍 {log['type']} Result - {log['status']} ({log['duration']}s)"):
            st.write(f"**Your Choice:** {log['choice']}")
            st.write(f"**Your Logic:** {log['reasoning']}")
            st.divider()
            st.info(f"🔑 **The Expert Bridge:**\n\n{log['solution']}")
            
    if st.button("Restart Mission"):
        st.session_state.step = 0
        st.session_state.logs = []
        st.rerun()