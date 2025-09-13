import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

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
ax.set_xlabel('Genre', fontsize=12)
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
sns.barplot(x=genre_avg_ratings.index, y=genre_avg_ratings.values, color='skyblue', ax=ax2)
ax2.set_title('Average Rating per Genre', fontsize=16, fontweight='bold')
ax2.set_xlabel('Genre', fontsize=12)
ax2.set_ylabel('Average Rating', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

st.pyplot(fig2)

# Question 3: How does mean rating change across movie release years?
st.title("Average Rating Across Movie Release Years")
st.markdown("How does mean rating change across movie release years? ")
st.markdown("Here, we see the change in average rating across the years. ")

# Mean rating for each movie release year
yearly_avg_ratings = df.groupby('year')['rating'].mean()

# Plotly line chart
fig3 = px.line(x=yearly_avg_ratings.index, y=yearly_avg_ratings.values, labels={'x': 'Movie Release Year', 'y': 'Mean Rating'}, title='Mean Rating Change Across Movie Release Years')

st.plotly_chart(fig3)

# Question 4: What are the 5 best-rated movies that have at least 50 ratings? At least 150 ratings?
st.title("Best-rated movies")
st.markdown("What are the 5 best-rated movies that have at least 50 ratings? At least 150 ratings? ")
st.markdown("Here, we see the Top 5 best-rated movies. ")

# Button to select the minimum ratings filter
min_ratings_choice = st.radio("Select minimum number of ratings:", ('50', '100', '150', '200'))
min_ratings = int(min_ratings_choice)

# Filter df based on user selection
movie_counts = df['title'].value_counts()
popular_movies = movie_counts[movie_counts >= min_ratings].index
top_5_movies = df[df['title'].isin(popular_movies)].groupby('title')['rating'].mean().sort_values(ascending=False).head(5)


st.subheader(f"Top 5 Movies with at least {min_ratings} Ratings")
fig, ax = plt.subplots(figsize=(13, 8))
ax.barh(top_5_movies.index[::-1], top_5_movies.values[::-1], color='skyblue')
ax.set_xlabel('Average Rating')
ax.set_ylabel('Movie Title')
ax.set_title(f'Top 5 Best-Rated Movies (Min. {min_ratings} Ratings)')
st.pyplot(fig)