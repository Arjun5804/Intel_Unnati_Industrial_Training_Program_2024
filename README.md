# Intel_Unnati_Industrial_Training_Program_2024
 Project Title: Intel Products Sentiment Analysis from Online Reviews

This project involves the sentiment analysis of Intel product reviews using a combination of machine learning and deep learning models. The primary focus is on reviews from e-commerce platforms such as Amazon and Flipkart.

Table of Contents
Project Overview
Folder Structure
Installation
Usage
Results
Contributing
License
Project Overview
This project entails scraping product reviews from e-commerce platforms, preparing and labeling the dataset into four categories (positive, negative, competition sentiment, and future expectation), performing exploratory data analysis (EDA), and training multiple machine learning models. It also involves the fine-tuning of a Llama 3 model for improved performance.

Steps:
Scraping Data: Fetch reviews from Amazon and Flipkart.
Data Preparation: Label the data into four sentiment categories.
EDA: Analyze and visualize data distributions and patterns.
Data Cleaning: Remove stopwords, punctuation, and perform lemmatization.
Feature Extraction: Vectorize review content and encode sentiment labels.
Model Training: Train various ML models (SVC, RandomForest, XGBoost, Naive Bayes) with hyperparameter tuning.
Ensemble Methods: Implement stacking and voting classifiers.
Deep Learning: Fine-tune Llama 3 model for sequence classification. Also various models like ANN, CNN, LSTM, BiLSTM, RoBERTa are evaluated.
Evaluation: Assess model performance using various metrics.

Usage

The requirements are present in the code files, you can check it there!
Scraping Data
Run the scrapers in the Scrapper folder to fetch the latest reviews.

Data Preparation and EDA
Use the notebooks in the EDA folder for exploratory data analysis and data preparation steps.

Training ML Models
Use the code files in the Code files folder to train various machine learning models.

Training DL Models
Use the notebooks in the Colab Notebooks for DL and LLM folder to train deep learning models and the fine-tuned Llama 3 model.

Testing
Run the models on the test datasets provided in the Train and Test data files folder to evaluate their performance.

Results
The results of the trained models, including performance metrics and visualizations, are documented in the intel_final_report and Project PPT folders.

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
 
 
