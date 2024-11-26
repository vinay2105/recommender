import pickle
import pandas as pd
import requests

import pickle
import os

from sklearn.metrics.pairwise import cosine_similarity
new_df = pickle.load(open('movies.pkl','rb'))
movies_list = new_df['title'].values
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=6000,stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

similarity = cosine_similarity(vectors)
def fetch_movie_poster(movie_id):
    api_key = os.getenv("TMDB_key")  # Replace with your TMDb API key
    base_url = "https://api.themoviedb.org/3/movie/"
    poster_base_url = "https://image.tmdb.org/t/p/w500"  # Adjust size if needed

    # Make a request to fetch movie details
    url = f"{base_url}{movie_id}?api_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:  # Successful request
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return f"{poster_base_url}{poster_path}"  # Complete poster URL
        else:
            return None
    else:
        print(f"Error: Unable to fetch details for movie ID {movie_id}.")
        return None

def recommend(movie):
    movie_index = new_df[new_df['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:10]
    L = []
    P = []
    for i in movie_list:
        movie_id=new_df.iloc[i[0]].movie_id
        L.append(new_df.iloc[i[0]].title)
        P.append(fetch_movie_poster(movie_id))

    return L,P
