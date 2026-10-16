
import streamlit as st

st.set_page_config(page_title="Cricket Score Predictor", page_icon="🏏")

st.title("🏏 Cricket Score Predictor")
st.write("Welcome to our Cricket Dashboard!")

team = st.selectbox(
    "Choose batting team",
    ["India", "Australia", "England", "Pakistan"]
)

overs = st.slider("Overs completed", 1, 19, 10)
runs = st.number_input("Current runs", min_value=0, max_value=500, value=100)
wickets = st.slider("Wickets lost", 0, 10, 2)

run_rate = runs / overs
predicted_score = round(run_rate * 20)

st.metric("Current Run Rate", round(run_rate, 2))
st.metric("Projected 20-over Score", predicted_score)
st.write(f"Batting team: {team}")
st.write(f"Wickets lost: {wickets}")
