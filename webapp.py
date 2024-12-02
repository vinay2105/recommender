import pickle
import streamlit as st
import pandas as pd
import requests
import os
st.title('Movie Recommendation App')
new_df = pickle.load(open('movies.pkl','rb'))
movies_list = new_df['title'].values


import gdown
new_df = pickle.load(open('movies.pkl','rb'))

file_id = '1BWTpaIBrpK-o8IUYi9Q0oElai6FDYflM'
url = f"https://drive.google.com/file/d/1BWTpaIBrpK-o8IUYi9Q0oElai6FDYflM/view?usp=sharing={file_id}"

output_file = "similarity.pkl"

gdown.download(url, output_file, quiet=False, fuzzy=True)

print("Download complete!")
import pickle

file_path = 'similarity.pkl'

try:
    with open(file_path, 'rb') as f:
        similarity = pickle.load(f)
except pickle.UnpicklingError as e:
    print(f"Error unpickling file: {e}")


def fetch_movie_poster(movie_id):
    api_key = os.getenv("TMDB_ID")
    base_url = "https://api.themoviedb.org/3/movie/"
    poster_base_url = "https://image.tmdb.org/t/p/w500"

    url = f"{base_url}{movie_id}?api_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return f"{poster_base_url}{poster_path}"
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

movies_names = []
movies_poster = []

option = st.selectbox('Enter movies name', movies_list)
if st.button('recommend'):
    names,posters = recommend(option)
    c1,c2,c3,c4,c5,c6,c7,c8,c9 = st.columns(9)
    
    with c1:
        st.image(posters[0])
        st.write(names[0])
    with c2:
        st.image(posters[1])
        st.write(names[1])
    with c3:
        st.image(posters[2])
        st.write(names[2])
    with c4:
        st.image(posters[3])
        st.write(names[3])
    with c5:
        st.image(posters[4])
        st.write(names[4])
        
    with c6:
        st.image(posters[5])
        st.write(names[5])
        
    with c7:
        st.image(posters[6])
        st.write(names[6])
        
    with c8:
        st.image(posters[7])
        st.write(names[7])
    with c9:
        st.image(posters[8])
        st.write(names[8])