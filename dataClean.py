# Input  : Sentence
# Output : Cleaned sentence

# Algorithm 
# Step 01 - Get sentence 
# Step 02 - Convert to lowercase
# Step 03 - Remove special characters 
# Step 04 - Remove strings with length one
# Step 05 - Remove stopwords 
# Step 06 - Lemmatize words 
# Step 07 - Return cleaned sentence 

# Usage
# Step 01 - import dataClean as DC
# Step 02 - Call DC.dataClean(text) where text is the sentence to be cleaned

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import customStopWordsRemoval as CSWR
import re

def convertToLowerCase(text):
    return text.lower()

def removeStopWords(text):
    cachedStopWords = stopwords.words("english")
    return CSWR.customStopWordsRemoval(" ".join([word for word in text.split() if word not in cachedStopWords]))

def removeSpecialCharacters(text):
    return re.sub('[^A-Za-z0-9]+', ' ', text)

def removeSingleCharacters(text):
    return " ".join(word for word in word_tokenize(text, language="english") if len(word) > 1)

def lemmatizeWords(text):
    lmtzr = WordNetLemmatizer()
    return " ".join(lmtzr.lemmatize(word) for word in word_tokenize(text, language="english"))

def dataClean(text):
    return lemmatizeWords(
        removeStopWords(
            removeSingleCharacters(
                removeSpecialCharacters(
                    convertToLowerCase(text)
                )
            )
        )
    )

