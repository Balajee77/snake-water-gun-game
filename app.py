import streamlit as st
import random

st.title("🐍 Snake - 💧 Water - 🔫 Gun")

choices = ["snake", "water", "gun"]

user = st.selectbox("Choose your option:", choices)

if st.button("Play 🎮"):

    computer = random.choice(choices)

    if user == computer:
        result = "It's a Draw! 🤝"

    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        result = "You Win! 🎉"

    else:
        result = "You Lose! 😢"

    st.write("### Your choice:", user)
    st.write("### Computer choice:", computer)
    st.write("##", result)