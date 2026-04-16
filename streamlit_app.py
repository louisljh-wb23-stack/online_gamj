import streamlit as st

# =========================
# init state
# =========================
if "started" not in st.session_state:
    st.session_state.started = False

# =========================
# START SCREEN
# =========================
if not st.session_state.started:

    # -------- BACKGROUND IMAGE --------
    page_bg = """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1521737604893-d14cc237f11d");
        background-size: cover;
        background-position: center;
    }

    /* hide default streamlit elements */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

    # -------- CENTER BUTTON --------
    st.markdown(
        """
        <style>
        .center-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;
            flex-direction: column;
        }

        .start-btn {
            background-color: white;
            padding: 15px 50px;
            border-radius: 30px;
            font-size: 20px;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="center-container">', unsafe_allow_html=True)

    if st.button("START"):
        st.session_state.started = True
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# MAIN APP
# =========================
else:
    st.title("Input Interface")

    age = st.number_input("Age")
    sessions = st.number_input("Sessions per Week")

    if st.button("Back to Start"):
        st.session_state.started = False
        st.rerun()
