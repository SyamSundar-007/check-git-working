import pandas as pd
import streamlit as st
import pickle as pkl
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



data = pkl.load( open('df_new.pkl', 'rb'))
indices = pkl.load( open('indices.pkl' , 'rb') )
tfidf_matrix = pkl.load( open("tfidf_matrix.pkl" , 'rb') )
tf_idf = pkl.load(open('tfidf.pkl',"rb"))
# indices = indices
# print( type(indices) )
# print( indices )
indices.index = indices.index.str.lower()
def recomend_movie( title , n=10):
    if title not in indices:
        return['Movie not found']
    idx = indices[title]
    sim_score = cosine_similarity(tfidf_matrix[idx],tfidf_matrix ).flatten()
    similar_index = sim_score.argsort()[::-1][1:n+1]
    return data['title'].iloc[similar_index]

# text = input("Enter the movie: ")

# # list_mov = recomend_movie( text)
# # print(list_mov)


# # st.title("Movie Recommendation System")



# return
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="📊",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------
st.title("📊 My Streamlit App")
st.write("Welcome to my application!")


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("Navigation")

option = st.sidebar.selectbox(
    "Choose an option",
    ["Home", "Data", "Analysis"]
)


# -----------------------------
# Session State
# -----------------------------
if "count" not in st.session_state:
    st.session_state.count = 0


# -----------------------------
# Home
# -----------------------------
if option == "Home":
    st.header("Home")

    movie_name = st.text_input("Enter your movie name")

    if st.button("Check recomendations"):
        movie_list = recomend_movie(movie_name )
        for idx, value  in enumerate(movie_list, start=1):
            st.write(f"{idx} . {value}")


# -----------------------------
# Data
# -----------------------------
elif option == "Data":

    st.header("Data")

    uploaded_file = st.file_uploader(
        "Upload CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("File uploaded successfully!")

        st.write("Shape:", df.shape)

        st.dataframe(df)


# -----------------------------
# Analysis
# -----------------------------
elif option == "Analysis":

    st.header("Analysis")

    st.write("Put your analysis here.")

    # Example
    # st.bar_chart(df["column_name"])


