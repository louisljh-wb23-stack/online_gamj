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
        /* background */
        .stApp {
            background-image: url("https://raw.githubusercontent.com/louisljh-wb23-stack/online_gamj/326d080c022ad5d8648e064b01dda026c446aba9/unicorn.png");
            background-size: cover;
            background-position: center;
        }

        /* hide streamlit UI */
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* center container */
        .center-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;
            flex-direction: column;
        }

        /* streamlit button style */
        .stButton > button {
            background-color: #A4DE02;   /* 黄绿色 */
            color: black;
            padding: 18px 70px;
            font-size: 22px;
            font-weight: bold;
            border-radius: 40px;
            border: none;
            box-shadow: 0px 6px 18px rgba(0,0,0,0.25);
            transition: all 0.25s ease-in-out;
        }

        .stButton > button:hover {
            background-color: #8BC34A;
            transform: scale(1.08);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="center-container">', unsafe_allow_html=True)

    st.title("")

    if st.button("START"):
        st.session_state.started = True
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# =========================
# MAIN APP
# =========================
else:

    st.title("🎮 Player Engagement Input Interface")

    st.write("Enter player data below:")

    age = st.number_input("Age", min_value=0, max_value=100, value=20)
    sessions = st.number_input("Sessions Per Week", min_value=0)
    duration = st.number_input("Avg Session Duration (min)", min_value=0)

    model = st.selectbox(
        "Choose Model",
        ["KNN", "Random Forest", "Logistic Regression"]
    )

    st.write("Selected Model:", model)

    if st.button("Back to Start"):
        st.session_state.started = False
        st.rerun()
