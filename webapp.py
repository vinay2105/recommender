import pickle
import streamlit as st
import pandas as pd
st.title('Movie Recommendation App')
new_df = pickle.load(open('movies.pkl','rb'))
movies_list = new_df['title'].values
import gdown

# Google Drive file ID
file_id = '1BWTpaIBrpK-o8IUYi9Q0oElai6FDYflM'  # Replace this with your file ID
url = f"https://drive.google.com/file/d/1BWTpaIBrpK-o8IUYi9Q0oElai6FDYflM/view?usp=sharing={file_id}"

output_file = "similarity.pkl"
print("Downloading similarity.pkl from Google Drive...")

gdown.download(url, output_file, quiet=False, fuzzy=True)

print("Download complete!")
import pickle

file_path = 'similarity.pkl'

try:
    with open(file_path, 'rb') as f:
        similarity = pickle.load(f)
except pickle.UnpicklingError as e:
    print(f"Error unpickling file: {e}")









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