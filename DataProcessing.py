#!/usr/bin/env python
# coding: utf-8

# ## Preprocessing Data
# Most important ways of preprocessing data used in NLP pipelines: 
# ### 1. Removing tags
#     - eg. Removal of HTML tags
#     - use BeautifulSoup
# ### 2. Removing accented characters
#     - eg. converting é to e
# ### 3. Expanding Contractions
#     - eg. ain't to is not
# ### 4. Removing special characters
#     - Special characters often add extra noise in unstructured text
#     - Simple regular expressions (regex) can be used to achieve this
# ### 5. Stemming and lemmatization
#     - obtaining the base form of a word is called stemming.
#     - stemming removes word suffix to get base form of the word
#     - eg. of stemming : watches, watching and watched :: base word is watch
#     + lemmatization removes word affixes to get base form of the word
# ### 6. Stopwords
#     - eg. removing "a", "an", "the" etc
#     - these are words that have no meaning when constructing meaningful features from text
#     
# ### Other extra operations:
# + Tokenization
# + Removing extra white space
# + Text lowercasing
# + Spelling corrections
# + Grammatical error corrections
# + Removing repeated characters

# In[1]:


# Remove HTML tags
import re
from bs4 import BeautifulSoup

def strip_html_tags(text):
    soup = Beautifulsoup(text, "html.parser")
    [s.extract() for s in soup(['iframe', 'script'])]
    stripped_text = soup.get_text()
    stripped_text = re.sub(r'[\r|\n|\r\n]+', '\n', stripped_text)
    return stripped_text


# In[2]:


# Remove Accented Characters
import unicodedata

def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text


# In[3]:


# Expand Contractions
from contractions import CONTRACTION_MAP

def expand_contractions(text, contraction_mapping = CONTRACTION_MAP):
    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping_keys())), flags = re.IGNORECASE|re.DOTALL)
    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expand_contraction = contraction_mapping.get(match)                            if contraction_mapping.get(match)                            else contraction_mapping.get(match.lower())
        expand_contraction = first_char + expanded_contraction[1:]
        return expanded_contraction


# In[5]:


# Spacy performs parts of speech tagging and effective lemmatization for each token. Hence using Spacy instead
# Lemmatization

import spacy
nlp = spacy.load('en', parse = True, tag = True, entity = True)
# just an example text
# text = 'The car crashed over a big mountainous region it crashed and crashed again!'
def lemmatize_text(text):
    text = nlp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    return text


# In[6]:


# Remove special characters
def remove_special_characters(text, remove_digits = False):
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)
    return text


# In[8]:


# Remove stopwords
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
tokenizer = ToktokTokenizer()
stopword_list = nltk.corpus.stopwords.words('english')

def remove_stopwords(text, is_lower_case = False):
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    
    if is_lower_case:
        filtered_tokens = [token for token in tokens if token not in stopword_list]
    else:
        filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text       


# In[9]:


# Text Normalizer
def normalize_corpus(corpus, html_stripping = True, contraction_expansion = True, accented_char_removal = True, text_lower_case = True, text_lemmatization = True, special_char_removal = True, stopword_removal = True, remove_digits = True):
    normalized_corpus = []
    
    #normalize each document in corpus
    for doc in corpus:
        
        # strip HTML
        if html_stripping:
            doc = strip_html_tags(doc)
        
        # remove accented characters
        if accented_char_removal:
            doc = remove_accented_chars(doc)
            
        # expand contractions
        if contraction_expansion:
            doc = expand_contractions(doc)
            
        # lowercase the text
        if text_lower_case:
            doc = doc.lower()
            
        # remove extra newlines
        doc = re.sub(r'[\r|\n|\r\n]+', ' ', doc)
        
        # lemmatize text
        if text_lemmatization:
            doc = lemmatize_text(doc)
            
        # remove special characters and\or digits
        if special_char_removal:
            # insert spaces between special characters to isolate them
            special_char_pattern = re.compile(r'([{.(-)!}])')
            doc = special_char_pattern.sub(" \\1 ", doc)
            doc = remove_special_characters(doc, remove_digits = remove_digits)
            
        # remove extra whitespace
        doc = re.sub(' +', ' ', doc)
        
        # remove stopwords
        if stopword_removal:
            doc = remove_stopwords(doc, is_lower_case = text_lower_case)
            
        normalized_corpus.append(doc)
        
    return normalized_corpus


# In[ ]:




