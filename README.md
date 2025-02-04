# Intel_Unnati_Industrial_Training_Program_2024
<h1>Intel Products Sentiment Analysis from Online Reviews</h1>

<p>This project involves the sentiment analysis of Intel product reviews using a combination of machine learning, deep learning and LLM models. Since our team has chosen Category A reviews(user reviews), the primary focus is on reviews from e-commerce platforms such as Amazon and Flipkart. The products under scope of our project are Intel Core 12th, 13th and 14th generation Desktop processors that include the i3, i5, i7 and i9 categories. The reviews dataset is new, as the dataset contains reviews upto 3rd July 2024(latest data scrapped on 3rd July 2024).</p>

<h2>Table of Contents</h2>
<ul>
  <li><a href="#project-overview">Project Overview</a></li>
  <li><a href="#folder-structure">Folder Structure</a></li>
  <li><a href="#project-flow">Project Flow</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#results">Results</a></li>
  <li><a href="#contributing">Contributing</a></li>
  <li><a href="#license">License</a></li>
</ul>

<h2 id="project-overview">Project Overview</h2>
<p>This project entails scraping product reviews from e-commerce platforms, preparing and labeling the dataset into four categories (positive, negative, competition sentiment, and future expectation), performing exploratory data analysis (EDA), and training multiple machine learning models. It also involves the fine-tuning of a Llama 3 model for improved performance.</p>

<h3>Steps:</h3>
<ol>
  <li><strong>Scraping Data</strong>: Fetch reviews from Amazon and Flipkart.</li>
  <li><strong>Data Preparation</strong>: Label the data into four sentiment categories.</li>
  <li><strong>EDA</strong>: Analyze and visualize data distributions and patterns.</li>
  <li><strong>Data Cleaning</strong>: Remove stopwords, punctuation, and perform lemmatization.</li>
  <li><strong>Feature Extraction</strong>: Vectorize review content and encode sentiment labels.</li>
  <li><strong>Model Training</strong>: Train various ML models (SVC, RandomForest, XGBoost, Naive Bayes) with hyperparameter tuning.</li>
  <li><strong>Ensemble Methods</strong>: Implement stacking and voting classifiers.</li>
  <li><strong>Deep Learning</strong>: Fine-tune Llama 3 model for sequence classification. Evaluate various models like ANN, CNN, LSTM, BiLSTM, and RoBERTa.</li>
  <li><strong>Evaluation</strong>: Assess model performance using various metrics.</li>
</ol>

<h2 id="folder-structure">Folder Structure</h2>
<ul>
  <li><strong>Scrapper</strong>: Contains scrapper files for fetching e-commerce Intel reviews.</li>
  <li><strong>Code files</strong>: Machine Learning code files.</li>
  <li><strong>Colab Notebooks for DL and LLM</strong>: Proof of work for Deep Learning and LLM models.</li>
  <li><strong>Datasets</strong>: Used at different points of time.</li>
  <li><strong>Final models</strong>: Fine-tuned Llama 3 models.</li>
  <li><strong>ML notebooks</strong>: Proof of work for Machine Learning models.</li>
  <li><strong>Train and Test data files</strong>: Training and testing datasets.</li>
  <li><strong>EDA</strong>: Exploratory Data Analysis.</li>
  <li><strong>reviews_dataset</strong>: Contains the review dataset.</li>
  <li><strong>intel_final_report</strong>: Detailed final report.</li>
  <li><strong>Project PPT</strong>: Project presentation slides.</li>
</ul>

<h2 id="project-flow">Project Flow</h2>
<p>Below is the project flow diagram that illustrates the process:</p>
<img src="Project flow.png" alt="Project Flow Diagram" />

<h2 id="installation">Installation</h2>
<p>To get started, clone the repository and install the required dependencies:</p>
<pre><code>git clone https://github.com/Arjun5804/Intel_Unnati_Industrial_Training_Program_2024.git
cd Intel_Unnati_Industrial_Training_Program_2024
pip install -r requirements.txt</code></pre>

<h2 id="usage">Usage</h2>

<h3>Scraping Data</h3>
<p>Run the scrapers in the <code>Scrapper</code> folder to fetch the latest reviews. Update the URLs if required(only amazon or flipkart)</p>

<h3>Data Preparation and EDA</h3>
<p>Use the notebook: <code>Exploratory_Data_Analysis</code> folder for exploratory data analysis and data preparation steps.</p>

<h3>Training ML Models</h3>
<p>Use the code files in the <code>Code files</code> folder to train various machine learning models. Check out the ipynb files for LazyClassifier and Data cleaning and preprocessing</p>

<h3>Training DL  and LLM Models</h3>
<p>Use the notebooks in the <code>Colab Notebooks for DL and LLM</code> folder to train deep learning models and the fine-tuned Llama 3 8B model.</p>

<h3>Testing</h3>
<p>Run the models on the test datasets provided in the <code>Train and Test data files</code> folder to evaluate their performance. Codes in all the folders are already tested and are error free(except for codes of Mistral model)</p>

<h2 id="results">Results</h2>
<p>The results of the trained models, including performance metrics and visualizations, are documented in the <code>intel final report</code> and also in the different ipynb files present in the ML and Colab notebooks folders.</p>

<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.</p>

<h2 id="license">License</h2>
<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>







 
