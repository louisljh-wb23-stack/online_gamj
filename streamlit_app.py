import streamlit as st

# =========================
# INIT STATE
# =========================
if "started" not in st.session_state:
    st.session_state.started = False


# =========================
# START SCREEN
# =========================
if not st.session_state.started:

    st.markdown(
        """
        <style>

        /* === TILE BACKGROUND === */
        .stApp {
            background-image: url("https://raw.githubusercontent.com/louisljh-wb23-stack/online_gamj/326d080c022ad5d8648e064b01dda026c446aba9/unicorn.png");
            background-repeat: repeat;      /* 平铺 */
            background-size: 200px 200px;   /* 每个tile大小（关键） */
            background-position: top left;
        }

        /* hide streamlit UI */
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* === FULL SCREEN CENTER === */
        .center-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;   /* 全屏垂直居中 */
            flex-direction: column;
        }

        /* === START BUTTON === */
        .stButton > button {
            background: linear-gradient(45deg, #A4DE02, #8BC34A);
            color: black;
            padding: 20px 90px;
            font-size: 24px;
            font-weight: bold;
            border-radius: 50px;
            border: none;
            box-shadow: 0px 10px 25px rgba(0,0,0,0.3);
            transition: 0.25s;
        }

        .stButton > button:hover {
            transform: scale(1.08);
            box-shadow: 0px 14px 30px rgba(0,0,0,0.4);
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # CENTER CONTENT
    st.markdown('<div class="center-container">', unsafe_allow_html=True)

    st.title("🎮 Game Engagement Model")

    st.write("Click start to enter system")

    if st.button("START"):
        st.session_state.started = True
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# =========================
# MAIN APP
# =========================
else:

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
