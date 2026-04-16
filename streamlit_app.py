import streamlit as st
import time

# =========================
# INIT STATE
# =========================
if "started" not in st.session_state:
    st.session_state.started = False


# =========================
# CSS
# =========================
st.markdown(
    """
    <style>

    /* ❗ lock full screen */
    html, body {
        height: 100%;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }

    .stApp {
        height: 100vh;
        overflow: hidden;

        background-image: url("https://raw.githubusercontent.com/louisljh-wb23-stack/online_gamj/326d080c022ad5d8648e064b01dda026c446aba9/unicorn.png");
        background-size: 45%;
        background-repeat: no-repeat;
        background-position: center;
    }

    /* remove streamlit padding */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* ⭐ TRUE CENTER (FIXED) */
    .center {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
    }

    /* fade in */
    .fade-in {
        animation: fadeIn 1s ease-in;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    /* BUTTON STYLE */
    .stButton > button {
        background: linear-gradient(45deg, #A4DE02, #8BC34A);
        color: black;
        padding: 20px 85px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 50px;
        border: none;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: scale(1.08);
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================
# START SCREEN
# =========================
if not st.session_state.started:

    st.markdown('<div class="center fade-in">', unsafe_allow_html=True)

    st.title("🎮 Welcome")

    if st.button("START"):
        time.sleep(0.3)
        st.session_state.started = True
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# =========================
# MAIN APP
# =========================
else:

    st.markdown('<div class="center fade-in">', unsafe_allow_html=True)

    st.title("📊 Input Interface")

    age = st.number_input("Age", 0, 100, 20)
    sessions = st.number_input("Sessions Per Week", 0, 50, 5)
    duration = st.number_input("Avg Session Duration", 0, 300, 30)

    model = st.selectbox(
        "Choose Model",
        ["KNN", "Random Forest", "Logistic Regression"]
    )

    if st.button("Back"):
        st.session_state.started = False
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
