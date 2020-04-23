# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')

from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.tag import pos_tag
from requests_html import HTMLSession


STOP_WORDS = set(stopwords.words('english'))

url = 'https://en.wikipedia.org/wiki/Neil_Armstrong'

with HTMLSession() as session:
    response = session.get(url)

text = response.html.xpath("//div[@class='mw-parser-output']")[0].text

words = word_tokenize(text)

cleaned_words = []
for word in words:
    if (word.lower() in STOP_WORDS) or (word.lower() in punctuation):
        continue
    cleaned_words.append(word.lower())

tagged_words = pos_tag(cleaned_words)

noun_words = [word[0] for word in tagged_words if word[1] == 'NN']

nouns_freq = {}

for word in noun_words:

    if word in nouns_freq:
        nouns_freq[word] += 1
    else:
        nouns_freq[word] = 1

nouns_freq = sorted(nouns_freq.items(), key=lambda x: x[1], reverse=True)

nouns_bigrams = [gram for gram in ngrams(cleaned_words, 2) if gram[0] in noun_words]

nouns_phrases = sorted([' '.join(gram) for gram in nouns_bigrams])

with open('wiki.txt', 'w', encoding='utf-8') as f:
    for phrase in nouns_phrases:
        f.write(f'{phrase}\n')