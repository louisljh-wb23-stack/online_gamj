import streamlit as st

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

    /* FULL SCREEN FIX */
    html, body, .stApp {
        height: 100vh;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }

    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
    }

    /* BACKGROUND IMAGE + FADE IN */
    .stApp {
        background-image: url("https://raw.githubusercontent.com/louisljh-wb23-stack/online_gamj/326d080c022ad5d8648e064b01dda026c446aba9/unicorn.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;

        animation: bgFadeIn 1.2s ease-in;
    }

    @keyframes bgFadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    /* CENTER CONTAINER (slightly lower) */
    .center {
        position: absolute;
        top: 58%;   /* ↓ 往下移一点 */
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
    }

    /* START BUTTON */
    .stButton > button {
        background: linear-gradient(45deg, #A4DE02, #8BC34A);
        color: black;
        padding: 22px 95px;
        font-size: 26px;
        font-weight: bold;
        border-radius: 50px;
        border: none;
        box-shadow: 0px 12px 30px rgba(0,0,0,0.35);
        transition: all 0.3s ease-in-out;
    }

    .stButton > button:hover {
        transform: scale(1.08);
    }

    /* FADE IN FOR MAIN PAGE */
    .fade-in {
        animation: fadeIn 0.8s ease-in;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
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

    if st.button("START"):
        st.session_state.started = True
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# =========================
# MAIN SCREEN
# =========================
else:

    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    st.title("Input Interface")

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
