import streamlit as st
import pandas as pd
import joblib

# =========================
# LOAD MODELS
# =========================
models = {
    "Logistic Regression": joblib.load("lg.joblib"),
    "KNN": joblib.load("knn.joblib"),
    "Decision Tree": joblib.load("dt.joblib"),
    "Random Forest": joblib.load("rf2.joblib"),
}

# =========================
# COMMON FEATURES 
# =========================
FEATURES = [
    "Age",
    "PlayTimeHours",
    "SessionsPerWeek",
    "AchievementsUnlocked",
    "PlayerLevel",
    "AvgSessionDurationMinutes"
]

# =========================
# SESSION STATE
# =========================
if "started" not in st.session_state:
    st.session_state.started = False

if "model_name" not in st.session_state:
    st.session_state.model_name = "Random Forest"

# =========================
# SIDEBAR MODEL SELECT
# =========================
st.sidebar.title("⚙️ Model Selection")

model_name = st.sidebar.selectbox(
    "Choose Model",
    list(models.keys()),
    index=list(models.keys()).index(st.session_state.model_name)
)

st.session_state.model_name = model_name
model = models[model_name]

st.sidebar.markdown("---")
st.sidebar.success(f"Current model:\n{model_name}")

# =========================
# START SCREEN CSS
# =========================
start_css = """
<style>
.stApp {
    background-image: url("https://raw.githubusercontent.com/louisljh-wb23-stack/online_gamj/326d080c022ad5d8648e064b01dda026c446aba9/unicorn.png");
    background-size: 45%;
    background-repeat: no-repeat;
    background-position: center;
}
.center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
}
</style>
"""

main_css = """
<style>
.stApp { background: none !important; }
</style>
"""

# =========================
# START PAGE
# =========================
if not st.session_state.started:

    st.markdown(start_css, unsafe_allow_html=True)
    st.markdown('<div class="center">', unsafe_allow_html=True)

    st.title("👾 Press Start")

    if st.button("START"):
        st.session_state.started = True
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# MAIN APP
# =========================
else:

    st.markdown(main_css, unsafe_allow_html=True)

    st.title(f"🎮 Player Engagement Predictor")

    # =========================
    # INPUTS (统一 features)
    # =========================
    age = st.number_input("Age", 0, 99999, 20)
    playtime = st.number_input("Play Time Hours", 0, 99999, 10)
    sessions = st.number_input("Sessions Per Week", 0, 99999, 5)
    achievements = st.number_input("Achievements Unlocked", 0, 99999, 10)
    level = st.number_input("Player Level", 0, 99999, 1)
    duration = st.number_input("Avg Session Duration (Minutes)", 0, 99999, 30)

    # =========================
    # PREDICT
    # =========================
    if st.button("Predict"):

        input_data = pd.DataFrame([{
            "Age": age,
            "PlayTimeHours": playtime,
            "SessionsPerWeek": sessions,
            "AchievementsUnlocked": achievements,
            "PlayerLevel": level,
            "AvgSessionDurationMinutes": duration
        }])

        with st.spinner(f"Running {model_name}..."):
            pred = model.predict(input_data)[0]

        label_map = {0: "Low", 1: "Medium", 2: "High"}
        label = label_map.get(pred, str(pred))

        st.success(f"🎯 Prediction ({model_name}): {label}")

        # =========================
        # PROBABILITY
        # =========================
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_data)[0]
            classes = model.classes_

            st.write("📊 Probability:")
            st.write(dict(zip(classes, proba)))

    # =========================
    # BACK
    # =========================
    if st.button("Back"):
        st.session_state.started = False
        st.rerun()
