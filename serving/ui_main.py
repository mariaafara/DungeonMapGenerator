"""ui app."""

import json
import os

import requests
import streamlit as st

st.title("Dungeon Map Generator web app")  # define a h1 header with the app title

# define the maze size
maze_size_input = st.number_input("Maze size", value=4,)
episode_input = st.number_input("Number of episodes", value=5,)
alpha_input = st.number_input("Alpha", value=0.3,)
epsilon_input = st.number_input("Epsilon", value=0.2,)
discount_input = st.number_input("Discount", value=0.1,)

# displays a button
if st.button("Generate Maze"):
    if maze_size_input is not None:
        user_input = {"maze_size": maze_size_input,
                      "num_episodes": episode_input,
                      "alpha": alpha_input,
                      "discount": discount_input,
                      "epsilon": epsilon_input}
        response = requests.post(str(os.environ.get("PREDICTION_BASE_URL")) + "/generate_maze",
                                 data=json.dumps(user_input))
        if response.status_code == 200:
            st.success('Generation was successful.')
        st.image(response.content)
else:
    st.write("Insert your inputs/")
