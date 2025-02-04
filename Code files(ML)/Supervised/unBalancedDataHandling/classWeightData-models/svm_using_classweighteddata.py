# -*- coding: utf-8 -*-
"""SVM-Using-ClassWeightedData.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gX3isMv5eCl6ZMVoq4-yMGWphqgeVVso

*Assuming that the necessary libraries are imported

CLASS WEIGHTED DATA SVM
"""

import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.utils import shuffle
from sklearn.utils.class_weight import compute_class_weight
import numpy as np


# Define the parameter grid for RandomizedSearchCV
param_grid = {
    'C': [0.1, 1, 10, 100],
    'gamma': ['scale', 'auto'],
    'kernel': ['linear', 'rbf', 'poly'],
    'class_weight': ['balanced', None]  # Try both balanced and None
}

# Initialize SVC classifier
svc = SVC()

# Initialize RandomizedSearchCV
random_search = RandomizedSearchCV(estimator=svc, param_distributions=param_grid, scoring='accuracy',
                                   cv=5, n_iter=25, random_state=42, verbose=2, n_jobs=-1)

# Fit RandomizedSearchCV
random_search.fit(X_train, y_train)

# Best parameters and estimator
best_params = random_search.best_params_
best_estimator = random_search.best_estimator_

print(f"Best Parameters: {best_params}")

# Predict on test data
y_pred = best_estimator.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

print("Classification Report:")
print(classification_report(y_test, y_pred))