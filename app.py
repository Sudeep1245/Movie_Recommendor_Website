import streamlit as st
import pickle
import os
import gdown


def download_similarity_file():
    file_path = "similarity.pkl"
    if not os.path.exists(file_path):
        st.warning("Downloading similarity.pkl from Google Drive...")
        # Replace this with your actual file ID
        file_id = "12NLEDxyYAHqchbwFiAkiuZbetn4O-wd5"
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url,'similarity.pkl', quiet=False)
        st.success("Download complete!")

download_similarity_file()

def recommend(movie):
    movie_index = movies_list[movies_list['title']==movie].index[0]
    distance = similarity[movie_index]
    sim_movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_movies = []

    for i in sim_movie_list:
        recommend_movies.append(movies_list.iloc[i[0]].title)

    return recommend_movies

movies_list = pickle.load(open('movies.pkl','rb'))

similarity = pickle.load(open('similarity.pkl','rb'))

movies_list1 = movies_list['title'].values
st.title('Movie Recommender System')

selected_movie = st.selectbox(
    'Enter your movie name',
    (movies_list1))



if st.button('Recommend'):
    recommendation = recommend(selected_movie)
    for i in recommendation:    
        st.write(i)