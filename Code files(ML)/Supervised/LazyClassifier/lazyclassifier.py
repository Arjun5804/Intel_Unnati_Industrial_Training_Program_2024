# -*- coding: utf-8 -*-
"""LazyClassifier.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/155shg7yD8zXaVBVuuYRprXd3_Ou8fBCP

LAZY CLASSIFIER
"""

from lazypredict.Supervised import LazyClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.utils import shuffle
from imblearn.over_sampling import SMOTE
import pandas as pd
import numpy as np

# Assuming df is your DataFrame with 'ReviewContent' and 'Sentiment_encoded' columns

# Shuffle the dataset
df = shuffle(df, random_state=42)

# Prepare data for training
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['ReviewContent']).toarray()  # Convert to dense array
y = df['Sentiment_encoded']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply SMOTE to the training data
smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

# Convert back to DataFrame for LazyPredict
X_train_df = pd.DataFrame(X_train_smote, columns=vectorizer.get_feature_names_out())
X_test_df = pd.DataFrame(X_test, columns=vectorizer.get_feature_names_out())

# Initialize LazyClassifier
clf = LazyClassifier(predictions=True)

# Fit and evaluate models
models_summary, predictions = clf.fit(X_train_df, X_test_df, y_train_smote, y_test)

print(models_summary)