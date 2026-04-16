import streamlit as st
import joblib
import numpy as np

# =========================
# LOAD MODEL
# =========================
model = joblib.load("rf.joblib")

st.title("🎮 Player Engagement Prediction App")

st.write("Enter player behavior data to predict engagement level.")

# =========================
# INPUT FEATURES
# =========================
age = st.number_input("Age", min_value=0, max_value=100, value=20)
play_time = st.number_input("Play Time Hours", min_value=0.0, value=5.0)
sessions = st.number_input("Sessions Per Week", min_value=0, value=3)
achievements = st.number_input("Achievements Unlocked", min_value=0, value=10)
player_level = st.number_input("Player Level", min_value=0, value=1)
avg_session = st.number_input("Avg Session Duration (minutes)", min_value=0.0, value=30.0)

# =========================
# PREDICTION
# =========================
if st.button("Predict Engagement Level"):
    
    X = np.array([[age,
                   play_time,
                   sessions,
                   achievements,
                   player_level,
                   avg_session]])

    prediction = model.predict(X)[0]

    st.success(f"Predicted Engagement Level: {prediction}")
