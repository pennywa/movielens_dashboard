import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Movie Ratings Analysis Dashboards",
    page_icon="🎬",
    layout="wide"
)

df = pd.read_csv('movie_ratings.csv')

st.title("Movie Ratings Analysis Dashboard")
st.markdown("---")
st.header("Key Insights and Visualizations")
st.markdown("---")

# Question 1: What's the breakdown of genres for the movies that were rated?
st.title("Genre Breakdown for Rated Movies")
st.markdown("What's the breakdown of genres for the movies that were rated? ")
st.markdown("Here, we see the distribution of movie ratings across different genres. ")

# Count of ratings for each genre
genre_counts = df['genres'].value_counts().sort_values(ascending=False)

# Matplotlib bar chart
fig, ax = plt.subplots(figsize=(13, 8))
ax.bar(genre_counts.index, genre_counts.values, color='skyblue')
ax.set_title('Number of Ratings per Genre', fontsize=16, fontweight='bold')
ax.set_xlabel('Genres', fontsize=12)
ax.set_ylabel('Number of Ratings', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

st.pyplot(fig)

# Question 2: Which genres have the highest viewer satisfaction (highest ratings)?
st.title("Genres with the highest ratings")
st.markdown("Which genres have the highest viewer satisfaction (highest ratings)? ")
st.markdown("Here, we see which genres have the highest viewer satisfication. ")

# Average rating for each genre
genre_avg_ratings = df.groupby('genres')['rating'].mean().sort_values(ascending=False)

# Seaborn bar chart
fig2, ax2 = plt.subplots(figsize=(13, 8))
sns.barplot(x=genre_avg_ratings.index, y=genre_avg_ratings.values, palette='viridis', ax=ax2)
ax2.set_title('Average Rating per Genre', fontsize=16, fontweight='bold')
ax2.set_xlabel('Genre', fontsize=12)
ax2.set_ylabel('Average Rating', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

st.pyplot(fig2)