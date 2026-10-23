
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import pickle

# Load the training data
data = pd.read_csv("reviews.csv")

# Separate reviews and labels
X = data["review"]
y = data["sentiment"]

# Create a machine learning model
model = make_pipeline(
    CountVectorizer(),
    MultinomialNB()
)

# Train the model
model.fit(X, y)

# Save the trained model
with open("sentiment_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Machine Learning model trained successfully!")
