# -*- coding: utf-8 -*-
"""StackingClassifier.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Nnl0QFdzr7D1-aru_-ITQAazakpK_I0Q

*Assuming the necessary libraries are imported.

STACKING CLASSIFIER
"""

from sklearn.ensemble import GradientBoostingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression

# Define the base models
base_models = [
    ('rf', RandomForestClassifier(
        bootstrap=best_params_rf['bootstrap'],
        class_weight=best_params_rf['class_weight'],
        max_depth=best_params_rf['max_depth'],
        max_features=best_params_rf['max_features'],
        min_samples_leaf=best_params_rf['min_samples_leaf'],
        min_samples_split=best_params_rf['min_samples_split'],
        n_estimators=best_params_rf['n_estimators'],
        random_state=42
    )),
    ('gb', GradientBoostingClassifier(n_estimators=100, random_state=42))
]

# Define the meta-model
meta_model = LogisticRegression(random_state=42)

# Create the stacking classifier
stacking_model = StackingClassifier(
    estimators=base_models,
    final_estimator=meta_model,
    cv=10  # You can specify the number of cross-validation folds here
)

# Stratified K-Fold Cross Validation
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

# Perform cross-validation
cross_val_scores_stacking = cross_val_score(stacking_model, X_train_tfidf, y_train, cv=skf, scoring='accuracy')

print(f"Cross-Validation Accuracy Scores (Stacking): {cross_val_scores_stacking}")
print(f"Mean Cross-Validation Accuracy (Stacking): {cross_val_scores_stacking.mean()}")

# Fit the stacking model to the training data
stacking_model.fit(X_train_tfidf, y_train)

# Predict on test data
y_pred_stacking = stacking_model.predict(X_test_tfidf)

# Evaluate model performance
accuracy_stacking = accuracy_score(y_test, y_pred_stacking)
print(f"Accuracy (Stacking): {accuracy_stacking:.2f}")

print("Classification Report (Stacking):")
print(classification_report(y_test, y_pred_stacking))