import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity

with open('./artifacts/movies.pkl', 'rb') as f:
    movies_list = pickle.load(f)
with open('./artifacts/vector.pkl', 'rb') as f:
    vector = pickle.load(f)



def recommend(movie):
    movie_index = movies_list[movies_list['title']==movie].index[0]
    similarity = cosine_similarity(vector[movie_index:movie_index+1],vector).flatten()
    sim_movie_list = sorted(list(enumerate(similarity)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_movies = []

    for i in sim_movie_list:
        recommend_movies.append(movies_list.iloc[i[0]].title)

    return recommend_movies


movies_titles = movies_list['title'].values
st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'Enter your movie name',
    (movies_titles))



if st.button('Recommend'):
    recommendation = recommend(selected_movie)
    for i in recommendation:    
        st.write(i)