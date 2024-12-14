# Content-based Movie Recommendation System
**Project Overview**

This project is a content-based movie recommendation system developed using the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle. It allows users to input a movie name and receive a list of 5 similar movies based on content features such as genres, cast, crew, and plot descriptions. The recommendation model has been serialized into movies.pkl and similarity.pkl files for efficient deployment on Render or Streamlit.

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
**Note:** 
Due to file size limitations on GitHub, the similarity.pkl file (176 MB) has not been included in the repository. This file is essential for running the recommendation system. Instructions to generate it are provided below.

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

3. Generate similarity.pkl:
   
- Open the Jupyter Notebook movie-recommender-system.ipynb and run the cells to create the similarity.pkl file. Save the file in the project directory.


4. Run the application:
```
python app.py
```

**Deployment Challenges**

While the project is functional locally, deployment on Streamlit Cloud has been challenging due to the size of the similarity.pkl file (176 MB), which exceeds GitHub's file size limit. Attempts to use Git LFS were unsuccessful so far. Possible solutions being explored include:

- Hosting large files on an external storage service (e.g., AWS S3, Google Drive) and fetching them during app startup.
- Splitting the similarity.pkl file into smaller parts for easier upload.

**Contributing**

Contributions are welcome! Feel free to fork this repository and submit pull requests for improvements or bug fixes.

**Acknowledgements**

- [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) for the data.
- The Python and data science communities for their open-source tools and libraries.
