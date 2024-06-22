import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('player_stats_clean.csv')

# ignore all non-numeric data types
numeric_data = data.select_dtypes(include=[np.number])

st.set_page_config(page_title="Diamond Analytics")
st.title('OPS Correlation Pair Plots')

correlation_matrix = numeric_data.corr()

ops_corr = correlation_matrix["OPS"].sort_values(ascending=False, key=abs)

# don't include OPS in the correlations
top_features = ops_corr.index[1:6]

# iterate through each feature and generate pair plot
tab_labels = top_features.unique().tolist()
tabs = st.tabs(tab_labels)

for tab, feature in zip(tabs, tab_labels):
    with tab:
        st.subheader(f'Scatter Plot: {feature} vs OPS')
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x=feature, y='OPS', ax=ax)
        ax.set_title(f'{feature} vs OPS')
        ax.set_xlabel(feature)
        ax.set_ylabel('OPS')
        st.pyplot(fig)

