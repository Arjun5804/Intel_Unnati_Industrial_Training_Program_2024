# -*- coding: utf-8 -*-
"""NaiveBias-RandomizedSearchCV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/155shg7yD8zXaVBVuuYRprXd3_Ou8fBCP

*assuming necessary libraries are imported

Naive Bias RANDOMIZED SERACH CV
"""

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd

# Assuming the data is preprocessed and loaded into the DataFrame df

# Shuffle the dataset
df = shuffle(df, random_state=42)

# Define features and target variable
X = df['ReviewContent']
y = df['Sentiment_encoded']

# Stratified split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# TF-IDF Vectorization
tfidf = TfidfVectorizer(max_features=5000)
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Define the parameter grid
param_grid = {
    'alpha': [0.1, 0.5, 1.0, 5.0, 10.0]
}

# Initialize MultinomialNB
nb = MultinomialNB()

# Initialize RandomizedSearchCV
random_search_nb = RandomizedSearchCV(estimator=nb, param_distributions=param_grid, scoring='accuracy',
                                      cv=5, n_iter=50, random_state=42, verbose=2, n_jobs=-1)

# Fit RandomizedSearchCV
random_search_nb.fit(X_train_tfidf, y_train)

# Best parameters and estimator
best_params_nb = random_search_nb.best_params_
best_estimator_nb = random_search_nb.best_estimator_

print(f"Best Parameters (Naive Bayes): {best_params_nb}")

# Predict on test data
y_pred_nb = best_estimator_nb.predict(X_test_tfidf)

# Evaluate model performance
accuracy_nb = accuracy_score(y_test, y_pred_nb)
print(f"Accuracy (Naive Bayes): {accuracy_nb:.2f}")

print("Classification Report (Naive Bayes):")
print(classification_report(y_test, y_pred_nb))