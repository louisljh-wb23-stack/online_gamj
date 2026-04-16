import streamlit as st
import time
import pandas as pd
import joblib

# =========================
# LOAD MODEL
# =========================
model = joblib.load("rf.joblib")

FEATURES = [
    "Age",
    "PlayTimeHours",
    "SessionsPerWeek",
    "AchievementsUnlocked",
    "PlayerLevel",
    "AvgSessionDurationMinutes"
]

# =========================
# INIT STATE
# =========================
if "started" not in st.session_state:
    st.session_state.started = False


# =========================
# START PAGE CSS (unicorn background)
# =========================
start_css = """
<style>

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

.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}

header, footer {
    visibility: hidden;
}

.center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}

.stButton > button {
    background: linear-gradient(45deg, #A4DE02, #8BC34A);
    color: black;
    padding: 20px 85px;
    font-size: 24px;
    font-weight: bold;
    border-radius: 50px;
    border: none;
}

</style>
"""


# =========================
# MAIN PAGE CSS (restore dark)
# =========================
main_css = """
<style>

.stApp {
    background: none !important;
}

</style>
"""


# =========================
# START SCREEN
# =========================
if not st.session_state.started:

    st.markdown(start_css, unsafe_allow_html=True)

    st.markdown('<div class="center">', unsafe_allow_html=True)

    st.title("👾 Press Start")

    if st.button("START"):
        time.sleep(0.2)
        st.session_state.started = True
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# =========================
# MAIN SCREEN + MODEL
# =========================
else:

    st.markdown(main_css, unsafe_allow_html=True)

    st.title("📊 What is your information?")

    # =========================
    # INPUTS
    # =========================
    age = st.number_input("Age", 0, 100, 20)
    playtime = st.number_input("Play Time Hours", 0, 1000, 10)
    sessions = st.number_input("Sessions Per Week", 0, 50, 5)
    achievements = st.number_input("Achievements Unlocked", 0, 1000, 10)
    level = st.number_input("Player Level", 0, 100, 1)
    duration = st.number_input("Avg Session Duration", 0, 300, 30)

    model_name = st.selectbox(
        "Choose Model",
        ["Random Forest", "KNN", "Logistic Regression"]
    )

    # =========================
    # PREDICT BUTTON
    # =========================
    if st.button("Predict"):

        input_data = pd.DataFrame([[
            age,
            playtime,
            sessions,
            achievements,
            level,
            duration
        ]], columns=FEATURES)

        prediction = model.predict(input_data)[0]

        st.success(f"🎯 Predicted Engagement Level: {prediction}")

        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_data)
            st.write("Probability:")
            st.write(proba)

    # =========================
    # BACK BUTTON
    # =========================
    if st.button("Back"):
        st.session_state.started = False
        st.rerun()
