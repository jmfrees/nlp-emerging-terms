# STL
import os
from collections import Counter

# PDM
from gensim.models import Phrases, TfidfModel
from gensim.corpora import Dictionary

# LOCAL
from semantic_extraction.preprocess import CorpusReader

print("Reading data")
models_path = os.path.join(".", "models")
filename = "g4boyz5m"
file_ext = ".csv"
filepath = os.path.join(".", "datasets", filename + file_ext)

data = list(CorpusReader(filepath))
dct = Dictionary()
# Needs BoW to be created for checking against model??
model = TfidfModel(dictionary=dct)


counter = Counter()
for d in Bag_of_Words:
    if not d:
        continue
    max_word = max(map(lambda k: (dct[k[0]], k[1]), model[d]), key=lambda x: x[1])[0]
    counter[max_word] += 1

print(counter.most_common(10))
