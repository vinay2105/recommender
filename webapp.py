import pickle
import streamlit as st
import pandas as pd
st.title('Movie Recommendation App')
new_df = pickle.load(open('movies.pkl','rb'))
movies_list = new_df['title'].values
import urllib.request
url = "https://drive.google.com/file/d/1EJKk3fhC-krId6_mV_Ufp-iW8zm-JHKr/view?usp=sharing"
similarity = "similarity.pkl"
similarity = urllib.request.urlretrieve(url, similarity)


def recommend(movie):
    movie_index = new_df[new_df['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x:x[1])[1:6]
    L = []
    for i in movie_list:
        L.append(new_df.iloc[i[0]].title)
    return L



option = st.selectbox('Enter movies name', movies_list)
if st.button('recommend'):
    Recommendations = recommend(option)
    for i in Recommendations:
        st.write(i)