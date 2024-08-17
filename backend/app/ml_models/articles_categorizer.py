# Import necessary libraries
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


class ArticleCategorizer:
    def __init__(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Book1.xlsx"))
        self.df = pd.read_excel(file_path, sheet_name="Sheet1")

    def categorize(self, input_title):
        self.df['Title'] = self.df['Title'].str.lower()  # Convert to lowercase
        self.df['Title'] = self.df['Title'].str.replace('[^\w\s]', '')  # Remove punctuation and special characters

        # Feature extraction using TF-IDF
        vectorizer = TfidfVectorizer(stop_words='english')
        X = vectorizer.fit_transform(self.df['Title'])

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, self.df['Category'], test_size=0.2, random_state=42)

        # Train a K-Nearest Neighbors classifier
        k_neighbors = 5  # You can adjust the number of neighbors as needed
        clf = KNeighborsClassifier(n_neighbors=k_neighbors)
        clf.fit(X_train, y_train)

        # Test article
        test_article = input_title

        # Preprocess the test article
        test_article = test_article.lower()
        test_article = test_article.replace('[^\w\s]', '')

        # Feature extraction for the test article
        X_test_article = vectorizer.transform([test_article])

        # Predict the category of the test article
        predicted_category = clf.predict(X_test_article)

        return predicted_category[0]
