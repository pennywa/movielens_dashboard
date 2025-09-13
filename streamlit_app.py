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

# Interactive filters for age, gender, and occupation
st.subheader("Filter by Demographic")

col1, col2, col3 = st.columns(3)

with col1:
    age_min, age_max = st.slider('Select Age Range', min_value=int(df['age'].min()), max_value=int(df['age'].max()), value=(int(df['age'].min()), int(df['age'].max())))

with col2:
    genders = ['All'] + sorted(df['gender'].unique())
    selected_gender = st.selectbox('Select Gender', genders)

with col3:
    occupations = ['All'] + sorted(df['occupation'].unique())
    selected_occupation = st.selectbox('Select Occupation', occupations)

filtered_df_q1 = df[(df['age'] >= age_min) & (df['age'] <= age_max)]
if selected_gender != 'All':
    filtered_df_q1 = filtered_df_q1[filtered_df_q1['gender'] == selected_gender]
if selected_occupation != 'All':
    filtered_df_q1 = filtered_df_q1[filtered_df_q1['occupation'] == selected_occupation]

# Average rating for the filtered data
genre_counts = filtered_df_q1['genres'].value_counts().sort_values(ascending=False)

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


# Average rating for filtered data
genre_avg_ratings = filtered_df_q1.groupby('genres')['rating'].mean().sort_values(ascending=False)

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

# Filter by the decades
decades = sorted(df['decade'].unique())
decades_list = ['All'] + [int(d) for d in decades if not pd.isna(d)]

selected_decade = st.selectbox('Select a Decade', decades_list)

# Filter df based on the selected decade
if selected_decade != 'All':
    filtered_df = df[df['decade'] == selected_decade]
else:
    filtered_df = df.copy()

# Group by year and calculate the avg rating
yearly_avg_ratings = filtered_df.groupby('year')['rating'].mean()
fig3 = px.line(x=yearly_avg_ratings.index, y=yearly_avg_ratings.values, labels={'x': 'Movie Release Year', 'y': 'Mean Rating'}, title=f'Mean Rating Change for Movies in the {selected_decade}s')
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