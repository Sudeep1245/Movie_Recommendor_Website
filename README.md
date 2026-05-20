# Movie Recommender System

## About the Project

This is a content-based movie recommendation system built using NLP techniques and cosine similarity.

The system recommends 5 movies similar to the movie selected by the user.  
The model is trained on a dataset containing more than 4500 movies.

Technologies used:
- Python
- Pandas
- Scikit-learn
- Streamlit
- TF-IDF Vectorization
- Cosine Similarity

---

# Project Workflow

1. Data Cleaning and Preprocessing
2. Feature Engineering
3. TF-IDF Vectorization
4. Cosine Similarity Calculation
5. Movie Recommendation
6. Streamlit Web Application

---

# How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/Sudeep1245/movie-recommender-system.git
```

---

## 2. Move into the Project Directory

```bash
cd movie-recommender-system
```

---

## 3. Create a Virtual Environment

```bash
python -m venv myenv
```

---

## 4. Activate the Virtual Environment

### Windows

```bash
myenv\Scripts\activate
```

### Mac/Linux

```bash
source myenv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Run the Training Pipeline

```bash
python src/train.py
```

This will create:
- `artifacts/movies.pkl`
- `artifacts/vector.pkl`
- `artifacts/tfidf.pkl`

---

## 7. Run the Streamlit App

```bash
streamlit run app.py
```

---

# Future Improvements

- Add movie posters using TMDB API
- Add hybrid recommendation system
- Improve recommendation quality using transformers
- Add fuzzy search support
