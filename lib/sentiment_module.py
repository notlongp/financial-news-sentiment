import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def cleaning_data(string):
    review = re.sub('[^a-zA-Z]', ' ', string)
    review = review.lower().split()
    return review


def tokenize_stem(string):
    review = cleaning_data(string)
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)

    return review

def cluster_extraction(nn_output):
    sentiments = []
    for item in nn_output:
        for i in range(0,3):
            if item[i] == max(item):
                sentiments.append(i)
    return sentiments

def combine_sentiments(sentiments1, sentiments2):
    mutual_sentiments = []
    for s1, s2 in zip(sentiments1, sentiments2):
        if s1 +s2 > 2:
            mutual_sentiments.append(2)
        elif s1 + s2 == 2:
            mutual_sentiments.append(1)
        elif s1 + s2 < 2:
            mutual_sentiments.append(0)
    return mutual_sentiments