import streamlit as st
import pickle
import requests # library to hit API

def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    # st.text(data)
    # st.text("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US")
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

# similar main function as written in Jupyter notebook
def recommend(movie_name):
    movie_index = df_movies[df_movies["title"] == movie_name].index[0]
    distances = similarity[movie_index]
    recommended_movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x : x[1])[1 : 6]

    recommended_movies = []
    recommended_movies_posters = []

    for recommended_movie in recommended_movies_list:
        movie_id = df_movies.iloc[recommended_movie[0]].movie_id
        
        recommended_movies.append(df_movies.iloc[recommended_movie[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# this movies_list contains the dataframe df, used in Jupyter notebook
df_movies = pickle.load(open("movies.pkl", "rb"))
# the list of all the movies
movies_list = df_movies["title"].values 

similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a movie",
    (movies_list),
)

st.button("Reset", type="primary")

if st.button("Recommend"):
    movie_names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(movie_names[0])
        st.image(posters[0])

    with col2:
        st.text(movie_names[1])
        st.image(posters[1])

    with col3:
        st.text(movie_names[2])
        st.image(posters[2])

    with col4:
        st.text(movie_names[3])
        st.image(posters[3])

    with col5:
        st.text(movie_names[4])
        st.image(posters[4])

    st.write("BINGE THEM ALL !!!")