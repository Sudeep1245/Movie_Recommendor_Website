import pandas as pd 
from function_collection import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

def train():
    # loading data
    movies = pd.read_csv('./data/tmdb_5000_movies.csv')
    credits = pd.read_csv('./data/tmdb_5000_credits.csv')

    df = pd.merge(movies,credits,on='title')

    # filtering data
    df = df[['id','title','overview','genres','keywords','cast','crew']]

    df.dropna(inplace =True)

    # Cleaning data
    df['genres'] = df['genres'].apply(extract_names)
    df['keywords'] = df['keywords'].apply(extract_names)
    df['cast'] = df['cast'].apply(extract_top_cast)
    df['crew'] = df['crew'].apply(fetch_director)


    df['overview'] = df['overview'].apply(lambda x:x.split())

    columns = ['genres', 'keywords', 'cast', 'crew']
    for col in columns:
        df[col] = df[col].apply(lambda x:[i.replace(' ','') for i in x])


    df['tag'] = df['overview'] + df['genres'] + df['keywords'] + df['cast'] + df['crew']

    # final filtering
    new_df = df[['id', 'title', 'tag']].copy()

    # preprocessing data
    new_df['tag'] = new_df['tag'].apply(lambda x:' '.join(x))
    new_df['tag'] = new_df['tag'].apply(lambda x:x.lower())
    new_df['tag'] = new_df['tag'].apply(stem)


    # Apply bag of word on clean and preprocessed  data
    tfidf = TfidfVectorizer(max_features=2000, stop_words='english')

    vector = tfidf.fit_transform(new_df['tag'])


    os.makedirs('artifacts', exist_ok=True)


    with open('./artifacts/movies.pkl', 'wb') as f:
        pickle.dump(new_df, f)

    with open('./artifacts/vector.pkl', 'wb') as f:
        pickle.dump(vector, f)

    with open('./artifacts/tfidf.pkl', 'wb') as f:
        pickle.dump(tfidf, f)

if __name__ == '__main__':
    train()