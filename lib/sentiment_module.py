import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def tokenize_stem(string):
    review = re.sub('[^a-zA-Z]', ' ', string)
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)

    return review

# corpus = crop_text("Business live  Markets hope for progress over EU recovery fund; US consumer confidence drops â€“ as it happened")
# print(corpus)

# from sklearn.feature_extraction.text import CountVectorizer
# cv = CountVectorizer(max_features = 1500)
# X = cv.fit_transform([corpus]).toarray()
# print(X)
