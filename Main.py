import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import Ridge

# load model and predictors list
with open('ridge_model.pkl', 'rb') as f:
    ridge_model, new_predictors = pickle.load(f)

# load the data
data_clean = pd.read_csv("player_stats_clean.csv")
data_raw = pd.read_csv("player_stats_raw.csv")

player_names = data_clean["Name"].unique().tolist()

# main application
st.set_page_config(page_title="Diamond Analytics")
st.title('Diamond Analytics Player Evaluation (OPS)')


player_name = st.selectbox('Select player name:', [''] + sorted(player_names))

if player_name:
    st.write(f'Searching for player: {player_name}')
    player_data_raw = data_raw[data_raw["Name"].str.contains(player_name, case=False)]  # for display to the user
    player_data_clean = data_clean[data_clean["Name"].str.contains(player_name, case=False)]  # for use by the model

    # style.format() will stop it from formatting the season year as a number
    display_columns = ["Name", "Team", "Season", "OPS", "AVG", "SLG"]
    player_data_filtered = (player_data_raw[display_columns].sort_values(by="Season")
                            .style.format({'Season': lambda x: f"{x:.0f}"}))
    st.dataframe(player_data_filtered, hide_index=True)

    if not player_data_clean.empty:
        # needs to be converted to numpy array
        player_features = player_data_clean[new_predictors].iloc[0].values.reshape(1, -1)

        predicted_ops = ridge_model.predict(player_features)[0]
        st.write(f'Predict OPS for {player_name} in 2024: {predicted_ops}')
    else:
        st.write('Player not found')
