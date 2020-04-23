from string import punctuation

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.stem.snowball import EnglishStemmer


stemmer = EnglishStemmer()

STOP_WORDS = set(stopwords.words('english'))


with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()


sentences = sent_tokenize(text)

words = word_tokenize(text)

cleaned_words = []
for word in words:
    if (word.lower() in STOP_WORDS) or (word.lower() in punctuation):
        continue
    cleaned_words.append(word.lower())


# frequency_words = {}
#
# for word in words:
#
#     st_word = stemmer.stem(word)
#
#     if (st_word in STOP_WORDS) or (st_word in punctuation):
#         continue
#
#     if st_word in frequency_words:
#         frequency_words[st_word] += 1
#     else:
#         frequency_words[st_word] = 1
#
# popular_words = sorted(frequency_words.items(), key=lambda x: x[1], reverse=True)[:5]
# print(popular_words)


phrases = ngrams(cleaned_words, 7)

phrases = [' '.join(gr) for gr in phrases]

frequency_phrases = {}

for ph in phrases:

    if ph in frequency_phrases:
        frequency_phrases[ph] += 1
    else:
        frequency_phrases[ph] = 1

popular_phrases = sorted(frequency_phrases.items(), key=lambda x: x[1], reverse=True)[:5]
print(popular_phrases)
