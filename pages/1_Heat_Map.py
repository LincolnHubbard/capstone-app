import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('player_stats_clean.csv')

# ignore all non-numeric data types
numeric_data = data.select_dtypes(include=[np.number])

st.set_page_config(page_title="Diamond Analytics")
st.title('OPS Correlation Heat Map')

correlation_matrix = numeric_data.corr()

# only include correlations with OPS
ops_corr = correlation_matrix["OPS"].sort_values(ascending=False)
ops_corr = ops_corr.drop(labels="OPS")

top_bottom_corr = pd.concat([ops_corr.head(5), ops_corr.tail(5)])

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(top_bottom_corr.to_frame(), annot=True, cmap='coolwarm', vmin=-1, vmax=1,
            ax=ax, annot_kws={"size": 10})
plt.xticks(rotation=45, ha='right',fontsize=10)
plt.yticks(fontsize=8)
st.pyplot(fig)