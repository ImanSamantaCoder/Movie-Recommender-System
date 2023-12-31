import streamlit as st
import pandas as pd
import pickle
import requests
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    return "http://image.tmdb.org/t/p/w500"+data['poster_path']
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
        
        
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name=st.selectbox('How would you like to be contacted',movies['title'].values)
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    
    st.header(names[0])
    st.image(posters[0])
    st.text("next movie")
    st.header(names[1])
    st.image(posters[1])
    st.text("next movie")
    st.header(names[2])
    st.image(posters[2])
    st.text("next movie")
    st.header(names[3])
    st.image(posters[3])
    st.text("next movie")
    st.header(names[4])
    st.image(posters[4])    
