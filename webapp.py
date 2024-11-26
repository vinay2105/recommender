import pickle
import streamlit as st
import pandas as pd
from model import recommend
from model import fetch_movie_poster
from sklearn.metrics.pairwise import cosine_similarity
st.title('Movie Recommendation App')
new_df = pickle.load(open('movies.pkl','rb'))
movies_list = new_df['title'].values
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=6000,stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

similarity = cosine_similarity(vectors)
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