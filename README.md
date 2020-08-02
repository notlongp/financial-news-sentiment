# Financial News Sentiment using NLP, Machine Learning, and Deep Learning
This project assessed the sentiment of financial news headlines and preview texts using TextBlob, vaderSentiment, Machine Learning with spaCy, and Deep Learning with Artificial Neural Network (nltk tokenization and spaCy pipeline) . Data is scraped from 3 major financial news website (CNBC, Reuters, the Guardian). Training data was retrieved from [kaggle](https://www.kaggle.com/ankurzing/sentiment-analysis-for-financial-news)

# About the project
## Part 0 - Data Collecting
This script scraped information about articles from CNBC, Reuters, the Guardian for the past 2.5 years (except Reuters since their archive only store articles for around 2 years). This script is not required to be run as the data has already been scraped in /data/.

## Part 1 - Data Cleaning
It's important to run this part before running any other part in the repository as it makes sense of the raw input data and store it inside the Jupyter notebook environment for reusability purposes.

## Part 2 - Exploratory Data Analysis
Since the data is straight forward and text-based, there are not much to explore about it. However, it's important to keep in mind the number of articles written per day/per month in order to carry this project to assess the correlation between financial news sentiment and the fluctuation of S&P500 index price in the upcoming project.

## Part 3 - Natural Language Processing with TextBlob
Applied Python’s TextBlob to perform text polarity analysis, and used clustering algorithms (K-Means Clustering and Natural Break Optimization) to categorize positive, neutral, and negative articles.

## Part 4 - Natural Language Processing with vaderSentiment
Applied Python’s vaderSentiment to perform text polarity analysis, and used clustering algorithms (K-Means Clustering and Natural Break Optimization) to categorize positive, neutral, and negative articles.

## Part 5 - Natural Language Processing with nltk and application of Deep Learning models (ANN, CNN) with Google News Word2Vec
In order to run this part properly, first you need to download Google News Word2vec bin.gz file [here](https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit) and place it inside folder /data/.
