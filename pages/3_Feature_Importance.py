import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

# load model again
with open('ridge_model.pkl', 'rb') as f:
    ridge_model, new_predictors = pickle.load(f)

data = pd.read_csv('player_stats_clean.csv')

st.set_page_config(page_title="Diamond Analytics")
st.title('Feature Importance')


# the feature importances are really just the coef from the model
feature_importances = ridge_model.coef_
features = new_predictors

importance_df = pd.DataFrame({'Feature': features, 'Importance' : feature_importances})

positive_importance_df = (importance_df[importance_df['Importance'] > 0]
                          .sort_values(by='Importance', ascending=False).head(10))

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=positive_importance_df, palette='viridis', ax=ax)
ax.set_title('Top 10 Most Important Statistics')
ax.set_xlabel('Importance')
ax.set_ylabel('Feature')
st.pyplot(fig)