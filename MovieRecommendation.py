
import streamlit as st

# AI-Based Rule-Based Movie Recommendation System

movies = [
    {
        "name": "3 Idiots",
        "genre": "Comedy",
        "mood": "Happy"
    },
    {
        "name": "The Hangover",
        "genre": "Comedy",
        "mood": "Happy"
    },
    {
        "name": "Hera Pheri",
        "genre": "Comedy",
        "mood": "Happy"
    },
    {
        "name": "Avengers: Endgame",
        "genre": "Action",
        "mood": "Excited"
    },
    {
        "name": "War",
        "genre": "Action",
        "mood": "Excited"
    },
    {
        "name": "Pathaan",
        "genre": "Action",
        "mood": "Excited"
    },
    {
        "name": "Yeh Jawaani Hai Deewani",
        "genre": "Romance",
        "mood": "Romantic"
    },
    {
        "name": "Jab We Met",
        "genre": "Romance",
        "mood": "Romantic"
    },
    {
        "name": "The Notebook",
        "genre": "Romance",
        "mood": "Romantic"
    },
    {
        "name": "Interstellar",
        "genre": "Sci-Fi",
        "mood": "Curious"
    },
    {
        "name": "The Martian",
        "genre": "Sci-Fi",
        "mood": "Curious"
    },
    {
        "name": "Koi... Mil Gaya",
        "genre": "Sci-Fi",
        "mood": "Curious"
    }
]

# Page settings
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

# Heading
st.title("🎬 Movie Recommendation System")

st.write(
    "Find movies according to your favourite genre "
    "and current mood!"
)

st.info(
    "This project uses predefined IF-THEN rules "
    "to recommend movies."
)

# User input
genre = st.selectbox(
    "Select your favourite genre",
    ["Comedy", "Action", "Romance", "Sci-Fi"]
)

mood = st.selectbox(
    "Select your current mood",
    ["Happy", "Excited", "Romantic", "Curious"]
)

# Recommendation button
if st.button("Recommend Movies"):

    recommendations = []

    # Check every movie
    for movie in movies:

        if (
            movie["genre"] == genre
            and movie["mood"] == mood
        ):
            recommendations.append(movie["name"])

    # Display results
    if recommendations:

        st.subheader("🍿 Recommended Movies")

        for name in recommendations:
            st.success(name)

    else:
        st.warning(
            "No exact match found. "
            "Please try another genre or mood."
        )

st.write("---")
st.caption(
    "Mini Project | Python | Rule-Based AI"
)
