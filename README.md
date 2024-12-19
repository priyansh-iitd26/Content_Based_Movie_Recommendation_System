# Content-based Movie Recommendation System

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Project Files](#project-files)
- [How It Works](#how-it-works)
- [Setup Instructions](#setup-instructions)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

---

**Project Overview**

This project is a content-based movie recommendation system developed using the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle. It allows users to input a movie name and receive a list of 5 similar movies based on content features such as genres, cast, crew, and plot descriptions. The recommendation model has been serialized into movies.pkl and similarity.pkl files for efficient deployment on Render or Streamlit.

**Features**

- Content-based recommendation system using movie metadata.
- Suggestions based on genres, cast, crew, and plot similarity.
- Interactive interface built with Python.

**Dataset**

The recommendation model was built using the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). It contains detailed metadata about movies, including genres, cast, crew, and keywords.

**Project Files**

```
Movie-Recommender-System/
├── app.py                          # Main application file to run the recommender
├── movie-recommender-system.ipynb  # Jupyter Notebook for building the model
├── movies.pkl                      # Serialized movie data
├── similarity.pkl                  # Serialized similarity matrix
├── requirements.txt                # Dependencies required for the project
├── README.md                       # Project documentation
```

**How it works**
1. *Data preprocessing*:
 - Extracted relevant features (genres, cast, crew, and keywords) from the TMDB dataset.
 - Cleaned and transformed the data for compatibility with the recommendation algorithm.  
2. *Model Building*:
- Created a content-based similarity model using cosine similarity.
- Serialized the movie data (movies.pkl) and similarity matrix (similarity.pkl) for quick lookup.
3. *Interactive Application*:
- app.py serves as the main interface where users can input a movie name and get recommendations.

**Setup Instructions**
1. Clone the repository to your local machine and navigate to the directory.
```
git clone https://github.com/yourusername/movie-recommender-system.git
cd movie-recommender-system
```
2. Install the required dependencies.
```
pip install -r requirements.txt
```

3. Run the application:
```
python app.py
```

**Contributing**

Contributions are welcome! Feel free to fork this repository and submit pull requests for improvements or bug fixes.

**Acknowledgements**

- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) for the data.
- The Python and data science communities for their open-source tools and libraries.
